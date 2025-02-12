import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

seed = 0
random.seed(seed)
np.random.seed(seed)

G = nx.Graph()
# G.add_node("A")
# G.add_node("B")
# G.add_node("C")
# G.add_node("D")
# G.add_node("E")
G.add_edge("A","B")
G.add_edge("A","D")
G.add_edge("A","C")
G.add_edge("B","E")
G.add_edge("E","D")
G.add_edge("C","D")


G.add_edge("A","B")

nx.draw(G,with_labels=True, node_color="red",font_color="white",font_size=20, node_size=3000)
plt.margins(0.2)
plt.show()