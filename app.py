from flask import Flask, jsonify, send_file
from db import getCitiesPairs, getCout
from path_finder import find_shortest_paths
from graph_visualization import show_graph, show_graph_national, show_graph_regional

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    cities, pairs_national, pairs_regional, pairs_non_national, pairs_non_regional = getCitiesPairs()
    cities = list(cities)
    results = {
        "REGIONAL": [],
        "NATIONAL": [],
        "NREGIONAL": [],
        "NNATIONAL": []

    }
    cout_r, cout_n = getCout()
    for index in range(len(cities)):
        for index2 in range(index, len(cities)):
            if (index == index2):
                continue
            path_national = find_shortest_paths(pairs_national, cities[index], cities[index2], 1)
            path_regional = find_shortest_paths(pairs_regional, cities[index], cities[index2], 1)
            try:
                results["REGIONAL"].append(['->'.join(path_regional[0][0]), path_regional[0][1] * cout_r])
                results["NATIONAL"].append(['->'.join(path_national[0][0]), path_national[0][1] * cout_n])
            except:
                print("A")
            print(path_regional)
    for index in range(len(pairs_non_regional)):
        results['NREGIONAL'].append([str(pairs_non_regional[index][0][0]) + '->' + str(pairs_non_regional[index][0][1]), pairs_non_regional[index][1]])
    for index in range(len(pairs_non_national)):
        results['NNATIONAL'].append([str(pairs_non_national[index][0][0]) + '->' + str(pairs_non_national[index][0][1]), pairs_non_national[index][1]])
    return jsonify(results)


@app.route('/graph')
def plot_graph():
    show_graph()
    return send_file('./static/graph_villes.png',mimetype='image/png')

@app.route('/graph_national')
def plot_national():
    show_graph_national()
    return send_file('./static/graph_villes_national.png',mimetype='image/png')

@app.route('/graph_regional')
def plot_regional():
    show_graph_regional()
    return send_file('./static/graph_villes_regional.png',mimetype='image/png')



if __name__ == '__main__':
    app.run()
