import sys
sys.path.append('/home/home4/ychen/Code/python-lib') # add the path of networkx in Duke-CS cluster

from networkx import *

import numpy
from citation_library import *

def graph_metrics(G, pagerank_dict):
# nodes, edges, avg deg, avg cc
    enable_connected_components = 1
    median_deg = numpy.median(sorted(G.degree().values()))
    avg_deg = numpy.average(sorted(G.degree().values()))
    avg_cc = networkx.average_clustering(G)
    print G.number_of_nodes(), G.number_of_edges(),
    print numpy.average(pagerank_dict.values()),
    print median_deg, "%.3f" % avg_deg, "%.3f" % avg_cc,
    print 'Assortativity', degree_assortativity_coefficient(G)
    if (enable_connected_components):
        connected = sorted(connected_components(G), key = len, reverse=True)
        print len(connected), 'components',
        singleton = 0
        for ii in connected:
            if (len(ii) == 1):
                singleton += 1
        print singleton, 'singletons'
        Gc = max(nx.connected_component_subgraphs(G), key=len)
        print Gc.number_of_nodes(), Gc.number_of_edges(), networkx.average_clustering(Gc)#, diameter(Gc)
        print len(connected[0]), len(connected[1]), len(connected[2]), len(connected[3]), len(connected[4])
    return


def subset_graph_metrics(G, pagerank_dict, node_list):
    # nodes, edges, avg deg, avg cc
    median_deg = numpy.median(sorted(G.degree(node_list).values()))
    avg_deg = numpy.average(sorted(G.degree(node_list).values()))
    avg_cc = numpy.average(networkx.clustering(G, node_list).values())
    #print pagerank_dict
    pagerank_values = []
    for x in node_list:
    	#print x
    	pagerank_values.append(pagerank_dict[x])
    #numpy.average(pagerank(G, alpha=0.9).values()),
    #print G.number_of_nodes(), G.number_of_edges(), G.number_of_edges() * 2.0 / (G.number_of_nodes() * (G.number_of_nodes() - 1)), median_deg, "%.2f" % avg_deg, "%.2f" % avg_cc
    print len(node_list), median_deg, '%.3f' % avg_deg, '%.3f' % avg_cc, numpy.average(pagerank_values)
    return

f_nodes = open("gs_graph_nodes.txt", "r")
f_edges = open("gs_collaboration_graph.txt", "r")


f_country_nodes = open("gs_country_graph_nodes.txt", "r")
f_country_nodes = open("gs_title.txt", "r")
f_profile_nodes = open("gs_profile.txt", "r")



f_yr_nodes = open("gs_graph_yr_nodes.txt", "r")
f_yr_edges = open("gs_collaboration_yearly_graph.txt", "r")

all_nodes = f_nodes.read().split("\n"); all_nodes = all_nodes[:-1]
all_edges = f_edges.read().split("\n"); all_edges = all_edges[:-1]

all_country_nodes = f_country_nodes.read().split("\n"); all_country_nodes = all_country_nodes[:-1]
all_profiles = f_profile_nodes.read().split("\n"); all_profiles = all_profiles[:-1]


# Construct the graph G #

G_all = nx.Graph()

for x in all_nodes:
    G_all.add_node(int(x))
for x in all_edges:
    y = x.split(",")
    G_all.add_edge(int(y[0]), int(y[1]))

#all_deg = G_all.degree().values()

# Discipline-based Data Aggregation #

all_cs_nodes = []; all_bio_nodes = []; all_phy_nodes = [];
all_cs_total = []; all_cs_hidx = []; all_cs_gidx = [];
all_bio_total = []; all_bio_hidx = []; all_bio_gidx = [];
all_phy_total = []; all_phy_hidx = []; all_phy_gidx = [];


all_total = []; all_hidx = []; all_gidx = [];

for x in all_profiles:
    y = x.split(" ")
    cs = int(y[4]); bio = int(y[5]); phy = int(y[6])
    all_total.append(int(y[1])); all_hidx.append(int(y[2])); all_gidx.append(int(y[3]))
    if cs:
        all_cs_nodes.append(int(y[0]))
        all_cs_total.append(int(y[1]))
        all_cs_hidx.append(int(y[2]))
        all_cs_gidx.append(int(y[3]))
    if bio:
        all_bio_nodes.append(int(y[0]))
        all_bio_total.append(int(y[1]))
        all_bio_hidx.append(int(y[2]))
        all_bio_gidx.append(int(y[3]))
    if phy:
        all_phy_nodes.append(int(y[0]))
        all_phy_total.append(int(y[1]))
        all_phy_hidx.append(int(y[2]))
        all_phy_gidx.append(int(y[3]))

print len(all_cs_nodes), len(all_bio_nodes), len(all_phy_nodes)


node_country_id = []

for x in all_country_nodes:
    y = x.split(" ")
    node_country_id.append(int(y[0]))

pagerank_dict = pagerank(G_all, alpha=0.9)

graph_metrics(G_all, pagerank_dict)

