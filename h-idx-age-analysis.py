import numpy
from citation_library import *

def add_to_dict(target_dict, key):
	if (key in target_dict):
		target_dict[key] = target_dict[key] + 1
	else:
		target_dict[key] = 1

f_h_age = open("gs_h_age.txt", "r") # h-index vs experience

lines=f_h_age.read().split('\n')

all_h_age = []
all_possible_age = {}

for x in lines:
	y = x.split(" ")
	if (len(y) == 2):
		print (y),
		tmp_h = int(y[0])
		tmp_age = int(y[1])
		print (tmp_h, tmp_age)
		all_h_age.append((tmp_h, tmp_age))
		add_to_dict(all_possible_age, tmp_age)

print (all_possible_age)

result_yr_seq = []
result_20_seq = []
result_50_seq = []
result_80_seq = []

for x in all_possible_age:
	current_yr_seq = []
	for j in range(0, len(all_h_age)):
		if (all_h_age[j][1] == x):
			current_yr_seq.append(all_h_age[j][0])
	current_yr_seq.sort()
	result_yr_seq.append(x)
	result_20_seq.append(get_percentile_value(current_yr_seq, 20))
	result_50_seq.append(numpy.median(current_yr_seq))
	result_80_seq.append(get_percentile_value(current_yr_seq, 80))
	print (x, get_percentile_value(current_yr_seq, 20), numpy.median(current_yr_seq), get_percentile_value(current_yr_seq, 80) )

print ('output for matlab')
print ('year =', result_yr_seq)
print ('result_20 =', result_20_seq)
print ('result_50 =', result_50_seq)
print ('result_80 =', result_80_seq)
