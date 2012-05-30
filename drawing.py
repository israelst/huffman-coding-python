try:
    import matplotlib.pyplot as plt
except:
    raise

import networkx as nx

G=nx.path_graph(8)
nx.draw(G)
#plt.savefig("simple_path.png") # save as png
plt.show() # display

child = (7, None, (3, 'a'), (4, None, (2, None, (1, 'c'), (1, 'i')), (2, 'b')))
freq, label, child = child

