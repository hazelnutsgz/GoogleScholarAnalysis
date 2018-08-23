    # -*- coding: utf-8 -*-
# get the collaboration graph (weighted)
# get total citation, h-index, g-index, of every author
 
# format
# python citation_preprocess_new.py # default
# python citation_preprocess_new.py n [0-3] # distributed version
 
import os
import numpy
import sys
from citation_library import *
 
reload(sys)
sys.setdefaultencoding('utf-8')
 
 
'''
bioinformatics
complex systems
control theory
embedded systems
evolutionary computation
formal methods
game theory
graph theory
hci
image processing
multi-agent systems
multimedia
natural language processing
optimization
pattern recognition
remote sensing
signal processing
systematics
wireless communications
'''
 
bio_keywords = []
 
min_year = 1930
max_year = 2015
 
 
 
def year_summary(input_year_user): #year_user = set([]) #element: (1950, 1), (2012, 50), (yr, id)
    for i in range(min_year, max_year+1):
        year_count = 0
        for x in input_year_user:       
            if (x[0] == i):
                year_count += 1
    print i, year_count
    return
 
 
filename=os.listdir('gs_result/')
 
total= 0
 
all_name = [];
 
all_total_citation = []; all_h_index = []; all_i10_index = []; all_g_index = []; all_inst = [];
cs_total_citation = []; cs_h_index = []; cs_i10_index = []; cs_g_index = []; cs_inst = [];
neuro_total_citation = []; neuro_h_index = []; neuro_i10_index = []; neuro_g_index = []; neuro_inst = [];
 
paper_data = {}
year_user = set([]) #element: (1950, 1), (2012, 50), (yr, id)
 
f_profile = open("process_data/gs_profile.txt", "w")
f_name = open("process_data/gs_name.txt", "w")
f_year = open("process_data/gs_earliest_year.txt", "w")
f_google_id = open("process_data/gs_google_id.txt", "w")
 
 
f_h_age = open("process_data/gs_h_age.txt", "w") # h-index vs experience
f_g_age = open("process_data/gs_g_age.txt", "w") # g-index vs experience
f_t_age = open("process_data/gs_t_age.txt", "w") # total citation vs experience
 
 
 
f_title = open("process_data/gs_title.txt", "w") # academic title
f_h_idx = open("process_data/gs_h_idx.txt", "w")
f_g_idx = open("process_data/gs_g_idx.txt", "w")
f_t_idx = open("process_data/gs_t_idx.txt", "w")
#f_subject = open("gs_subject.txt", "w")
 
country_list = []
 
for x in filename:
    if (x[-6:]=='.parse'):# and (x[0] in 'DEFGHIJKLMNOPQRSdefghijklmnopqrs'):
        x_name = os.path.join('gs_result/', x);
        lines=open(x_name, "r").read().split('\n')
        #close(x)
        #print 'uid', lines[0], 'name', lines[1], 'index', lines[7],
        # get idx ['413', '364', '10', '9', '11', '9']
        # check if it's a verified account
        affilation_str = lines[2].lower()
        keyword_str = lines[3].lower()
        verified_str = lines[4].lower()
 
 
# removed on Jul. 23, 2015: all authors
        if (verified_str[0] == 'n'):
            continue
 
 
