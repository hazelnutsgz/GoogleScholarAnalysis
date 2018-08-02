# -*- coding: utf-8 -*-
# get the collaboration graph (weighted)
# get total citation, h-index, g-index, of every author

import os
import numpy
from citation_library import *



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

min_year = 1990
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

f_profile = open("gs_profile.txt", "w")
f_name = open("gs_name.txt", "w")


f_h_age = open("gs_h_age.txt", "w") # h-index vs experience
f_g_age = open("gs_g_age.txt", "w") # g-index vs experience
f_t_age = open("gs_t_age.txt", "w") # total vs experience



f_title = open("gs_title.txt", "w") # academic title
f_h_idx = open("gs_h_idx.txt", "w")
f_g_idx = open("gs_g_idx.txt", "w")
f_t_idx = open("gs_t_idx.txt", "w")
#f_subject = open("gs_subject.txt", "w")

country_list = []

for x in filename:
	if x[-6:]=='.parse':
		print x,
		x_name = os.path.join('gs_result/', x);
		lines=open(x_name, "r").read().split('\n')
		#close(x)
		#print 'uid', lines[0], 'name', lines[1], 'index', lines[7],
		# get idx ['413', '364', '10', '9', '11', '9']
        # check if it's a verified account
		affilation_str = lines[2].lower()
		keyword_str = lines[3].lower()
		verified_str = lines[4].lower()
#		if (verified_str[0] == 'n'):
#			continue
#		if (verified_str[-8:] != 'duke.edu'):
#		if (verified_str[-4:] != '.edu'):
#			continue
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
		
		
        #if cnt >= 13:
		#			paper = eval(strs)
		paperlist=[]
		if (len(lines) >= 14):
			earliest_yr = 2015
			for cnt in range(13, len(lines)):
				if (len(lines[cnt])==0):
					break
				#print lines[cnt], len(lines[cnt]),
				try:
					paper = eval(lines[cnt])
				except:
					pass

				paperlen = len(paper)
				pp = ''
				
				# paper[2] : 'CR Lin, M Gerla'
				# = number of authors
				#author_list = paper[2]
				
				#pp = str(author_num) + '$$'
				
				for p in range(1,paperlen):
					pp = pp + paper[p] + '$$'
					if (p == 2):
						author_num = len(paper[p].split(','))				
					
				pub_year = paper[paperlen-1]
				if (pub_year.isdigit() == True):
					num_yr = int(pub_year)
					if (num_yr >= min_year and num_yr <= max_year):
						if (num_yr<earliest_yr):
							earliest_yr = num_yr					
				'''
				if (pub_year.isdigit() == True):
					num_yr = int(pub_year)
					if (num_yr >= min_year and num_yr <= max_year):
						if (num_yr<earliest_yr):
							earliest_yr = num_yr
					
						year_user.add((num_yr, total))
						paperlist.append(str(author_num)+'|'+str(pub_year)+'|'+pp)
					else:
						paperlist.append(str(author_num)+'|'+str(-1)+'|'+pp)
				else:
					paperlist.append(str(author_num)+'|'+str(-1)+'|'+pp)
				'''
				paperlist.append(pp)

		#print total, lines[1], total_citation, h_index, g_index, len(paperlist)
		#print earliest_yr, h_index
		if (earliest_yr < 2015):
			f_h_age.write(str(h_index)+' '+str(2015-earliest_yr)+'\n') # h-index, and years since the 1st paper
			f_g_age.write(str(g_index)+' '+str(2015-earliest_yr)+'\n') # g-index, and years since the 1st paper
			f_t_age.write(str(total_citation)+' '+str(2015-earliest_yr)+'\n') # total_citation, and years since the 1st paper
		

		
		#check title from lines[2]
		if (affilation_str.find("postdoc") >= 0 or affilation_str.find("research associate")>= 0):
			f_title.write("2\n");
		elif (affilation_str.find("student") >= 0 or affilation_str.find("research assistant")>= 0):
			f_title.write("1\n");
		elif (affilation_str.find("prof") >= 0 or affilation_str.find("lecturer") >= 0):
			f_title.write('3\n');
		else:
			f_title.write('0\n');
		
		paper_data[total] = paperlist
		
		#print		
		
		if (verified_str.find("cs.") >= 0 or verified_str.find("informatik.") >= 0 or has_cs_keyword(keyword_str)==1 or affilation_str.find("computer") >= 0):
