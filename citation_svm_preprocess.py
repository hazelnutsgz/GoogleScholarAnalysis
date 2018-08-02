# prepare data for SVM
# get the collaboration graph (weighted)
# get total citation, h-index, g-index, of every author

import os
import numpy
from citation_library import *
import pdb
filename=os.listdir('gs_result/')

total= 0

all_name = [];

all_total_citation = []; all_h_index = []; all_i10_index = []; all_g_index = []; all_inst = [];
cs_total_citation = []; cs_h_index = []; cs_i10_index = []; cs_g_index = []; cs_inst = [];
neuro_total_citation = []; neuro_h_index = []; neuro_i10_index = []; neuro_g_index = []; neuro_inst = [];

all_job_title = [];

data = {}

faculty_count = 0
student_postdoc_count = 0

f_svm_informetrics = open("gs_svm_informetrics.txt", "w")
f_svm_name = open("gs_svm_name.txt", "w")
f_svm_simple = open("gs_svm_simple.txt", "w") # simple SVM input without considering centrality
f_svm_simple_rank = open("gs_svm_simple_rank.txt", "w") # simple rank-based SVM input without considering centrality

#f_title = open("gs_title.txt", "w")
#f_h_idx = open("gs_h_idx.txt", "w")
#f_g_idx = open("gs_g_idx.txt", "w")
#f_t_idx = open("gs_t_idx.txt", "w")

sum_aau = 0
sum_non_aau = 0

all_aau_stat = []

for x in filename:
	if x[-6:]=='.parse':
		#print x,
		x_name = os.path.join('gs_result/', x);
		lines=open(x_name, "r").read().split('\n')
		#close(x)
		#print 'uid', lines[0], 'name', lines[1], 'index', lines[7],
		# get idx ['413', '364', '10', '9', '11', '9']
        # check if it's a verified account
		affilation_str = lines[2].lower()
		keyword_str = lines[3].lower()
		verified_str = lines[4].lower()

		if (verified_str[0] == 'n'): # skip unverified account
			continue
		if (verified_str[-4:] != '.edu'): # skip unverified account
			continue
		aau_stat = getaau(verified_str)
		if (aau_stat>= 0):
			sum_aau += 1
			all_aau_stat.append(1)
		else:
			sum_non_aau+=1
			all_aau_stat.append(0)
    #check title from lines[2]
		if (affilation_str.find("prof") >= 0 and affilation_str.find("research associate prof") < 0 and affilation_str.find("research assistant prof") < 0):
			job_title=1
			faculty_count+=1
		elif (affilation_str.find("postdoc") >= 0 or affilation_str.find("scientist") >= 0 or affilation_str.find("research associate") >= 0):
			job_title=0
			student_postdoc_count+=1
		elif (affilation_str.find("student") >= 0 or affilation_str.find("candidate") >= 0  or affilation_str.find("research assistant") >= 0):
			job_title=0
			student_postdoc_count+=1
		else:
			continue; # filter out accounts not from academia
        

		xy= eval(lines[7])
		g_index = getGIndex(eval(lines[11]))
		uni_code = getuni(verified_str)
		total_citation = int(xy[0]); h_index = int(xy[2]); i10_index = int(xy[4])
        			
		all_total_citation.append(total_citation); all_h_index.append(h_index); all_i10_index.append(i10_index); all_g_index.append(g_index); all_inst.append(uni_code)
		all_name.append(lines[1])
        
		all_job_title.append(job_title)
		
        #if cnt >= 13:
		#			paper = eval(strs)
		paperlist=[]
		if (len(lines) >= 14):
			for cnt in range(13, len(lines)):
				if (len(lines[cnt])==0):
					break
				#print lines[cnt], len(lines[cnt]),
				#try:
				paper = lines[cnt].strip("'")[1:-1].split(", ")
				paperlen = len(paper)
				pp = ''
				
				# paper[2] : 'CR Lin, M Gerla'
				# = number of authors
				#author_list = paper[2]
				
				#pp = str(author_num) + '$$'
				
				#for p in range(1,paperlen):
				#	pp = pp + paper[p] + '$$'
				#	if (p == 2):
				#		author_num = len(paper[p].split(','))				
				#print paper
				#print paper[1]+'$$'+paper[paperlen-1]
            # title + year (some papers does not have year info)
				#try:
				if (paperlen > 1):
					paperlist.append(paper[1]+'$$'+paper[paperlen-1])
				#except:
				#	print lines
					#print paper
					#print paperlen
					#break
				
#				s=eval(lines[cnt]);
				#except:					
				#	s=['bad']
				#	pass
#				print lines[cnt], s[0]

		#print total, lines[1], total_citation, h_index, g_index, len(paperlist)
		f_svm_name.write(lines[1]+'\n')
		f_svm_informetrics.write(lines[1]+'$$'+str(total)+' '+str(total_citation)+' '+str(h_index)+' '+str(g_index)+' '+str(aau_stat)+' '+str(job_title)+'\n')
		f_svm_simple.write(str(job_title)+' 1:'+str(total_citation)+' 2:'+str(h_index)+' 3:'+str(g_index))
		if (aau_stat >= 0):
			#f_svm_informetrics.write(' 4:1 5:0\n')
			f_svm_simple.write(' 4:1 5:0\n')
		else:
			#f_svm_informetrics.write(' 4:0 5:1\n')
			f_svm_simple.write(' 4:0 5:1\n')
		data[total] = paperlist
			
		total=total+1

f_svm_informetrics.close()
f_svm_name.close()
f_svm_simple.close()

print (len(data))

print ('faculty:', faculty_count)
print ('student/postdoc:', student_postdoc_count)

print ('AAU', sum_aau)
print ('Non AAU', sum_non_aau)
print ('####')

# get rank here...
# all_total_citation / all_h_index / all_g_index ...

#get topper

whole_sorted_t = sorted(all_total_citation)
whole_sorted_h = sorted(all_h_index)
whole_sorted_g = sorted(all_g_index)
#def gettopper(whole_sorted_set, index_value):
	#for i in range(0, len(whole_sorted_set)):
	#	if (whole_sorted_set[i] >= index_value):
	#		return 100.0*i/len(whole_sorted_set)

for i in range(0, len(all_total_citation)):
	t_topper = gettopper(whole_sorted_t, all_total_citation[i])
	h_topper = gettopper(whole_sorted_h, all_h_index[i])
	g_topper = gettopper(whole_sorted_g, all_g_index[i])
	#print t_topper, h_topper, g_topper
	f_svm_simple_rank.write(str(all_job_title[i])+' 1:'+str(t_topper)+' 2:'+str(h_topper)+' 3:'+str(g_topper)+'\n')
	

compute_collaboration_graph = 1

if (compute_collaboration_graph == 1):

	#f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "w")
	f_svm_graph = open("gs_svm_collaboration_graph.txt", "w")

	f_svm_graph.close()

	for i in range(0, total):
		#f_weighted_graph = open("gs_weighted_collaboration_graph.txt", "a")
		f_svm_graph = open("gs_svm_collaboration_graph.txt", "a")
		for j in range(i+1, total):
			# compare data[i], data[j]
			joint_papers = set(data[i]) & set(data[j])
			if (len(joint_papers)>0):
				f_svm_graph.write(str(i)+' '+str(j)+'\n')
				
		f_svm_graph.close()


	f_svm_graph.close()
