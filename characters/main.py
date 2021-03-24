from typing import List, Any

import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from pathlib import Path
import operator
import itertools


main_matrix = np.loadtxt("mat1.txt")
char_num = len(main_matrix) #duzina matrice, kao .length() u javaScript
# print(N)

char_json_names = Path('characters.txt').read_text()
char_json_names = char_json_names.split("\n") #napravi array iz JSON objekta koji sam dobio
#kreiram praznu mrezu
network = nx.Graph()
# print(network)
for i in range(char_num):
    network.add_node(char_json_names[i]) #add node je kao .append
for i in range(char_num):
    for j in range(char_num):
       if (main_matrix[i][j] > 0):
           network.add_edge(char_json_names[i], char_json_names[j])
node_size = []
for node in network:
    node_size.append(network.degree(node) * 50)
position = nx.spring_layout(network, k = 1, iterations =  25)

nx.draw(network, pos = position, node_size = node_size, with_labels= True)

#povezanost lika
char_name_degree = {}
for i in network.degree():
    char_name_degree[i[1]] = i[0]
    char_names_sorted = sorted(char_name_degree.items(), key = operator.itemgetter(0), reverse =  True)
first_five = list(char_names_sorted)[0:5]
print(first_five)

#centralizovanost likova
char_names_centrality = nx.closeness_centrality(network)
char_centrality_sorted = sorted(char_names_centrality.items(), key=lambda item: item[1], reverse = True)
first_five_centrality =  list(char_centrality_sorted)[0:5]
print(first_five_centrality)

#povezanost medju njima
char_names_betweenness = nx.betweenness_centrality(network)
char_betweenness_sorted = sorted(char_names_betweenness.items(), key=lambda item: item[1], reverse = True)
first_five_betweenness =  list(char_betweenness_sorted)[0:5]
print(first_five_betweenness)

plt.show()