#		if (keyword_str.find("network") >= 0 or keyword_str.find("system") >= 0 or keyword_str.find("cloud") >= 0 or keyword_str.find("distributed") >= 0) and (verified_str.find("cs.") >= 0 or verified_str.find("informatik.") >= 0 or keyword_str.find("computer") >= 0 or keyword_str.find("informat") >= 0 or affilation_str.find("computer") >= 0):
#		if (keyword_str.find("network") >= 0 or keyword_str.find("distributed systems")>= 0):
#		if (keyword_str.find("information retrieval") >= 0 or keyword_str.find("data mining") >= 0 or keyword_str.find("machine learning") >= 0):		

			# computer science author
			cs_total_citation.append(total_citation); cs_h_index.append(h_index); cs_i10_index.append(i10_index); cs_g_index.append(g_index); cs_inst.append(uni_code)
			f_profile.write('1 ')
				
		else:
			f_profile.write('0 ')

#		if (keyword_str.find("psychiatry") >= 0 or keyword_str.find("neuro") >= 0):
		if (verified_str.find("neuro.") >= 0 or verified_str.find("med.") >= 0 or has_bio_keyword(keyword_str) == 1 or affilation_str.find("bio") >= 0):
			# neuroscience author
			neuro_total_citation.append(total_citation); neuro_h_index.append(h_index); neuro_i10_index.append(i10_index); neuro_g_index.append(g_index); neuro_inst.append(uni_code)
			f_profile.write('1 ')
		else:
			f_profile.write('0 ')

		if (verified_str.find("soc.") >= 0 or verified_str.find("sociology.") >= 0 or affilation_str.find("sociology") >= 0):
			f_profile.write('1\n')
		else:
			f_profile.write('0\n')

			
		total=total+1

f_profile.close()
f_name.close()
f_h_age.close()
#f_subject.close()

print len(paper_data), 'users'

print '####'

#year_summary(year_user)

compute_collaboration_graph = 0

if (compute_collaboration_graph == 1):

	f_node_list = open("gs_graph_nodes.txt", "w")
	f_country_node_list = open("gs_country_graph_nodes.txt", "w")
	#f_yr_node_list = open("gs_graph_yr_nodes.txt", "w")

	for i in range(0, total):
		f_node_list.write(str(i)+"\n")
		f_country_node_list.write(str(country_list[i])+" "+str(i)+"\n")
	#for x in year_user:
	#	f_yr_node_list.write(str(x[0])+" "+str(x[1])+"\n")
	f_node_list.close()
	f_country_node_list.close()
	#f_yr_node_list.close()
	
	#f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "w")
	f_graph = open("gs_collaboration_graph.txt", "w")
	f_yr_graph = open("gs_collaboration_yearly_graph.txt", "w")

	#f_yr_graph.close()
	f_graph.close()

	for i in range(0, total):
		#f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "a")
		#f_yr_graph = open("gs_collaboration_yearly_graph.txt", "a")
		f_graph = open("gs_collaboration_graph.txt", "a")
		if ((i % 1000) == 0):
			print i,
		for j in range(i+1, total):
			# compare data[i], data[j]
			joint_papers = set(paper_data[i]) & set(paper_data[j])
			if (len(joint_papers) == 0):
				continue
			
			f_graph.write(str(i)+','+str(j)+'\n')
			'''
			joint_year = set()
			for xxx in joint_papers:				 
				tmp_paper=xxx.split('|')
				#print tmp_paper
				tmp_num_author = int(tmp_paper[0])
				tmp_year = int(tmp_paper[1])
				if (tmp_year > 0):
					joint_year.add(tmp_year)
			
			
			#print joint_year
			for xx in joint_year:
				f_yr_graph.write(str(xx)+','+str(i)+','+str(j)+'\n')
			'''
				
		#f_yr_graph.close()
		f_graph.close()


	f_yr_graph.close()
	f_graph.close()
