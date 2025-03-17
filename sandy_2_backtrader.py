# failed code just for reference

from datetime import datetime
import backtrader as bt

class SmaCross(bt.SignalStrategy):
    def __init__(self):
        sma = bt.ind.SMA(period=50)
        price = self.data
        crossover = bt.ind.Crossover(price, sma)
        self.signal_add(bt.SIGNAL_LONG, crossover)

cerebro = bt.Cerebro()

data = bt.feeds.YahooFinance(dataname="BTC-USD", fromdate=datetime(2015, 1, 1),
                                  todate=datetime(2021, 1, 1))

cerebro.adddata(data)  # No need for data.setenvironment(self) anymore
cerebro.addstrategy(SmaCross)

cerebro.run()
cerebro.plot()