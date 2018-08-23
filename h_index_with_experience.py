import numpy
from citation_library import *
from draw_hist import get_formatter, get_plt

f_h_age = open("process_data/gs_h_age.txt", "r") # h-index vs experience
f_g_age = open("process_data/gs_g_age.txt", "r") # g-index vs experience
f_t_age = open("process_data/gs_t_age.txt", "r") # total vs experience

all_h = f_h_age.read().split("\n"); all_h = all_h[:-1]
all_g = f_g_age.read().split("\n"); all_g = all_g[:-1]
all_t = f_t_age.read().split("\n"); all_t = all_t[:-1]

h_data = {}
g_data = {}
t_data = {}


def percentile(data, percent):
    lens = len(data)
    new_data = sorted(data)
    print("sorted")
    part = int(percent * lens / 100)
    return new_data[part]


# for x in all_h:
# 	y = x.split(" ")
# 	tmp_h = int(y[0]); yr = int(y[1])
# 	if (h_data.has_key(yr)):
# 		h_data[yr].append(tmp_h)
# 	else:
# 		h_data[yr] = [tmp_h]

# for x in all_g:
# 	y = x.split(" ")
# 	tmp_h = int(y[0]); yr = int(y[1])
# 	if (g_data.has_key(yr)):
# 		g_data[yr].append(tmp_h)
# 	else:
# 		g_data[yr] = [tmp_h]


for x in all_t:
	y = x.split(" ")
	tmp_h = int(y[0]); yr = int(y[1])
	if (t_data.has_key(yr)):
		t_data[yr].append(tmp_h)
	else:
		t_data[yr] = [tmp_h]



g_20_with_year = []
g_50_with_year = []
g_80_with_year = []

h_20_with_year = []
h_50_with_year = []
h_80_with_year = []

t_20_with_year = []
t_50_with_year = []
t_80_with_year = []

min_year = 1
max_year = 20


for year in range(min_year, max_year + 1):
    # g_20_with_year.append( percentile(g_data[year], 20))
    # g_50_with_year.append( percentile(g_data[year], 50))
    # g_80_with_year.append( percentile(g_data[year], 80))

    # h_20_with_year.append( percentile(h_data[year], 20))
    # h_50_with_year.append( percentile(h_data[year], 50))
    # h_80_with_year.append( percentile(h_data[year], 80))

    t_20_with_year.append( percentile(t_data[year], 20))
    t_50_with_year.append( percentile(t_data[year], 50))
    t_80_with_year.append( percentile(t_data[year], 80))


angchen = [1, 7, 18, 42, 39, 75, 45]
chunyipeng = [111, 113, 204, 189, 289, 300, 364, 460, 508, 442, 300]


def see_a_scholar(name, index_name, index_list):

	plt = get_plt()
	ax=plt.gca()
	ax.xaxis.set_major_formatter(get_formatter())
	ax.set_xlabel("Experience", fontsize=12)
	ax.set_ylabel(index_name, fontsize=12)
	plt.title("The Roadmap for " + name)
	lens = len(index_list)
	plt.plot(t_20_with_year[0: lens], color='green', label = 'Mediocre')
	plt.plot(t_50_with_year[0 : lens], color='blue', label = 'Normal')
	plt.plot(t_80_with_year[0 : lens], color='red', label = 'Excellent')
	plt.plot(index_list, color = 'yellow', label = 'Somebody')
	plt.legend(loc='best')
	plt.savefig("evaluate_" + name + ".png")
	plt.close()

if __name__ == '__main__':
	see_a_scholar("AngChen", "Citation", [1, 7, 18, 42, 39, 75, 45])
	see_a_scholar("Chunyi Peng", "Citation", [111, 113, 204, 189, 289, 300, 364, 460, 508, 442, 300])

