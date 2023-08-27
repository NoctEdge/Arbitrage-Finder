# Arbitrage Finder

A python script that identifies and exploits price differences across different cryptocurrency exchanges.


Please note that To use the code, make sure you have the ccxt library installed. You can install it using the following command:

```bash
pip install ccxt
```

- Fetching Prices: The ```fetch_prices``` method fetches the latest prices for the specified symbols from multiple exchanges using their respective APIs. It stores the prices in a dictionary.
- Finding Arbitrage Opportunities: The ```find_arbitrage_opportunities``` method analyzes the fetched prices to identify arbitrage opportunities. It compares prices between pairs of exchanges for each symbol and calculates the price difference and potential profit. If a profit can be made, it prints the details of the arbitrage opportunity.
- Please note that to use this code, you need to have API keys for the exchanges you wish to fetch prices from. Replace ```'YOUR_API_KEY'``` and ```'YOUR_API_SECRET'``` with your actual API keys for each exchange.

__NOTE:__ Keep in mind that arbitrage opportunities can be short-lived and depend on various factors, including exchange fees, trading volumes, and network delays. This code provides a starting point, but it's important to consider additional factors and thoroughly test any trading strategies before using them with real funds.
