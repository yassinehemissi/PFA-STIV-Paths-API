import networkx as nx
import matplotlib.pyplot as plt
from db import getCities, getCitiesPairs
def show_graph():
    plt.clf()
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    cities, cities_pairs = getCities()
    cities = list(cities)

    distances = {}
    G = nx.Graph()
    for i in range(len(cities_pairs)):
        G.add_edge(cities_pairs[i][0][0], cities_pairs[i][0][1])
        distances[(cities_pairs[i][0][0], cities_pairs[i][0][1])] = str((cities_pairs[i][1]))

    pos = nx.spring_layout(G)

    nx.draw(G, pos=pos,labels={node: node for node in G.nodes()}, with_labels=True)
    nx.draw_networkx_edge_labels(G, edge_labels=distances, pos=pos)
    plt.title("Villes STIV")
    plt.axis('off')
    plt.savefig('./static/graph_villes.png')

def show_graph_national():
    plt.clf()
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    cities, pairs_national, pairs_regional, pairs_non_national, pairs_non_regional = getCitiesPairs()
    cities = list(cities)

    distances = {}
    G = nx.Graph()
    for i in range(len(pairs_national)):
        G.add_edge(pairs_national[i][0][0], pairs_national[i][0][1])
        distances[(pairs_national[i][0][0], pairs_national[i][0][1])] = str((pairs_national[i][1]))

    pos = nx.spring_layout(G)

    nx.draw(G, pos=pos,labels={node: node for node in G.nodes()}, with_labels=True)
    nx.draw_networkx_edge_labels(G, edge_labels=distances, pos=pos)
    plt.title("Villes STIV")
    plt.axis('off')
    plt.savefig('./static/graph_villes_national.png')


def show_graph_regional():
    plt.clf()
    plt.rcParams["figure.figsize"] = [7.50, 3.50]
    plt.rcParams["figure.autolayout"] = True

    cities, pairs_national, pairs_regional, pairs_non_national, pairs_non_regional = getCitiesPairs()
    cities = list(cities)

    distances = {}
    G = nx.Graph()
    for i in range(len(pairs_regional)):
        G.add_edge(pairs_regional[i][0][0], pairs_regional[i][0][1])
        distances[(pairs_regional[i][0][0], pairs_regional[i][0][1])] = str((pairs_regional[i][1]))

    pos = nx.spring_layout(G)

    nx.draw(G, pos=pos,labels={node: node for node in G.nodes()}, with_labels=True)
    nx.draw_networkx_edge_labels(G, edge_labels=distances, pos=pos)
    plt.title("Villes STIV")
    plt.axis('off')
    plt.savefig('./static/graph_villes_regional.png')