#'''
# corrcoef matrix
print '%.2f' % numpy.corrcoef(G_all.degree().values(), all_total)[0][1], '%.2f' % numpy.corrcoef(clustering(G_all).values(), all_total)[0][1], '%.2f' %  numpy.corrcoef(pagerank_dict.values(), all_total)[0][1]
print '%.2f' % numpy.corrcoef(G_all.degree().values(), all_hidx)[0][1], '%.2f' % numpy.corrcoef(clustering(G_all).values(), all_hidx)[0][1], '%.2f' %  numpy.corrcoef(pagerank_dict.values(), all_hidx)[0][1]
print '%.2f' % numpy.corrcoef(G_all.degree().values(), all_gidx)[0][1], '%.2f' % numpy.corrcoef(clustering(G_all).values(), all_gidx)[0][1], '%.2f' %  numpy.corrcoef(pagerank_dict.values(), all_gidx)[0][1]
#'''

print numpy.corrcoef(G_all.degree().values(), pagerank_dict.values())

print 'Avg. Total= %.2f' % numpy.average(all_total), 'Avg. H-idx= %.2f' % numpy.average(all_hidx), 'Avg. G-idx= %.2f' % numpy.average(all_gidx)


# Gender #

print '== Gender =='

# please run: "python citation_name_to_gender.py > gs_gender.txt &" first

f_gender_nodes = open("gs_gender.txt", "r")
all_gender = f_gender_nodes.read().split("\n"); all_gender = all_gender[:-1]
current_idx = 0
male_IDs=[]; male_deg = []; male_pagerank=[]; male_total = []; male_hidx = []; male_gidx = [];
female_IDs=[]; female_deg = []; female_pagerank=[]; female_total = []; female_hidx = []; female_gidx= [];
for x in all_gender:
    if (x == 'male'):
        male_IDs.append(current_idx)
#        male_deg.append(all_deg[current_idx]);
        male_pagerank.append(pagerank_dict[current_idx])
        male_total.append(all_total[current_idx]); male_hidx.append(all_hidx[current_idx]); male_gidx.append(all_gidx[current_idx]);
    elif (x == 'female'):
        female_IDs.append(current_idx)
#        female_deg.append(all_deg[current_idx]);
        female_pagerank.append(pagerank_dict[current_idx])
        female_total.append(all_total[current_idx]); female_hidx.append(all_hidx[current_idx]); female_gidx.append(all_gidx[current_idx]);
    current_idx += 1



print 'Male: ', len(male_hidx), '%.2f' % numpy.average(G_all.degree(male_IDs).values()), '%.2f' % numpy.average(networkx.clustering(G_all, male_IDs).values()), numpy.average(male_pagerank)
print '-> Avg. Total= %.2f' % numpy.average(male_total),'Avg. H-idx= %.2f' % numpy.average(male_hidx), 'Avg. G-idx= %.2f' % numpy.average(male_gidx)
print 'Female: ', len(female_hidx), '%.2f' % numpy.average(G_all.degree(female_IDs).values()), '%.2f' % numpy.average(networkx.clustering(G_all, female_IDs).values()), numpy.average(female_pagerank)
print '->Avg. Total= %.2f' % numpy.average(female_total), 'Avg. H-idx= %.2f' % numpy.average(female_hidx), 'Avg. G-idx= %.2f' % numpy.average(female_gidx)

print '== Academic Titles =='

for current_title in range(1, 4):
    print current_title, ":",	
    curr_node_list = []; current_total = []; current_hidx = []; current_gidx = [];
    for ii in range(0, len(node_country_id)):
        if (node_country_id[ii] == current_title):
            curr_node_list.append(ii)
            current_total.append(all_total[ii]);current_hidx.append(all_hidx[ii]); current_gidx.append(all_gidx[ii]);
                    
    subset_graph_metrics(G_all, pagerank_dict, curr_node_list)
    print '-> Avg. Total= %.2f' % numpy.average(current_total), 'Avg. H-idx= %.2f' % numpy.average(current_hidx), 'Avg. G-idx= %.2f' % numpy.average(current_gidx)


print '== Discipline =='

print 'CS:',
subset_graph_metrics(G_all, pagerank_dict, all_cs_nodes)
print '-> Avg. Total= %.2f' % numpy.average(all_cs_total), 'Avg. H-idx= %.2f' % numpy.average(all_cs_hidx), 'Avg. G-idx= %.2f' % numpy.average(all_cs_gidx)
print 'Bio:',
subset_graph_metrics(G_all, pagerank_dict, all_bio_nodes)
print '-> Avg. Total= %.2f' % numpy.average(all_bio_total), 'Avg. H-idx= %.2f' % numpy.average(all_bio_hidx), 'Avg. G-idx= %.2f' % numpy.average(all_bio_gidx)
print 'Physics:',
subset_graph_metrics(G_all, pagerank_dict, all_phy_nodes)
print '-> Avg. Total= %.2f' % numpy.average(all_phy_total), 'Avg. H-idx= %.2f' % numpy.average(all_phy_hidx), 'Avg. G-idx= %.2f' % numpy.average(all_phy_gidx)


#pagerank_seq = pagerank_dict.values()
f_output_all_hidx = open("unprocessed_data/all_hidx.txt", "w")
f_output_all_gidx = open("unprocessed_data/all_gidx.txt", "w")
f_output_all_pagerank = open("unprocessed_data/all_pagerank.txt", "w")
for ii in range(0, len(all_hidx)):
    f_output_all_hidx.write(str(all_hidx[ii])+'\n')
    f_output_all_gidx.write(str(all_gidx[ii])+'\n')
    f_output_all_pagerank.write(str(pagerank_dict[ii])+'\n')
f_output_all_pagerank.close()
f_output_all_hidx.close()
f_output_all_gidx.close() 