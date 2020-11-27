from src import ForexArbitrage

#v1 = 5
#tickers1 = ['USD', 'EUR', 'GBP', 'CHF', 'CAD']     # Major Currency Pairs (Us Dollar, Euro, Pound Sterling, Swiss Franc, Canadian Dollar)

#g = Arbitrage.Graph(v1, tickers1)
#g.Bellman_Ford()

#v2 = 4
#tickers2 = ['TRY', 'MXN', 'HUF', 'THB']    # Exotic Currency Pairs (Turkish Lira, Mexican Peso, Hungarian Forint, Thai Baht)

#g = Arbitrage.Graph(v2, tickers2)
#g.Bellman_Ford()

v3 = 6
tickers3 = ['EUR', 'USD', 'HUF', 'MXN', 'TRY', 'CAD']   # Mixed Currencies

g = ForexArbitrage.Graph(v3, tickers3)
g.Bellman_Ford()
