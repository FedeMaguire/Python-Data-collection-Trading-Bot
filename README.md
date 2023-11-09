# :bar_chart::chart_with_upwards_trend::coin:  Python Trading Bot with Graphical User Interface.
 

## This is a cryptocurrency trading bot that uses Binance's API for scheduled live Data gathering and the TA library for tecnical indicator calculations.
# How it works:
The tradingBot trigers a  buy order when a condition is met, and keeps track of the trade until needs to be closed when another condition is met. 
This is done by checking for a buy signal generated in a pandas frame corresponding to the Stochastic RSI value K-line equal or above 0.05, and the previous RSI value K-line was below 0.05, if so, it places a buy limit order. When an order was placed The code checks for a sell signal in the same  Pandas frame corresponding to the RSI value K-line equal or above 0.9 and the previous RSI value K-line was below 0.9, when this condition is met, the order is closed, and the cicle start over again.

# Libraries
```
import pandas as pd
import ta #Tecnical indicators
from binance import Client
from datetime import timedelta # Add and substract timestamps
import time
from pytz import timezone
from keys import api_key, api_secret
``` 

# prerequisits:
- Binances API key (stored in keys.py)
- Binance API secret (stored in keys.py)
# Charts:
- # Libraries:

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf
```
The chart are created using matplotlib and mpfinance libraries and loaded to the gui as JPG files everytime a new event is scheduled.

# Graphical User Interface
- # Libraries:
```
import customtkinter
import os
from PIL import Image
import pandas as pd
import plotly.graph_objects as go
```

The GUI is coded using CustomTkinter library to create an easy to use environment with clear CHARTS, TRADES and SETTINGS sections. LIGHT and DARK mode are available.
**The GUI is still a work in progrss, the SETTINGS section is under work.**
# Disclaimer
This project is for informational purposes only. You should not construe any such information or other material as legal, tax, investment, financial, or other advice. Nothing contained here constitutes a solicitation, recommendation, endorsement, or offer by me or any third party service provider to buy or sell any securities or other financial instruments in this or in any other jurisdiction in which such solicitation or offer would be unlawful under the securities laws of such jurisdiction.

If you plan to use real money, USE AT YOUR OWN RISK.

Under no circumstances will I be held responsible or liable in any way for any claims, damages, losses, expenses, costs, or liabilities whatsoever, including, without limitation, any direct or indirect damages for loss of profits.