#       if (verified_str[-8:] != 'duke.edu'):
#       if (verified_str[-4:] != '.edu'):
#           continue
        if (verified_str[-4:] == '.edu'):
            country_list.append(1)
        if (verified_str[-3:] == '.uk'):
            country_list.append(2)
        else: # other countries
            country_list.append(0)
 
        xy= eval(lines[7])
        g_index = getGIndex(eval(lines[11]))
        uni_code = getuni(verified_str)
        total_citation = int(xy[0]); h_index = int(xy[2]); i10_index = int(xy[4])
        all_total_citation.append(total_citation); all_h_index.append(h_index); all_i10_index.append(i10_index); all_g_index.append(g_index); all_inst.append(uni_code)
        all_name.append(lines[1])
        f_name.write(lines[1]+'\n')
        f_profile.write(str(total)+' '+str(total_citation)+' '+str(h_index)+' '+str(g_index)+' ')
        f_h_idx.write(str(h_index)+'\n')
        f_g_idx.write(str(g_index)+'\n')
        f_t_idx.write(str(total_citation)+'\n')
        f_google_id.write(str(total)+' '+x+'\n')
        #print h_index, g_index, total_citation, "!",
        #if cnt >= 13:
        #           paper = eval(strs)
        paperlist=[]
        if (len(lines) >= 14):
            earliest_yr = 2015; default_earliest = 1;
            for cnt in range(13, len(lines)):
                if (len(lines[cnt])==0):
                    break
                #print lines[cnt], len(lines[cnt]),
 
                try:
                    paper = eval(lines[cnt])
                except:
                    pass
                paperlen = len(paper)
                if (paperlen > 2):
                    #continue
                    pp = ''
                 
                    # paper[2] : 'CR Lin, M Gerla'
                    # = number of authors
                    #author_list = paper[2]
                 
                    #pp = str(author_num) + '$$'
                 
                    for p in range(1,paperlen): # skip the paper ID (author-aware)
                        pp = pp + paper[p] + '$$'
                            #if (p == 2):
                            #author_num = len(paper[p].split(','))
                    pub_year = paper[paperlen-1]
                    if (pub_year.isdigit() == True):
                        num_yr = int(pub_year)
                        if (num_yr >= min_year and num_yr <= max_year):
                            if (num_yr<earliest_yr):
                                earliest_yr = num_yr; default_earliest = 0;
                        paperlist.append(pp)
 
 
        #print total, lines[1], total_citation, h_index, g_index, len(paperlist)
        #print earliest_yr, h_index
        #print earliest_yr
        if (default_earliest == 1): # cannot find a reasonable year
            f_year.write(str(-1)+"\n")
        else:
            f_year.write(str(earliest_yr)+"\n")
        if (earliest_yr < 2015):
            f_h_age.write(str(h_index)+' '+str(2015-earliest_yr)+'\n') # h-index, and years since the 1st paper
            f_g_age.write(str(g_index)+' '+str(2015-earliest_yr)+'\n') # g-index, and years since the 1st paper
            f_t_age.write(str(total_citation)+' '+str(2015-earliest_yr)+'\n') # total_citation, and years since the 1st paper
        #check title from lines[2]
        if (affilation_str.find("prof") >= 0):
            f_title.write('3\n');
        elif (affilation_str.find("student") >= 0 or affilation_str.find("phd candidate") >= 0 or affilation_str.find("research assistant") >= 0):
            f_title.write("1\n");
        elif (affilation_str.find("postdoc") >= 0 or affilation_str.find("research associate") >= 0 or affilation_str.find("research fellow") >= 0):
            f_title.write("2\n");
        else:
            f_title.write('0\n');
         
        paper_data[total] = paperlist
         
        #print      
         
        if (verified_str.find("cs.") >= 0 or verified_str.find("informatik.") >= 0 or has_cs_keyword(keyword_str)==1 or affilation_str.find("computer") >= 0):
#       if (keyword_str.find("network") >= 0 or keyword_str.find("system") >= 0 or keyword_str.find("cloud") >= 0 or keyword_str.find("distributed") >= 0) and (verified_str.find("cs.") >= 0 or verified_str.find("informatik.") >= 0 or keyword_str.find("computer") >= 0 or keyword_str.find("informat") >= 0 or affilation_str.find("computer") >= 0):
#       if (keyword_str.find("network") >= 0 or keyword_str.find("distributed systems")>= 0):
#       if (keyword_str.find("information retrieval") >= 0 or keyword_str.find("data mining") >= 0 or keyword_str.find("machine learning") >= 0):      
 
            # computer science author
            cs_total_citation.append(total_citation); cs_h_index.append(h_index); cs_i10_index.append(i10_index); cs_g_index.append(g_index); cs_inst.append(uni_code)
            f_profile.write('1 ')
        else:
            f_profile.write('0 ')
 
#       if (keyword_str.find("psychiatry") >= 0 or keyword_str.find("neuro") >= 0):
        if (verified_str.find("neuro.") >= 0 or verified_str.find("med.") >= 0 or has_bio_keyword(keyword_str) == 1 or affilation_str.find("bio") >= 0):
            # neuroscience author
            neuro_total_citation.append(total_citation); neuro_h_index.append(h_index); neuro_i10_index.append(i10_index); neuro_g_index.append(g_index); neuro_inst.append(uni_code)
            f_profile.write('1 ')
        else:
            f_profile.write('0 ')

        if (verified_str.find("phys") >= 0 or affilation_str.find("physics") >= 0 or has_physics_keyword(keyword_str) == 1 ):
            f_profile.write('1 ')
        else:
            f_profile.write('0 ')

        ##Sociology
        if (verified_str.find("soc") >= 0 or affilation_str.find("soci") >= 0 or has_social_keyword(keyword_str) == 1 ):
            f_profile.write('1\n')
            print ("catch social")
        else:
            f_profile.write('0\n')

        total = total +1
 
f_profile.close()
f_name.close(); f_year.close(); f_title.close()
f_h_age.close(); f_g_age.close(); f_t_age.close()
f_h_idx.close(); f_g_idx.close(); f_t_idx.close()
f_google_id.close()
 
#f_subject.close()
 
print len(paper_data), 'users'
 
