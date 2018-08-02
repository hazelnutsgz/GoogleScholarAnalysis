import numpy
from datetime import datetime
#from scipy.stats import spearmanr


univ_email = ['stanford.edu', 'mit.edu', 'ethz.ch', 'ox.ac.uk', 'epfl.ch', 'cam.ac.uk', 'duke.edu', 'unc.edu', 'princeton.edu', 
'yale.edu', 'cornell.edu', 'berkeley.edu', 'columbia.edu', 'ucsd.edu', 'ucla.edu', 'uci.edu', 'ucsb.edu', 'nyu.edu', 'harvard.edu', 
'clemson.edu', 'ncsu.edu', 'tsinghua.edu.cn', 'caltech.edu', 'pku.edu.cn', 'uni-goettingen.de', 'imperial.ac.uk', 'uchicago.edu', 
'uni-heidelberg.de', 'nus.edu.sg', 'anu.edu.au', 'cmu.edu', 'upenn.edu', 'jhu.edu', 'ucl.ac.uk', 'washington.edu', 'wustl.edu', 
'tudelft.nl', 'u-tokyo.ac.jp', 'umich.edu', 'utoronto.ca', 'northwestern.edu', 'uiuc.edu', 'ku.dk', 'umd.edu', 'ki.se', 'manchester.ac.uk', 
'ucdavis.edu', 'colorado.edu', 'usc.edu', 'ed.ac.uk', 'mcgill.ca', 'brown.edu',
'ust.hk', 'hku.hk', 'cuhk.edu.hk',
'liv.ac.uk', 'aalto.fi', 'helsinki.fi', 'qmul.ac.uk', 'aston.ac.uk', 'bbk.ac.uk', 'coventry.ac.uk', 'city.ac.uk', 'uni-paderborn.de', 
'uni-marburg.de', 'drexel.edu', 'dcu.ie', 'uoregon.edu',
              'vu.nl', 'exeter.ac.uk', 'reading.ac.uk', 'gre.ac.uk']

aau_email = ['bu.edu',
             'brandeis.edu',
             'brown.edu',
             'caltech.edu',
             'cmu.edu',
             'case.edu',
             'columbia.edu',
             'cornell.edu',
             'duke.edu',
             'emory.edu',
             'gatech.edu',
             'harvard.edu',
             'indiana.edu',
             'iastate.edu',
             'jhu.edu',
             'mit.edu',
             'mcgill.ca',
             'msu.edu',
             'nyu.edu',
             'northwestern.edu',
             'osu.edu',
             'psu.edu',
             'princeton.edu',
             'purdue.edu',
             'rice.edu',
             'rutgers.edu',
             'stanford.edu',
             'stonybrook.edu',
             'tamu.edu',
             'tulane.edu',
             'arizona.edu',
             'buffalo.edu',
             'berkeley.edu',
             'ucdavis.edu',
             'uci.edu',
             'ucla.edu',
             'ucsd.edu',
             'ucsb.edu',
             'uchicago.edu',
             'colorado.edu',
             'ufl.edu',
             'illinois.edu',
             'uiuc.edu',
             'uiowa.edu',
             'ku.edu',
             'umd.edu',
             'umich.edu',
             'umn.edu',
             'missouri.edu',
             'unc.edu',
             'uoregon.edu',
             'upenn.edu',
             'pitt.edu',
             'rochester.edu',
             'usc.edu',
             'utexas.edu',
             'toronto.edu',
             'virginia.edu',
             'washington.edu',
             'uw.edu',
             'wisc.edu',
             'vanderbilt.edu',
             'wustl.edu',
             'yale.edu']


cs_keywords = ['distributed systems', 'mobile', 'wireless', 'operating systems', 'robotics', 'programming', 'algorithms', 'artificial intelligence', 'comput', 'cryptography', 'databases', 'data mining', 'information', 'machine learning', 'network', 'software engineering', 'web']
bio_keywords = ['bio', 'neuro', 'medic', 'life sci', 'genetic', 'epidemiology', 'molecular', 'genomics', 'brain', 'clinical', 'psychiatry', 'pediatrics']
physics_keywords = ['physics']


def has_cs_keyword(input_keyword_str):
	for x in cs_keywords:
		if (x in input_keyword_str):
			return 1
	return 0

def has_bio_keyword(input_keyword_str):
	for x in bio_keywords:
		if (x in input_keyword_str):
			return 1
	return 0

def has_physics_keyword(input_keyword_str):
	for x in physics_keywords:
		if (x in input_keyword_str):
			return 1
	return 0



def getaau(emailstr):
	for i in range(0, len(aau_email)):
		if (emailstr.find(aau_email[i])>0):
			return i
	return -1

