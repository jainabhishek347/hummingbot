

from hummingbot.core.event.events import (
    OrderFilledEvent,
    OrderCancelledEvent,
    SellOrderCompletedEvent,
    SellOrderCreatedEvent,
    BuyOrderCompletedEvent,
    BuyOrderCreatedEvent, 
)
from hummingbot.strategy.script_strategy_base import Decimal, OrderType, ScriptStrategyBase

import logging

class Regular_Buy_BNB(ScriptStrategyBase):
    
    last_ordered_ts = 0.
    interval_for_buying = 10.
    buy_amount = Decimal("100")
    markets = {"binance_paper_trade": {"BNB-BTC"}}

    def buy_on_tick(self):
    
        if self.last_ordered_ts < (self.current_timestamp - self.interval_for_buying):
        
            price = self.connectors["binance_paper_trade"].get_price("BNB-BTC", False)
            amt = self.buy_amount / price
            self.buy("binance_paper_trade", "BNB-BTC", amt, OrderType.LIMIT, price)
            self.last_ordered_ts = self.current_timestamp

    def create_buy_order(self, event: BuyOrderCreatedEvent):
        self.logger().info(logging.INFO, f"The creation of buy order {event.order_id} was successful")
    
    def complete_buy_order(self, event: BuyOrderCompletedEvent):
        self.logger().info(f"The buy order {event.order_id} has been completed")

    def create_sell_order(self, event: SellOrderCreatedEvent):
       
        self.logger().info(logging.INFO, f"The creation of sell order {event.order_id} was successful")

    def complete_sell_order(self, event: SellOrderCompletedEvent):
        
        self.logger().info(f"The sell order {event.order_id} has been successfully completed")

    def fill_order(self, event: OrderFilledEvent):
        
        self.logger().info(logging.INFO, f"The order {event.order_id} has been successfully filled")

    def cancel_order(self, event: OrderCancelledEvent):
        
        self.logger().info(f"The order {event.order_id} has been cancelled")

 

  
