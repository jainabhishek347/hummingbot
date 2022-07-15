

#Crypto Trading using HummingBot

In order to make profits from trading cryptocurrencies, it  is essential to utilize right strategies which enable trader to place orders at right price and right time. <br/>
While lot of research backed strategies are already being widely used in the market by numerous traders. The successful traders are more likely to come with their own custom strategies for trading.
For creation of custom strategies needs to have a deep understanding of the cryptocurrency market along with sound knowledge of statistics.  <br/>
While most traders may read the market well, they may not have adequate knowledge of statistics to come up with profitable trading strategies. <br/>
This is where our project comes to the rescue!  <br/>
Our project harvests the power of artificial intelligence and machine learning to suggest parameters and their ranges which help in development of profitable trading strategies. 
The profitable strategies can then be deployed on he Hummingbot by developing Python scripts for the strategies.  <br/>
This ensures that the loss is minimized and profit is maximized and is user is free from hassle of complex mathematical calculations. <br/>

The machine learning process involves following key steps:
**Creation of Dataset:** 
To develop an accurate machine learning model, it is essential to have a good dataset with adequate number of data points that can be used for training and testing the model. For cryptocurrencies, a wide variety of data sources are available through which data for creating dataset can be collected. After creation of dataset, it needs to be cleaned and preprocessed to make it appropriate for the training and testing process. <br/>
**Selection of machine learning technique/ algorithm:** 
Due to rapid advancements in the domain of machine learning, numerous machine learning algorithms and techniques are available for a wide range of tasks. It is essential to select a machine learning model that would provide desired results based on the given dataset. <br/>
**Development of machine learning model:**  
To create machine learning Python is used as it provided a wide range of machine learning related functionalities and libraries such as TensorFlow, Jupyter Notebook, Keras etc. While creating model it is necessary to set the model parameters according to the requirements to achieve optimum results. <br/>
**Training of machine learning model:** 
Training of the model helps in identifying its accuracy, which is essential before it is deployed in production. Training of the model can take considerable time depending on factors such as processor used, size and nature of dataset, complexity of model etc. <br/>
**Obtain Optimized Parameters and Develop Strategy:** 
Post training of the model, input data is fed into it to obtained optimized parameter that help in development of trading strategy. <br/> 
Deploy the strategy on Hummingbot:
As per the developed strategy, scripts are coded in Python which can be deployed on Hummingbot and can be tested using paper trading mode.  <br/>

![image](https://user-images.githubusercontent.com/2360904/179184290-6f634f1b-4b54-4045-9a0d-ae4cbe8beabe.png)
 <br/>
Due to Non Disclosure Agreement, it is not possible to share the entire process along with the codebase. However we have added some sample scripts in the repo to show how they work on Hummingbot. <br/>
To rum this scripts, please follow these steps:
1) Install and set up HummingBot
2) Download the scripts and place them in the Hummingbot_files/hummingbot_scripts folder
3) Open Hummingbot instance and run the script using command :
   start --script <filename>