def getuni(emailstr):
	for i in range(0, len(univ_email)):
		if (emailstr.find(univ_email[i])>0):
			return i
	return -1

def uni_h_idx(input_set):
	input_set.sort(reverse=True)
	result = 0
	for i in range(0, len(input_set)):
		if (input_set[i]>=i+1):
			result = i+1
		else:
			break
	return result
	
def uni_g_idx(input_set):
	input_set.sort(reverse=True)
	return getGIndex(input_set)

def percentile(input_seq, per):
	N = len(input_seq)
	return input_seq[int(N * per / 100)]

def getrank(whole_set):
	# input: [3,4,100,1,2,6]
	# output: b=[2,3,5,0,1,4]
	array = numpy.array(whole_set)
	temp = array.argsort()
	ranks = numpy.empty(len(array), int)
	ranks[temp] = numpy.arange(len(array))
	return ranks

def binary_search(a, x, lo=0, hi=None):
	if hi is None:
		hi = len(a)
	while lo < hi:
		mid = (lo+hi)//2
		midval = a[mid]
		if midval < x:
			lo = mid+1
		elif midval > x:
 			hi = mid
		else:
			return 100.0*mid/len(a)
	return -1

def gettopper(whole_sorted_set, index_value):
	for i in range(0, len(whole_sorted_set)):
		if (whole_sorted_set[i] >= index_value):
			return 100.0*i/len(whole_sorted_set)
			
def get_highest_ranked_value(whole_sorted_set, top_num):
	return whole_sorted_set[len(whole_sorted_set) - top_num]
	#pass

def get_percentile_value(whole_sorted_set, percentile): # eg: percentile = 80
	return whole_sorted_set[int(len(whole_sorted_set)*percentile/100)-1]

def analysis_centrality_result(whole_centrality_set, whole_name_set, whole_h_index_set, whole_g_index_set):
	all_centrality = []
	all_g = []
	for x in whole_centrality_set:
		all_centrality.append(whole_centrality_set[x])	
		all_g.append(whole_g_index_set[x])
	
	showpercentile(all_centrality)
	

	#threshold_centrality = get_highest_ranked_value(sorted(all_centrality), 20) # get top 10
	top_h_set = []; top_g_set = []
	
	working_set = whole_centrality_set;
	for ii in range(0, int(len(whole_centrality_set)/10)):
		current_max_centrality = 0; max_id = 0;
		for x in working_set:
			if (working_set[x] >= current_max_centrality):
				current_max_centrality = working_set[x];
				max_id = x;
		
		if (ii < 20):				
			print (max_id, whole_name_set[max_id], current_max_centrality, whole_h_index_set[max_id], whole_g_index_set[max_id])
		top_h_set.append(whole_h_index_set[max_id])
		top_g_set.append(whole_g_index_set[max_id])
		#print ii, max_id
		
		del(working_set[max_id])
				
	print ('(Top20) Avg h-index :%.2f,' % numpy.average(top_h_set[0:20])),
	print ('Avg g-index :%.2f' % numpy.average(top_g_set[0:20]))
	#print spearmanr(all_centrality,all_g)
	print ('(Top 10 per) Avg h-index :%.2f,' % numpy.average(top_h_set),)
	print ('Avg g-index :%.2f' % numpy.average(top_g_set))
	
	#sorted_all_centrality = sorted(all_centrality)
	#for ii in range(100, 0, -5):
	#for ii in range(100, 90, -1):
		#upper_bound = get_percentile_value(sorted_all_centrality, ii)
		#lower_bound = get_percentile_value(sorted_all_centrality, ii-1)
		#tmp_g_set = []
		#for x in whole_centrality_set:
			#if (whole_centrality_set[x] >= lower_bound and whole_centrality_set[x] <= upper_bound):
				#tmp_g_set.append(whole_g_index_set[x])
		#print '%.2f ' % numpy.average(tmp_g_set),
	
	print	
	print ("--> ", datetime.now())

def getGIndex(cite):
	gindex = 0
	citation = 0
	cnt = 0
	while 1:
		if cnt < len(cite):
			citation = citation + int(cite[cnt])
		cnt = cnt + 1
		if cnt*cnt <= citation:
			gindex = cnt
		else:
		 	break
	return gindex
	
def showpercentile(all_data):
	sorted_data = sorted(all_data)
	print ('(5th)', percentile(sorted_data, 5), '(25th)', percentile(sorted_data, 25), '(50th)', percentile(sorted_data, 50), '(75th)', percentile(sorted_data, 75), '(95th)', percentile(sorted_data, 95), 'Avg', numpy.average(sorted_data))
	

def savefile(filename, dataset):
	FP = open(filename, "w");
	for x in dataset:
		FP.write(str(x)+" ")
	FP.close();
