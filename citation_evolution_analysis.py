import numpy
from citation_library import *

f_h_age = open("process_data/gs_h_age.txt", "r") # h-index vs experience
f_g_age = open("process_data/gs_g_age.txt", "r") # g-index vs experience
f_t_age = open("process_data/gs_t_age.txt", "r") # total vs experience

all_h = f_h_age.read().split("\n"); all_h = all_h[:-1]
all_g = f_g_age.read().split("\n"); all_g = all_g[:-1]
all_t = f_t_age.read().split("\n"); all_t = all_t[:-1]

h_data = {}

for x in all_h:
	y = x.split(" ")
	tmp_h = int(y[0]); yr = int(y[1])
	if (h_data.has_key(yr)):
		h_data[yr].append(tmp_h)
	else:
		h_data[yr] = [tmp_h]

h_20_seq = []; h_50_seq= []; h_80_seq = [];
g_20_seq = []; g_50_seq= []; g_80_seq = [];
t_20_seq = []; t_50_seq= []; t_80_seq = [];

f_h_result = open("result_h_evolution.txt", "w")


##Accumulate zero to twenty years
for i in range(1, 20):
	h_20_seq.append(percentile(sorted(h_data[i]), 20)); f_h_result.write(str(percentile(sorted(h_data[i]), 20))+" ")
	h_50_seq.append(percentile(sorted(h_data[i]), 50)); f_h_result.write(str(percentile(sorted(h_data[i]), 50))+" ")
	h_80_seq.append(percentile(sorted(h_data[i]), 80)); f_h_result.write(str(percentile(sorted(h_data[i]), 80))+"\n")

f_h_result.close()

print h_20_seq
print h_50_seq
print h_80_seq
numpy.savetxt('result_h_idx_evolution_20.txt', h_20_seq)
numpy.savetxt('result_h_idx_evolution_50.txt', h_50_seq)
numpy.savetxt('result_h_idx_evolution_80.txt', h_80_seq)
print


g_data = {}
for x in all_g:
	y = x.split(" ")
	tmp_g = int(y[0]); yr = int(y[1])
	if (g_data.has_key(yr)):
		g_data[yr].append(tmp_g)
	else:
		g_data[yr] = [tmp_g]
	
f_g_result = open("result_g_evolution.txt", "w")

for i in range(1, 20):
	g_20_seq.append(percentile(sorted(g_data[i]), 20)); f_g_result.write(str(percentile(sorted(g_data[i]), 20))+" ")
	g_50_seq.append(percentile(sorted(g_data[i]), 50)); f_g_result.write(str(percentile(sorted(g_data[i]), 50))+" ")
	g_80_seq.append(percentile(sorted(g_data[i]), 80)); f_g_result.write(str(percentile(sorted(g_data[i]), 80))+"\n")

f_g_result.close()

print g_20_seq
print g_50_seq
print g_80_seq
print
numpy.savetxt('result_g_idx_evolution_20.txt', g_20_seq)
numpy.savetxt('result_g_idx_evolution_50.txt', g_50_seq)
numpy.savetxt('result_g_idx_evolution_80.txt', g_80_seq)

t_data = {}

for x in all_t:
	y = x.split(" ")
	tmp_t = int(y[0]); yr = int(y[1])
	if (t_data.has_key(yr)):
		t_data[yr].append(tmp_t)
	else:
		t_data[yr] = [tmp_t]
		
for i in range(1, 20):
	t_20_seq.append(percentile(sorted(t_data[i]), 20));
	t_50_seq.append(percentile(sorted(t_data[i]), 50));
	t_80_seq.append(percentile(sorted(t_data[i]), 80));

print t_20_seq
print t_50_seq
print t_80_seq
print
numpy.savetxt('result_t_idx_evolution_20.txt', t_20_seq)
numpy.savetxt('result_t_idx_evolution_50.txt', t_50_seq)
numpy.savetxt('result_t_idx_evolution_80.txt', t_80_seq)
