# ForexArbitrage

Python program that detects arbitrage opportunities in the foreign exchange market using Bellman-Ford algorithm.

Given in input a list of currencies, the program:
  
 - Gathers currency pairs from yahoo_finance database, using pandas_datareader subpackage, and organizes them in a matrix data structure.
 - Abstracts the exchange market creating a graph model with currency as nodes and exchange rates as arches.
 - Finds negative cycles in the graph using Bellman-Ford algorithm, that correspond to an arbitrage opportunity.  
 - Computes the possible profit given by the concatenation of the negative cycle.
 - Displays the graph with the negative cycle highlighted using the networkx library.


*Disclaimer:
The arbitrages detected are only theoretical, thus more frequent than in real market, because the program doesn't cover the actual transaction fees imposed by the financial institution you are operating with (as they are variable).
This disparity between theoretical model and reality is accentuated with the trade of exotic currencies. Being very volatile and illiquid, fees will be higher on them as the bid-ask spread is usually large to compensate the lack of liquidity.*