print '####'
 
#year_summary(year_user)
 
compute_collaboration_graph = 0
 
if (compute_collaboration_graph == 1):
    print datetime.now()
    f_node_list = open("gs_graph_nodes.txt", "w")
    f_country_node_list = open("gs_country_graph_nodes.txt", "w")
    # f_yr_node_list = open("gs_graph_yr_nodes.txt", "w")
 
    for i in range(0, total):
        f_node_list.write(str(i)+"\n")
        f_country_node_list.write(str(country_list[i])+" "+str(i)+"\n")
    #for x in year_user:
    #   f_yr_node_list.write(str(x[0])+" "+str(x[1])+"\n")
    f_node_list.close()
    f_country_node_list.close()
    #f_yr_node_list.close()
     
    f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "w")
    f_graph = open("gs_collaboration_graph.txt", "w")
    f_yr_graph = open("gs_collaboration_yearly_graph.txt", "w")
 
    cmdargs = str(sys.argv)
    if (len(sys.argv) == 2):
        if (sys.argv[1] == '1'):
            f_graph = open("gs_collaboration_graph1.txt", "w")
            f_yr_graph = open("gs_collaboration_yearly_graph1.txt", "w")
        elif (sys.argv[1] == '2'):  
            f_graph = open("gs_collaboration_graph2.txt", "w")
            f_yr_graph = open("gs_collaboration_yearly_graph2.txt", "w")
        elif (sys.argv[1] == '3'):             
            f_graph = open("gs_collaboration_graph3.txt", "w")
            f_yr_graph = open("gs_collaboration_yearly_graph3.txt", "w")
        elif (sys.argv[1] == '0'): 
            f_graph = open("gs_collaboration_graph0.txt", "w")
            f_yr_graph = open("gs_collaboration_yearly_graph0.txt", "w")
    else:
        f_yr_graph = open("gs_collaboration_yearly_graph.txt", "w")
        f_graph = open("gs_collaboration_graph.txt", "w")
 
    #print 'Number of arguments:', len(sys.argv), 'arguments.'
    #print 'Argument List:', str(sys.argv)
 
    f_yr_graph.close()
    f_graph.close()
 
    for i in range(0, total):
        #f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "a")
        if (len(sys.argv) == 2):
            if (i % 4 != int(sys.argv[1])):
                continue
            if (sys.argv[1] == '1'):
                f_graph = open("gs_collaboration_graph1.txt", "a")
                f_yr_graph = open("gs_collaboration_yearly_graph1.txt", "a")
            elif (sys.argv[1] == '2'):
                f_graph = open("gs_collaboration_graph2.txt", "a")
                f_yr_graph = open("gs_collaboration_yearly_graph2.txt", "a")
            elif (sys.argv[1] == '3'):
                f_graph = open("gs_collaboration_graph3.txt", "a")
                f_yr_graph = open("gs_collaboration_yearly_graph3.txt", "a")
            elif (sys.argv[1] == '0'):
                f_graph = open("gs_collaboration_graph0.txt", "a")
                f_yr_graph = open("gs_collaboration_yearly_graph0.txt", "a")
 
        else:
            f_yr_graph = open("unprocessed_data/gs_collaboration_yearly_graph.txt", "a")
            f_graph = open("unprocessed_data/gs_collaboration_graph.txt", "a")
 
        if ((i % 1000) == 0):
            print i,
        for j in range(i+1, total):
            ### old version
            # compare data[i], data[j]
            joint_papers = set(paper_data[i]) & set(paper_data[j])
            if (len(joint_papers) == 0):
                continue
             
            #ok = 0
            #for xx in paper_data[i]:
            #   if (xx in paper_data[j]):
            #        ok = 1
            #        break
            #if (ok == 0):
            #    continue
            f_graph.write(str(i)+','+str(j)+'\n')
            #'''
            joint_year = set()
            for xxx in joint_papers:
                #print xxx
                tmp_paper=xxx.split('$$')
                #print tmp_paper
                if (len(tmp_paper)>1):
                    tmp_year_str = tmp_paper[-2]
                    if (tmp_year_str.isdigit()):
                        tmp_year = int(tmp_year_str)
                        if (tmp_year > 0):
                            joint_year.add(tmp_year)
            #print joint_year
            #for xx in joint_year:
            if (len(joint_year)>0):
                f_yr_graph.write(str(min(joint_year))+','+str(i)+','+str(j)+'\n')
                print min(joint_year), i, j
            else:
                f_yr_graph.write("-1"+','+str(i)+','+str(j)+'\n')
                print i, j
                pass
            #'''
                 
        f_yr_graph.close()
        f_graph.close()
 
 
    f_yr_graph.close()
    f_graph.close()
    print datetime.now()