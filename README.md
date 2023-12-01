# :bar_chart::chart_with_upwards_trend::coin:  Python Trading Bot with Graphical User Interface.
![image](https://github.com/FedeMaguire/Python-Trading-Bot/blob/main/screenshots/Screenshot%202023-11-27%20151559.jpg?raw=true)
# Overview
## This is a cryptocurrency trading bot written in Python. It utilizes Binance's API for scheduled live data gathering and the TA library for technical indicator calculations.
![image](https://github.com/FedeMaguire/Python-Trading-Bot/blob/main/screenshots/Screenshot%202023-11-09%20165227.jpg?raw=true)
 # 
![image](https://github.com/FedeMaguire/Python-Trading-Bot/blob/main/screenshots/Screenshot%202023-11-09%20165411.jpg?raw=true)

# How it Works
Live Data is gathered fom Binance using Binance API and a Pandas Frame is generated with the last 200 candles.The trading bot triggers a buy order when a specific condition is met and keeps track of the trade until it needs to be closed based on another condition. It does this by checking for a buy signal generated in a pandas DataFrame corresponding to the Stochastic RSI value K-line equal to or above 0.05, and the previous RSI value K-line was below 0.05. If this condition is met, it places a buy limit order. When an order is placed, the code checks for a sell signal in the same pandas DataFrame corresponding to the RSI value K-line equal to or above 0.9, and the previous RSI value K-line was below 0.9. When this condition is met, the order is closed, and the cycle starts over again.

# Graphical User Interface
# 
![image](https://github.com/FedeMaguire/Python-Trading-Bot/blob/main/screenshots/Screenshot%202023-11-09%20165322.jpg?raw=true)
# 
The GUI is coded using the CustomTkinter library to create an easy-to-use environment with clear sections for CHARTS, TRADES, and SETTINGS. LIGHT and DARK modes are available.**Please note that the SETTINGS section is still a work in progress.**
- # Libraries
```
import customtkinter
import os
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
```
 

# Prerequisites
- Binance API key (stored in "keys.py")
- Binance API secret (stored in "keys.py")

# TradingBot
- # Libraries
```
import pandas as pd
import ta #Tecnical indicators
from binance import Client
from datetime import timedelta # Add and substract timestamps
import time
from pytz import timezone
from keys import api_key, api_secret
```
# Charts:
The charts are created using the matplotlib and mplfinance libraries and loaded to the GUI as JPG files every time a new event is scheduled.
- # Libraries:
```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
```


# Disclaimer
This project is for informational purposes only. It is not legal, tax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation, endorsement, or offer to buy or sell any securities or other financial instruments in any jurisdiction. Use at your own risk.

Under no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs, or liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.
