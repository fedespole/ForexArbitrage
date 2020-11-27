# ForexArbitrage
Python program that detects arbitrage opportunities in the foreign exchange market using Bellman-Ford algorithm.

The program gathers exchange rates from yahoo_finance database, using pandas_datareader subpackage, and organizes them in a matrix data structure.
Then it abstracts the exchange market creating a graph model with currency as nodes and exchange rates as arches.
Finding arbitrage opportunities corresponds to search for a negative cycle in this graph, therefore Bellman-Ford algorithm is used.
After detecting it, the possible profit is computed and the graph (with the negative cycle highlighted) is displayed using the library networkx.


*Disclaimer
The arbitrages detected are only theoretical, thus more frequent than in real market, because the program doesn't cover the actual transaction fees imposed by the financial institution you are operating with (as they are variable).
This disparity between theoretical model and reality is accentuated with the trade of exotic currencies. Because they are volatile and illiquid, the fees will be higher on those as the bid-ask spread is usually large to compensate the lack of liquidity.*
