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
		
		

def graph_metrics(G):
	# nodes, edges, avg deg, avg cc
	sorted_deg = sorted(G.degree().values())
	median_deg = numpy.median(sorted_deg)
	avg_deg = numpy.average(sorted_deg)
	sorted_cc = sorted(networkx.clustering(G).values())
	avg_cc = numpy.average(sorted_cc)# networkx.average_clustering(G)
	density = G.number_of_edges() * 2.0 / (G.number_of_nodes() * (G.number_of_nodes() - 1))
	print G.number_of_nodes(), G.number_of_edges(), density, median_deg, "%.3f" % avg_deg, "%.3f" % avg_cc
	numpy.savetxt('result_all_deg_cdf.txt', get_per_from_seq(sorted_deg), fmt = "%.2f")
	numpy.savetxt('result_all_cc_cdf.txt', get_per_from_seq(sorted_cc), fmt = "%.2f")
	s = list(networkx.connected_components(G))
	print len(s[0]), len(s[1]), len(s[2])
	#print get_per_from_seq(sorted_deg)
	#print get_per_from_seq(sorted_cc)
	return


def subset_graph_metrics(G, node_list, meta_info):
	# nodes, edges, avg deg, avg cc
	sorted_deg = sorted(G.degree(node_list).values())
	median_deg = numpy.median(sorted_deg)
	avg_deg = numpy.average(sorted_deg)
	sorted_cc = sorted(networkx.clustering(G, node_list).values())
	avg_cc = numpy.average(sorted_cc)# networkx.average_clustering(G)
	#print G.number_of_nodes(), G.number_of_edges(), G.number_of_edges() * 2.0 / (G.number_of_nodes() * (G.number_of_nodes() - 1)), median_deg, "%.2f" % avg_deg, "%.2f" % avg_cc
	print len(node_list), median_deg, avg_deg, avg_cc
	if (meta_info == 4): # computer science
		numpy.savetxt('result_cs_deg_cdf.txt', get_per_from_seq(sorted_deg), fmt = "%.2f")
		numpy.savetxt('result_cs_cc_cdf.txt', get_per_from_seq(sorted_cc), fmt = "%.2f")
	elif (meta_info == 5): # bio
		numpy.savetxt('result_bio_deg_cdf.txt', get_per_from_seq(sorted_deg), fmt = "%.2f")
		numpy.savetxt('result_bio_cc_cdf.txt', get_per_from_seq(sorted_cc), fmt = "%.2f")
	elif (meta_info == 6):
		numpy.savetxt('result_phy_deg_cdf.txt', get_per_from_seq(sorted_deg), fmt = "%.2f")
		numpy.savetxt('result_phy_cc_cdf.txt', get_per_from_seq(sorted_cc), fmt = "%.2f")
	return


f_nodes = open("processed_data/gs_graph_nodes.txt", "r")
f_edges = open("processed_data/gs_collaboration_graph.txt", "r")

#f_country_nodes = open("gs_country_graph_nodes.txt", "r")
f_profiles = open("processed_data/gs_profile.txt", "r")


#f_yr_nodes = open("gs_graph_yr_nodes.txt", "r")
#f_yr_edges = open("gs_collaboration_yearly_graph.txt", "r")

all_nodes = f_nodes.read().split("\n"); all_nodes = all_nodes[:-1]
all_edges = f_edges.read().split("\n"); all_edges = all_edges[:-1]

all_profiles = f_profiles.read().split("\n"); all_profiles = all_profiles[:-1]


G_all = Graph()

for x in all_nodes:
	G_all.add_node(int(x))
for x in all_edges:
	y = x.split(",")
	G_all.add_edge(int(y[0]), int(y[1]))

graph_metrics(G_all)


# gs_profile
# 58755 86 6 8 0 1

for current_subject in range(4, 7):
	print current_subject, ":",
	
	curr_node_list = []
	for ii in range(0, len(all_nodes)):
		xx = all_profiles[ii]
		yy = xx.split(" ")
		if (int(yy[current_subject]) == 1):
			curr_node_list.append(ii)

	subset_graph_metrics(G_all, curr_node_list, current_subject)

