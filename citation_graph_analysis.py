import sys
sys.path.append('/home/home4/ychen/Code/python-lib') # add the path of networkx in Duke-CS cluster

from networkx import *
from citation_library import *
import numpy
from datetime import datetime
import math

fake_users = [53491, 88872]

file_weighted_graph = open("gs_weighted_collaboration_graph_bak.txt", "r");
#file_noweighted_graph = open("gs_weighted_collaboration_graph.txt", "r");

file_name = open("gs_name.txt", "r");
file_profile = open("gs_profile.txt", "r");

lines_profile = file_profile.read().split("\n")

max_node_id = 0;

all_total_citation = []; all_h_index = []; all_g_index = []; all_domain = [];

for x in lines_profile:
	per_line = x.split(' ')
	if (len(per_line) == 5): # skip the final blank line
		# ID / total_citation / h-index / g-index / CS?
		max_node_id = max(max_node_id, int(per_line[0]))
		all_total_citation.append(int(per_line[1]))
		all_h_index.append(int(per_line[2]))
		all_g_index.append(int(per_line[3]))
		all_domain.append(int(per_line[4]))
		# output to libsvm here
		# class : 0 - faculty, 1 - students/postdocs
		# format: class t:total h:h-idx g:g-idx c:centrality
		# format:   1 1:50 2:8 3:11 4:0.002


print 'Max Node ID:', max_node_id


lines_name = file_name.read().split("\n")

all_name = []

for x in lines_name:
	all_name.append(x)

lines_graph = file_weighted_graph.read().split("\n")



#bb= file_noweighted_graph.readlines().split("\n")
#G_weighted = nx.DiGraph()
G_weighted = nx.Graph()
G_noweighted = nx.Graph()

G_all = nx.Graph()

# Adding the nodes
for i in range(0, max_node_id+1):
	#all_domain[i] = 1
	G_all.add_node(i)
	if (all_domain[i] == 1):
		G_weighted.add_node(i)
		G_noweighted.add_node(i)


# Adding the edges
for x in lines_graph:
	nodes=x.split(' ')
	if (len(nodes) == 3): # skip the final blank line
		#print int(nodes[0]), int(nodes[1]), int(nodes[2])
		G_all.add_edge(int(nodes[0]), int(nodes[1]))
            
		if (all_domain[int(nodes[0])] == 0 or all_domain[int(nodes[1])] == 0):
			continue
		if ((int(nodes[0]) in fake_users) or (int(nodes[1]) in fake_users)):
			continue
			
		G_noweighted.add_edge(int(nodes[0]), int(nodes[1]))
		if (nodes[2] > 1.1):
			G_weighted.add_edge(int(nodes[0]), int(nodes[1]), weight=1.0/((float(nodes[2]))**0.5));

#		G_weighted.add_edge(int(nodes[0]), int(nodes[1]), freq=float(nodes[2]));
#		G_weighted.add_edge(int(nodes[1]), int(nodes[0]), freq=float(nodes[2]));
		#freq = float(nodes[2])

r = degree_assortativity_coefficient(G_all)
print("All Assortativity coefficient: %3.1f"%r)

#G_weighted.add_edge(int(nodes[0]), int(nodes[1]), weight=1.0/(float(nodes[2])**1))

# Get largest connected component as subgraph
SUB_G = connected_component_subgraphs(G_noweighted)
print len(G_noweighted), ':',
for x in SUB_G:
	print len(x),
print
H = connected_component_subgraphs(G_noweighted)[0]
print len(H)
sub_nodes = H.nodes()



#G_noweighted=G_noweighted.subgraph(sub_nodes)
#G_weighted=G_weighted.subgraph(sub_nodes)


# Cacluate weight of "G_weighted"
#for x in G_weighted.nodes():
#	out_ed = G_weighted.out_edges(x)
#	total_co = 0;
#	for y in out_ed:
#		total_co += G_weighted[y[0]][y[1]]['freq']
#	for y in out_ed:
#		G_weighted[y[0]][y[1]]['weight'] = 1.0 / (G_weighted[y[0]][y[1]]['freq'] / total_co);
#		G_weighted[y[0]][y[1]]['weight'] = 1.0 / ((G_weighted[y[0]][y[1]]['freq'] )**1);

print 'Number of Nodes=', len(G_noweighted)
deg = G_noweighted.degree().values()
print 'Degree: ',
showpercentile(deg)
#print connected_components(G_noweighted)

r = degree_assortativity_coefficient(G_noweighted)
print("Assortativity coefficient: %3.1f"%r)

#print weakly_connected_component_subgraphs(G_noweighted)

#result=weakly_connected_commponent_subgraphs(G_noweighted)
    #for r in result:
#print r

print datetime.now()


# {39593: 2.1670135659548426e-06, 45827: 0.0018706453337144111, 15821: 0.0, 32763: 0.0, 106492: 0.00020060202091675338, 79925: 0.0, }


centrality_weighted = betweenness_centrality(G_weighted, weight='weight')
print '** Betweeness Centrality (Weight) **'
analysis_centrality_result(centrality_weighted, all_name, all_h_index, all_g_index)

centrality_weighted = closeness_centrality(G_weighted, distance='weight')
print '** Closeness Centrality (Weight) **'
analysis_centrality_result(centrality_weighted, all_name, all_h_index, all_g_index)

centrality_noweighted = betweenness_centrality(G_noweighted)
print '** Betweeness Centrality (No weight) **'
analysis_centrality_result(centrality_noweighted, all_name, all_h_index, all_g_index)

centrality_noweighted = closeness_centrality(G_noweighted)
print '** Closeness Centrality (No weight) **'
analysis_centrality_result(centrality_noweighted, all_name, all_h_index, all_g_index)



