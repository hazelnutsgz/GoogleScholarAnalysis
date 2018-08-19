import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


s = [0.5516275686488452, 0.5707388144408491, 0.5958236951014177, 0.6183789937676062, 0.6488288434490966, 0.6816002603677694, 0.749638790961105, 0.7990474661529405,0.8537432123675855, 0.9155352933652493, 0.9837366990030546, 1.0633814219953581, 1.1506333059420248, 1.2390880028013567, 1.3427121771217712, 1.4645051654843146,1.5742300223680652, 1.6855057697745501, 1.8068598041342168, 1.9471740982675376, 2.1065314473923222, 2.2796744162513596, 2.5002428020236445, 2.775123789528642, 3.149757293218628, 3.286229780616022]
plt.plot(range(1990,2016), s)
plt.xlabel("year")
plt.ylabel("density = edges/nodes")
plt.title("density ")
plt.savefig("density.png")

