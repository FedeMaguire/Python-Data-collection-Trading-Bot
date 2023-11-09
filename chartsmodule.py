import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplfinance as mpf

def chartRSI():
    chart_df = pd.read_csv('test_chart.csv')
    plt.figure(figsize=(12,3),dpi=150, facecolor='white',layout='tight')
    sns.set_theme(style="whitegrid", palette="dark")
    plt.title("Sochastic RSI")
    plt.axhline(y=0.9, color='grey', linestyle='--')
    plt.axhline(y=0.05, color='grey', linestyle='--')
    sns.lineplot(data=chart_df['stochrsi_k'])
    plt.ylabel(None,loc='center')
    plt.rcParams['ytick.left'] = plt.rcParams['ytick.labelleft'] = False
    plt.rcParams['ytick.right'] = plt.rcParams['ytick.labelright'] = True
    plt.savefig('test_images\\StochRSI_chart.jpg', format='jpg', dpi=150)

def chartCANDLE_STICK():
    # Create the candlestick plot
    chart_df = pd.read_csv('test_chart.csv')
    chart_df['Time'] = pd.to_datetime(chart_df['Time'])
    chart_df.set_index('Time', inplace=True)
    mpf.plot(chart_df, type='candle', style='checkers', figscale=1, figsize=(16, 6), 
             scale_padding={'left': 0.08, 'top': 1, 'right': 0.4, 'bottom': 1},
             savefig=dict(fname='test_images\\CANDLE_STICK_chart.jpg',dpi=150))