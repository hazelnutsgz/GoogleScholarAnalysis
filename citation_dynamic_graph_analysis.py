import sys
sys.path.append('/home/home4/ychen/Code/python-lib') # add the path of networkx in Duke-CS cluster

# import matplotlib
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt

import random
from networkx import *
from draw_hist import get_plt, get_formatter

import numpy
from citation_library import *

#import matplotlib.pyplot as plt

save_figures = True

def effective_diamater(path_length_seq):
    sorted_seq = sorted(path_length_seq)
    return sorted_seq[int(len(path_length_seq)*0.9)]

def graph_metrics(G):
	## nodes, edges, avg deg, avg cc
    median_deg = numpy.median(sorted(G.degree().values()))
    avg_deg = numpy.average(sorted(G.degree().values()))
    avg_cc = networkx.average_clustering(G)
    print G.number_of_nodes(), G.number_of_edges(), G.number_of_edges() * 2.0 / (G.number_of_nodes() * (G.number_of_nodes() - 1)), median_deg, "%.2f" % avg_deg, "%.2f" % avg_cc



min_year = 1990
max_year = 2015



f_dyn =open("processed_data/gs_collaboration_yearly_graph.txt", "r")
f_collaboration_data = f_dyn.read().split("\n"); f_collaboration_data = f_collaboration_data[:-1]

f_year_info = open("processed_data/gs_earliest_year.txt", "r")
f_yr_data = f_year_info.read().split("\n"); f_yr_data = f_yr_data[:-1]

year_info = [];
for current_line in f_yr_data:
    year_info.append(int(current_line))
        #    if (int(current_line) > 0 and int(current_line) <= current_yr):
        #print int(current_line)
#G_current.add_node(int(current_line))


num_line_no_year = 0; total_line = 0

for current_line in f_collaboration_data:
    line_info = current_line.split(",")
    if (year_info[int(line_info[1])] < 0 or year_info[int(line_info[2])] < 0):
        continue
    total_line+=1
    if (int(line_info[0])<0):
        num_line_no_year += 1

print num_line_no_year * 100.0/total_line


print 'total nodes:', len(year_info)
print 'year', ':', '# of nodes', '# of edges', '# edges/# nodes', 'Avg. degree', 'Giant Component (%)'

num_node_seq = []; num_edge_seq = []; per_giant_seq = []; effective_diamater_seq = [];

for current_yr in range(min_year, max_year+1):
    G_current = Graph()

    for cur_node in range(0, len(year_info)):
        if (year_info[cur_node] > 0 and year_info[cur_node] <= current_yr):
            G_current.add_node(cur_node)
    for current_line in f_collaboration_data:
        line_info = current_line.split(",")
        if (int(line_info[0]) > 0 and int(line_info[0])<=current_yr):
            G_current.add_edge(int(line_info[1]), int(line_info[2]))
        elif (int(line_info[0]) < 0):
            # get a random but reasonable year
            #print line_info
            min_possible_year = max(year_info[int(line_info[1])], year_info[int(line_info[2])])
            delta_year = 2015 - min_possible_year
            #print delta_year
#            if (min_possible_year <= current_yr):
            if (min_possible_year + random.randint(0, delta_year+1) <= current_yr):
                G_current.add_edge(int(line_info[1]), int(line_info[2]))


    print current_yr, ":",
    print G_current.number_of_nodes(), G_current.number_of_edges(),
    print G_current.number_of_edges() * 2.0 / (G_current.number_of_nodes()*(G_current.number_of_nodes()-1)), # density
    print "%.2f" % numpy.average(G_current.degree().values()), # degree
    print "%.2f" % average_clustering(G_current), # clustering coefficient
    num_node_seq.append(G_current.number_of_nodes()); num_edge_seq.append(G_current.number_of_edges())

    SUB_G = connected_component_subgraphs(G_current)

    Largest_component = Graph();
    
    for x in SUB_G:
        if len(x) > len(Largest_component):
            Largest_component = x
    print 'Largest connected component:',
    print '# of nodes:', Largest_component.number_of_nodes(), Largest_component.number_of_nodes() * 100.0 / G_current.number_of_nodes(), '% ',

    per_giant_seq.append(Largest_component.number_of_nodes() * 100.0 / G_current.number_of_nodes())

    num_node = Largest_component.number_of_nodes()
    if (num_node < 1000):
        node_subset = Largest_component.nodes()
    else:
        node_subset = [];
        for x in range(0, 1000):
            node_subset.append(random.choice(Largest_component.nodes()))
    result_seq = []
    for x in node_subset:
        distance_seq = shortest_path_length(Largest_component,source=x)
    for y in distance_seq:
        if (distance_seq[y] > 0): #remove zero values
            result_seq.append(distance_seq[y])
    current_effective_diameter = effective_diamater(result_seq)

