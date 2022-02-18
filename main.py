import numpy as np
import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import sys


def loadAsset(asset):
    loaded_asset = pdr.get_data_yahoo(asset)
    day = np.arange(1, len(loaded_asset) + 1)
    loaded_asset['day'] = day
    loaded_asset.drop(columns=['Adj Close', 'Volume'], inplace=True)
    loaded_asset = loaded_asset[['day', 'Open', 'High', 'Low', 'Close']]
    print("\n\n=============================================\n\n")
    print("Asset Information:\n\n")
    print(loaded_asset.info())
    print("\n\n=============================================\n")

    loaded_asset['9-day'] = loaded_asset['Close'].rolling(9).mean()
    loaded_asset['21-day'] = loaded_asset['Close'].rolling(21).mean()

    loaded_asset['signal'] = np.where(loaded_asset['9-day'] > loaded_asset['21-day'], 1, 0)
    loaded_asset['signal'] = np.where(loaded_asset['9-day'] < loaded_asset['21-day'], -1, loaded_asset['signal'])
    loaded_asset.dropna(inplace=True)

    loaded_asset['return'] = np.log(loaded_asset['Close']).diff()
    loaded_asset['system_return'] = loaded_asset['signal'] * loaded_asset['return']
    loaded_asset['entry'] = loaded_asset.signal.diff()

    plt.subplot(1, 2, 1)
    plt.rcParams['figure.figsize'] = 12, 6
    plt.grid(True, alpha=.3)
    plt.plot(loaded_asset.iloc[-252:]['Close'], label='loaded_asset')
    plt.plot(loaded_asset.iloc[-252:]['9-day'], label='9-day')
    plt.plot(loaded_asset.iloc[-252:]['21-day'], label='21-day')
    plt.plot(loaded_asset[-252:].loc[loaded_asset.entry == 2].index,
             loaded_asset[-252:]['9-day'][loaded_asset.entry == 2], '^',
             color='g', markersize=12)
    plt.plot(loaded_asset[-252:].loc[loaded_asset.entry == -2].index,
             loaded_asset[-252:]['21-day'][loaded_asset.entry == -2], 'v',
             color='r', markersize=12)
    plt.legend(loc=2)

    plt.subplot(1, 2, 2)
    plt.plot(np.exp(loaded_asset['return']).cumprod(), label='Buy/Hold')
    plt.plot(np.exp(loaded_asset['system_return']).cumprod(), label='System')
    plt.legend(loc=2)
    plt.grid(True, alpha=.3)

    print("\nReturns: ")
    print(np.exp(loaded_asset['return']).cumprod()[-1] - 1)
    print("\nSystem Returns: ")
    print(np.exp(loaded_asset['system_return']).cumprod()[-1] - 1)

    plt.show()


def main():
    loadAsset(sys.argv[1])


main()
