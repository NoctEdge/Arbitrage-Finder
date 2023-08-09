import ccxt

class ArbitrageFinder:
    def __init__(self, exchanges):
        self.exchanges = exchanges

    def fetch_prices(self, symbols):
        prices = {}
        for exchange in self.exchanges:
            try:
                ticker = exchange.fetch_tickers(symbols)
                for symbol in symbols:
                    if symbol in ticker:
                        if symbol not in prices:
                            prices[symbol] = {}
                        prices[symbol][exchange.name] = ticker[symbol]['last']
            except ccxt.ExchangeError as e:
                print(f"Error fetching prices from {exchange.name}: {e}")
        return prices

    def find_arbitrage_opportunities(self, symbols):
        prices = self.fetch_prices(symbols)
        for symbol in symbols:
            if symbol in prices and len(prices[symbol]) >= 2:
                exchanges = list(prices[symbol].keys())
                for i in range(len(exchanges) - 1):
                    for j in range(i + 1, len(exchanges)):
                        exchange1 = exchanges[i]
                        exchange2 = exchanges[j]
                        price1 = prices[symbol][exchange1]
                        price2 = prices[symbol][exchange2]
                        price_difference = price2 - price1
                        if price_difference > 0:
                            percentage_difference = (price_difference / price1) * 100
                            print(f"Arbitrage Opportunity for {symbol}: {exchange1} ({price1}) -> {exchange2} ({price2})")
                            print(f"Potential Profit: {price_difference} ({percentage_difference:.2f}%)")
                            print("-----------------")

# Example usage:
# usage:
binance = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
    'enableRateLimit': True
})

bitstamp = ccxt.bitstamp({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_API_SECRET',
    'enableRateLimit': True
})

exchanges = [binance, bitstamp]
symbols = ['BTC/USDT', 'ETH/USDT']

arbitrage_finder = ArbitrageFinder(exchanges)
arbitrage_finder.find_arbitrage_opportunities(symbols)