#    current_effective_diameter = diameter(Largest_component)
    print '90th d:', current_effective_diameter,
    effective_diamater_seq.append(current_effective_diameter)
    r=degree_assortativity_coefficient(G_current)
    print("Assortativity coefficient: %3.2f"%r)

print num_node_seq
print num_edge_seq
print per_giant_seq

print effective_diamater_seq
if (save_figures):
    #The fraction of nodes that are part of the giant connected component over time
    plt = get_plt()
    ax=plt.gca()
    ax.xaxis.set_major_formatter(get_formatter()) 
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    plt.figure()
    plt.plot(range(min_year, max_year+1), per_giant_seq, '-o')
    plt.xlabel('Year')
    plt.ylabel('Percenage (%)')
    plt.ylim([0, 60])
    plt.title("Evolution of Giant")
    plt.savefig('gscholar_evolution_giant.png')

    plt.figure()
    plt.loglog(num_node_seq, num_edge_seq, '-o')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Number of Edges')
    plt.ylim([100, 1000000])
    plt.title("Evolution of Density")
    #    plt.title('Probability Density Function')
    plt.savefig('gscholar_evolution_density.png')

    # plt.figure()
    # plt.plot(range(min_year, max_year+1), effective_diamater_seq, '-o')
    # plt.xlabel('Year')
    # plt.ylabel('Effective Diameter')
    # plt.title("Evolution of Diameter")
    # plt.savefig('scholar_evolution_effective_diameter.png')

    plt.figure()
    plt.plot(range(min_year, max_year+1), sorted(effective_diamater_seq, reverse=True), '-o')
    plt.xlabel('Year')
    plt.ylabel('Effective Diameter')
    plt.ylim([0, 20])
    plt.title("Evolution of Diameter")
    plt.savefig('scholar_evolution_effective_diameter2.png')




f_nodes = open("gs_graph_nodes.txt", "r")
f_edges = open("gs_collaboration_graph.txt", "r")

f_yr_nodes = open("gs_graph_yr_nodes.txt", "r")
f_yr_edges = open("gs_collaboration_yearly_graph.txt", "r")

all_nodes = f_nodes.read().split("\n"); all_nodes = all_nodes[:-1]
all_edges = f_edges.read().split("\n"); all_edges = all_edges[:-1]

all_yr_nodes = f_yr_nodes.read().split("\n"); all_yr_nodes = all_yr_nodes[:-1]
all_yr_edges = f_yr_edges.read().split("\n"); all_yr_edges = all_yr_edges[:-1]


G_all = Graph()

for x in all_nodes:
	G_all.add_node(int(x))
for x in all_edges:
	y = x.split(",")
	G_all.add_edge(int(y[0]), int(y[1]))

graph_metrics(G_all)



# ##Analysis of seperate year
# for current_yr in range(min_year, max_year+1):
# 	print current_yr, ":",
# 	G_tmp = Graph()
# 	for x in all_yr_nodes:
# 		y=x.split(" ")
# 		#print y
# 		if (int(y[0]) == current_yr):
# 			G_tmp.add_node(int(y[1]))
# 	for x in all_yr_edges:
# 		y=x.split(",")
# 		if (int(y[0]) == current_yr):
# 			G_tmp.add_edge(int(y[1]), int(y[2]))
# 	graph_metrics(G_tmp)

#for i in range(0, max_node_id+1):
	##all_domain[i] = 1
	#G_all.add_node(i)

#for x in lines_graph:
#	nodes=x.split(' ')
	#if (len(nodes) == 3): # skip the final blank line
		#print int(nodes[0]), int(nodes[1]), int(nodes[2])
	#	G_all.add_edge(int(nodes[0]), int(nodes[1]))
