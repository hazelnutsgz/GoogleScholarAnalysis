import sys
sys.path.append('/home/home4/ychen/Code/python-lib') # add the path of networkx in Duke-CS cluster

from networkx import *
from citation_library import *
import numpy
from datetime import datetime
import math

fake_users = [53491, 88872]

#file_weighted_graph = open("gs_weighted_collaboration_graph_bak.txt", "r");
file_svm_noweighted_graph = open("gs_svm_collaboration_graph.txt", "r");

file_profile = open("gs_svm_informetrics.txt", "r");

lines_profile = file_profile.read().split("\n")

max_node_id = 0;

all_total_citation = []; all_h_index = []; all_g_index = []; all_if_faculty = [];
all_if_aau = [];
all_name = []

seq= [];

for x in lines_profile:	
	line_info = x.split('$$')
	# 
	
	if (len(line_info)< 2):
		continue
	
	per_line = line_info[1].split(' ')
	if (len(per_line) == 6): # skip the final blank line
		# ID / total_citation / h-index / g-index / aau_stat / faculty?
		all_name.append(line_info[0])
		seq.append(int(per_line[0]))
		max_node_id = max(max_node_id, int(per_line[0]))
		all_total_citation.append(int(per_line[1]))
		all_h_index.append(int(per_line[2]))
		all_g_index.append(int(per_line[3]))
		all_if_aau.append(int(per_line[4]))
		all_if_faculty.append(int(per_line[5]))
		# output to libsvm here
		# class : 0 - faculty, 1 - students/postdocs
		# format: class t:total h:h-idx g:g-idx c:centrality
		# format:   1 1:50 2:8 3:11 4:0.002

#print seq
print 'Max Node ID:', max_node_id
print len(all_total_citation)
print len(seq)

for i in range(0, max_node_id):
	if (i != seq[i]):
		print i,

# 0 - 15137, in total 15137 nodes

lines_graph= file_svm_noweighted_graph.read().split("\n")



#bb= file_noweighted_graph.readlines().split("\n")
#G_weighted = nx.DiGraph()
#G_weighted = nx.Graph()
G_noweighted = nx.Graph()

# Adding the nodes
for i in range(0, max_node_id+1):
	#all_domain[i] = 1
	#if (all_domain[i] == 1):
	#G_weighted.add_node(i)
	#if (i > 12000):
	#	continue
	G_noweighted.add_node(i)


# Adding the edges
for x in lines_graph:
	nodes=x.split(' ')
	if (len(nodes) == 2): # skip the final blank line
		#print int(nodes[0]), int(nodes[1]), int(nodes[2])
#		if (all_domain[int(nodes[0])] == 0 or all_domain[int(nodes[1])] == 0): # not CS user
#			continue
#		if ((int(nodes[0]) in fake_users) or (int(nodes[1]) in fake_users)):
#			continue
#		if (int(nodes[0]) > 12000 or int(nodes[1]) > 12000):
#			continue
		G_noweighted.add_edge(int(nodes[0]), int(nodes[1]))


#		G_weighted.add_edge(int(nodes[0]), int(nodes[1]), freq=float(nodes[2]));
#		G_weighted.add_edge(int(nodes[1]), int(nodes[0]), freq=float(nodes[2]));
		#freq = float(nodes[2])

print 'Number of Nodes=', len(G_noweighted)
deg = G_noweighted.degree().values()
print 'Degree: ',
showpercentile(deg)
#print connected_components(G_noweighted)

#print weakly_connected_component_subgraphs(G_noweighted)

#result=weakly_connected_commponent_subgraphs(G_noweighted)
    #for r in result:
#print r

print datetime.now()


# {39593: 2.1670135659548426e-06, 45827: 0.0018706453337144111, 15821: 0.0, 32763: 0.0, 106492: 0.00020060202091675338, 79925: 0.0, }



whole_centrality_set =  betweenness_centrality(G_noweighted)
print '** Betweeness Centrality (No weight) **'

print datetime.now()


f_svm_complete = open('gs_svm_complete.txt', 'w')


for x in whole_centrality_set:
	print x, all_name[x], ':',
	print all_if_faculty[x], 
	print all_total_citation[x], 
	print all_h_index[x], 
	print all_g_index[x], 
	print all_if_aau[x],
	print whole_centrality_set[x], 
	print deg[x]
	f_svm_complete.write(str(all_if_faculty[x])+' 1:'+str(all_total_citation[x])+' 2:'+str(all_h_index[x])+' 3:'+str(all_g_index[x])+ ' 4:'+str(deg[x])+' ')
	
	if (all_if_aau[x] >= 0):
		#f_svm_informetrics.write(' 4:1 5:0\n')
		f_svm_complete.write(' 5:1 6:0\n')
	else:
		#f_svm_informetrics.write(' 4:0 5:1\n')
		f_svm_complete.write(' 5:0 6:1\n')

f_svm_complete.close()


