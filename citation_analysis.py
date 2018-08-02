import os
import numpy
from citation_library import univ_email


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
	print '(5th)', percentile(sorted_data, 5), '(25th)', percentile(sorted_data, 25), '(50th)', percentile(sorted_data, 50), '(75th)', percentile(sorted_data, 75), '(95th)', percentile(sorted_data, 95), 'Avg', numpy.average(sorted_data)
	

def savefile(filename, dataset):
	FP = open(filename, "w");
	for x in dataset:
		FP.write(str(x)+" ")
	FP.close();
INPUT_DIR = './gs_result'
OUTPUT_DIR = ''

filename=os.listdir(INPUT_DIR)

total= 0


all_total_citation = []; all_h_index = []; all_i10_index = []; all_g_index = []; all_inst = [];
cs_total_citation = []; cs_h_index = []; cs_i10_index = []; cs_g_index = []; cs_inst = [];
neuro_total_citation = []; neuro_h_index = []; neuro_i10_index = []; neuro_g_index = []; neuro_inst = [];


for x in filename:
	if x[-6:]=='.parse':
		#print x,
		lines=open(os.path.join(INPUT_DIR, x), "r").read().split('\n')
		#close(x)
		#print 'uid', lines[0], 'name', lines[1], 'index', lines[7],
		# get idx ['413', '364', '10', '9', '11', '9']
        # check if it's a verified account
		affilation_str = lines[2].lower()
		keyword_str = lines[3].lower()
		verified_str = lines[4].lower()
		if (verified_str[0] == 'N'):
			continue
		xy= eval(lines[7])
		gindex = getGIndex(eval(lines[11]))
		uni_code = getuni(verified_str)
		total_citation = int(xy[0]); h_index = int(xy[2]); i10_index = int(xy[4])
		all_total_citation.append(total_citation); all_h_index.append(h_index); all_i10_index.append(i10_index); all_g_index.append(gindex); all_inst.append(uni_code)
		if (verified_str.find("cs.") >= 0 or verified_str.find("informatik.") >= 0 or keyword_str.find("computer") >= 0 or keyword_str.find("informat") >= 0 or affilation_str.find("computer") >= 0):
#		if (keyword_str.find("network") >= 0):
			# computer science author
			cs_total_citation.append(total_citation); cs_h_index.append(h_index); cs_i10_index.append(i10_index); cs_g_index.append(gindex); cs_inst.append(uni_code)

#		if (keyword_str.find("psychiatry") >= 0 or keyword_str.find("neuro") >= 0):
		if (verified_str.find("neuro.") >= 0 or keyword_str.find("bio") >= 0 or keyword_str.find("psychiatry") >= 0 or keyword_str.find("neuro") >= 0 or affilation_str.find("bio") >= 0):
			# neuroscience author
			neuro_total_citation.append(total_citation); neuro_h_index.append(h_index); neuro_i10_index.append(i10_index); neuro_g_index.append(gindex); neuro_inst.append(uni_code)

			
		total=total+1
		print(total)


		
rank_t = getrank(all_total_citation); rank_h = getrank(all_h_index); rank_i10 = getrank(all_i10_index); rank_g = getrank(all_g_index);

sorted_t = sorted(all_total_citation);
sorted_h = sorted(all_h_index); 
sorted_g = sorted(all_g_index);

savefile('result_sorted_total_citation.txt', sorted_t);
savefile('result_sorted_h_index.txt', sorted_h);
savefile('result_sorted_g_index.txt', sorted_g);


total_delta = []

uni_num_authors = numpy.zeros(len(univ_email))
uni_h_citation_authors = []
uni_g_citation_authors = []


for i in range(0, len(uni_num_authors)):
    uni_h_citation_authors.append([])
    uni_g_citation_authors.append([])

for i in range(0, total):
    if (all_inst[i] < 0):
        continue
    #    per_t = gettopper(sorted_t, all_total_citation[i]); per_h = gettopper(sorted_h, all_h_index[i]); per_g = gettopper(sorted_g, all_g_index[i]);
    per_t = binary_search(sorted_t, all_total_citation[i]); per_h = binary_search(sorted_h, all_h_index[i]); per_g = binary_search(sorted_g, all_g_index[i]);
    print all_total_citation[i], '(', per_t, ')',
    print all_h_index[i], '(', per_h, ')',
    print all_g_index[i], '(', per_g, ')',
    delta = max(per_t, per_g, per_h) - min(per_t, per_g, per_h)
    print '|', delta
    print '<', all_inst[i], '>'
    uni_h_citation_authors[all_inst[i]].append(all_h_index[i])
    uni_g_citation_authors[all_inst[i]].append(all_g_index[i])
    uni_num_authors[all_inst[i]]=uni_num_authors[all_inst[i]]+1
    total_delta.append(delta)
	
print 'Number of authors=', total
print 'Average (t/h/i10/g): ', numpy.average(all_total_citation), numpy.average(all_h_index), numpy.average(all_i10_index), numpy.average(all_g_index)
print 'STD (t/h/i10/g): ', numpy.std(all_total_citation), numpy.std(all_h_index), numpy.std(all_i10_index), numpy.std(all_g_index)
print 'Median (t/h/i10/g): ', numpy.median(all_total_citation), numpy.median(all_h_index), numpy.median(all_i10_index), numpy.median(all_g_index)

print 'total:',; showpercentile(all_total_citation)
print 'h-index:',; showpercentile(all_h_index)
print 'i10-index:',; showpercentile(all_i10_index)
print 'g-index:',; showpercentile(all_g_index)
print 'delta:',; showpercentile(total_delta);

sorted_delta = sorted(total_delta);
savefile('result_sorted_delta.txt', sorted_delta);

#print uni_citation_authors
# uni , # of authors, uni-h, uni-g
for i in range(0,len(uni_num_authors)):
    print '%30s' % univ_email[i], uni_num_authors[i], uni_h_idx(uni_h_citation_authors[i]), uni_g_idx(uni_g_citation_authors[i])

print 'Number of CS authors =', len(cs_total_citation)
print 'CS total:',; showpercentile(cs_total_citation)
print 'CS h-index:',; showpercentile(cs_h_index)
print 'CS i10-index:',; showpercentile(cs_i10_index)
print 'CS g-index:',; showpercentile(cs_g_index)

print 'Number of Neuro authors =', len(neuro_total_citation)
print 'Neuro total:',; showpercentile(neuro_total_citation)
print 'Neuro h-index:',; showpercentile(neuro_h_index)
print 'Neuro i10-index:',; showpercentile(neuro_i10_index)
print 'Neuro g-index:',; showpercentile(neuro_g_index)