all_citation = []; all_h_idx = []; all_g_idx = []; cs_citation = []; cs_h_idx = []; cs_g_idx = []; bio_citation = []; bio_h_idx = []; bio_g_idx = []; phy_citation = []; phy_h_idx = []; phy_g_idx = [];
for ii in range(0, len(all_nodes)):
	xx = all_profiles[ii]
	yy = xx.split(" ")
	tmp_citation = int(yy[1]); tmp_h_idx = int(yy[2]); tmp_g_idx = int(yy[3])
	all_citation.append(tmp_citation); all_h_idx.append(tmp_h_idx); all_g_idx.append(tmp_g_idx)
	if (int(yy[4]) == 1):
		cs_citation.append(tmp_citation); cs_h_idx.append(tmp_h_idx); cs_g_idx.append(tmp_g_idx)
	if (int(yy[5]) == 1):
		bio_citation.append(tmp_citation); bio_h_idx.append(tmp_h_idx); bio_g_idx.append(tmp_g_idx)
	if (int(yy[6]) == 1):
		phy_citation.append(tmp_citation); phy_h_idx.append(tmp_h_idx); phy_g_idx.append(tmp_g_idx)

numpy.savetxt('result_all_citation_cdf.txt', get_per_from_seq(sorted(all_citation)), fmt = "%.2f")
numpy.savetxt('result_all_h_idx_cdf.txt', get_per_from_seq(sorted(all_h_idx)), fmt = "%.2f")
numpy.savetxt('result_all_g_idx_cdf.txt', get_per_from_seq(sorted(all_g_idx)), fmt = "%.2f")

numpy.savetxt('result_cs_citation_cdf.txt', get_per_from_seq(sorted(cs_citation)), fmt = "%.2f")
numpy.savetxt('result_cs_h_idx_cdf.txt', get_per_from_seq(sorted(cs_h_idx)), fmt = "%.2f")
numpy.savetxt('result_cs_g_idx_cdf.txt', get_per_from_seq(sorted(cs_g_idx)), fmt = "%.2f")

numpy.savetxt('result_bio_citation_cdf.txt', get_per_from_seq(sorted(bio_citation)), fmt = "%.2f")
numpy.savetxt('result_bio_h_idx_cdf.txt', get_per_from_seq(sorted(bio_h_idx)), fmt = "%.2f")
numpy.savetxt('result_bio_g_idx_cdf.txt', get_per_from_seq(sorted(bio_g_idx)), fmt = "%.2f")

numpy.savetxt('result_phy_citation_cdf.txt', get_per_from_seq(sorted(phy_citation)), fmt = "%.2f")
numpy.savetxt('result_phy_h_idx_cdf.txt', get_per_from_seq(sorted(phy_h_idx)), fmt = "%.2f")
numpy.savetxt('result_phy_g_idx_cdf.txt', get_per_from_seq(sorted(phy_g_idx)), fmt = "%.2f")

		
print 'Average (t/h/g): ', numpy.average(all_citation), numpy.average(all_h_idx), numpy.average(all_g_idx)
print 'cs Average (t/h/g): ', numpy.average(cs_citation), numpy.average(cs_h_idx), numpy.average(cs_g_idx)
print 'Bio Average (t/h/g): ', numpy.average(bio_citation), numpy.average(bio_h_idx), numpy.average(bio_g_idx)
print 'Physics Average (t/h/g): ', numpy.average(phy_citation), numpy.average(phy_h_idx), numpy.average(phy_g_idx)
'''
print 'STD (t/h/g): ', numpy.std(all_citation), numpy.std(all_h_idx), numpy.std(all_g_idx)
print 'cs STD (t/h/g): ', numpy.std(cs_citation), numpy.std(cs_h_idx), numpy.std(cs_g_idx)
print 'Bio STD (t/h/g): ', numpy.std(bio_citation), numpy.std(bio_h_idx), numpy.std(bio_g_idx)
'''
print 'Median (t/h/g): ', numpy.median(all_citation), numpy.median(all_h_idx), numpy.median(all_g_idx)
print 'cs Median (t/h/g): ', numpy.median(cs_citation), numpy.median(cs_h_idx), numpy.median(cs_g_idx)	
print 'Bio Median (t/h/g): ', numpy.median(bio_citation), numpy.median(bio_h_idx), numpy.median(bio_g_idx)
print 'Physics Median (t/h/g): ', numpy.median(phy_citation), numpy.median(phy_h_idx), numpy.median(phy_g_idx)


