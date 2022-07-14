import requests
import time
import logging

from hummingbot.core.data_type.order_candidate import OrderCandidate
from hummingbot.core.event.events import OrderFilledEvent, OrderType, TradeType
from hummingbot.core.rate_oracle.rate_oracle import RateOracle
from hummingbot.strategy.script_strategy_base import ScriptStrategyBase
from hummingbot.connector.exchange_base import ExchangeBase
from hummingbot.connector.utils import split_hb_trading_pair

from typing import List
from decimal import Decimal
from statistics import mean



class BuyTRX(ScriptStrategyBase):
    
  
    usdt_amt: Decimal = Decimal("100")
    moving_avg_period: int = 100
    percent_price_decrease: Decimal = Decimal("0.1")
    gap: float = 10.
    last_ordered_ts: float = 0.
    connector_name: str = "binance_paper_trade"
    crypto_pair: str = "TRX-USD"
    base_val, quote_val = split_hb_trading_pair(crypto_pair)
    coversion_in_usd: str = f"{quote_val}-USD"

    markets = {connector_name: {crypto_pair}}

    @property

    def connector(self) -> ExchangeBase:
        
        return self.connectors[self.connector_name]

    def create_order(self) -> List[OrderCandidate]:
        
        closing_price = self.fetch_closing_price(self.crypto_pair)
        start_index = (-1 * self.moving_avg_period) - 1
        avg_closing_price = mean(closing_price[start_index:-1])
        order = []

        if closing_price[-1] < avg_closing_price * (Decimal("1") - self.percent_price_decrease):
            order_price = self.connector.get_price(self.crypto_pair, False) * Decimal("0.9")
            usd_conversion_rate = RateOracle.get_instance().rate(self.coversion_in_usd)
            amount = (self.usdt_amt / usd_conversion_rate) / order_price
            order.append(OrderCandidate(self.crypto_pair, False, OrderType.LIMIT, TradeType.BUY, amount,
                                           order_price))
        return order

    def fetch_closing_price(self, crypto_pair: str) -> List[Decimal]:
       
        url = "https://api.binance.com/api/v3/klines"
        params = {"symbol": crypto_pair.replace("-", ""),
                  "interval": "1d"}
        records = requests.get(url=url, params=params).json()
        return [Decimal(str(record[4])) for record in records]
    
    def place_on_tick(self):
        create_order: List[OrderCandidate] = self.create_order()
        create_order = self.connector.budget_checker.adjust_candidates(create_order, all_or_none=False)
        if create_order:
            self.place_order(create_order)

    def did_fill_order(self, event: OrderFilledEvent):
        
        msg = (f"({event.crypto_pair}) {event.trade_type.name} Order (price: {event.price}) of {event.amount} "
               f"{split_hb_trading_pair(event.crypto_pair)[0]} has been filled.")
        self.log_with_clock(logging.INFO, msg)
        self.notify_hb_app_with_timestamp(msg)

  
    def place_order(self, order: List[OrderCandidate]):
       
        if self.last_ordered_ts > time.time() - self.gap:
            return
        for order_candidate in order:
            if order_candidate.amount > Decimal("0"):
                self.buy(self.connector_name, self.crypto_pair, order_candidate.amount, order_candidate.order_type,
                         order_candidate.price)
                self.last_ordered_ts = time.time()


 
