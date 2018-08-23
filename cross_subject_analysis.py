import sys
sys.path.append('/home/home4/ychen/Code/python-lib') # add the path of networkx in Duke-CS cluster

from networkx import *

import numpy
from citation_library import *

def get_per_from_seq(input_seq):
	length = len(input_seq)
	result_seq = []
	for i in range(0, 99):
		point = length * i / 100.0 
		result_seq.append(input_seq[int(point)])
	return result_seq
		

def subset_graph_metrics(G, node_list):
	# nodes, edges, avg deg, avg cc
	sorted_deg = sorted(G.degree(node_list).values())
	median_deg = numpy.median(sorted_deg)
	avg_deg = numpy.average(sorted_deg)
	sorted_cc = sorted(networkx.clustering(G, node_list).values())
	avg_cc = numpy.average(sorted_cc)# networkx.average_clustering(G)
	#print G.number_of_nodes(), G.number_of_edges(), G.number_of_edges() * 2.0 / (G.number_of_nodes() * (G.number_of_nodes() - 1)), median_deg, "%.2f" % avg_deg, "%.2f" % avg_cc
	print len(node_list), median_deg, avg_deg, avg_cc
	
	return


def cross_subject_analysis(subject1, subject2):


	f_nodes = open("processed_data/gs_graph_nodes.txt", "r")
	f_edges = open("processed_data/gs_collaboration_graph.txt", "r")

	#f_country_nodes = open("gs_country_graph_nodes.txt", "r")
	f_profiles = open("process_data/gs_profile.txt", "r")


	#f_yr_nodes = open("gs_graph_yr_nodes.txt", "r")
	#f_yr_edges = open("gs_collaboration_yearly_graph.txt", "r")

	all_nodes = f_nodes.read().split("\n"); all_nodes = all_nodes[:-1]
	all_edges = f_edges.read().split("\n"); all_edges = all_edges[:-1]

	all_profiles = f_profiles.read().split("\n"); all_profiles = all_profiles[:-1]

	G_cross_graph = Graph()

	for x in all_profiles:
		xx = x.split(" ")
		if int(xx[subject1]) == 1 or int(xx[subject2]) == 1: 
			G_cross_graph.add_node(int(x[0]))




	for x in all_edges:
		y = x.split(",")
		profile_1 = all_profiles[int(y[0])].split(" ")
		profile_2 = all_profiles[int(y[1])].split(" ")
		if (profile_1[subject1] == '1' and profile_2[subject2] == '1') or (profile_1[subject2] == '1' and profile_2[subject1] == '1'):
			G_cross_graph.add_edge(int(y[0]), int(y[1]))
			print "LLLL"

# gs_profile
# 58755 86 6 8 0 1
	
	curr_node_list = []
	for ii in range(0, len(all_profiles)):
		xx = all_profiles[ii]
		yy = xx.split(" ")
		if (int(yy[subject2]) == 1) and (int(yy[subject1]) == 1):
			curr_node_list.append(ii)


	subset_graph_metrics(G_cross_graph, curr_node_list)



cross_subject_analysis(4, 5)






