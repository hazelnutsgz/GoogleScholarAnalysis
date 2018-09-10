import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import ticker

formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
from draw_hist import get_formatter, get_plt



min_year = 1990
max_year = 2015
plt = get_plt()
ax = plt.gca()  
ax.xaxis.set_major_formatter(get_formatter()) 

per_giant_seq = [
    14.7590470995, 17.0125535772, 18.8043871658, 20.715776568, 22.7198961376, 24.9176962459,27.2299601225,29.6997912988,31.7616687932,33.9055676357,36.111577322,

38.3457603072,40.7688929189,42.9463527245,45.2461207304,47.2408491355,49.0194921712,

50.8925084942,52.6590846774,54.5725646123,56.6491759004 ,58.8662753927,61.2852909063,

64.1583839461,67.6425668712,68.9581524663

]

effective_diamater_seq = [

	13, 18, 13,11,10, 12,12,11,10,10,9,11,8,11,11,13, 8 ,8 ,7, 8, 8, 8,7,7,7,7

]

num_edge_seq= [

	30334,

	 33689,

	37864,

	42367,

	47977,

	54451,

	64855,

	74659,

	86316,

	100209,

	117226,

	137911,

	162428,

	191081,

	227058,

	271468,

	320222,

	375529,

	441508,

	521056,

	614629,

	720906,

	849540,

	999286,

	1179666,

	1233999

]

num_node_seq = [

	54990, 

	59027,

	63549,

	68513,

	73944,

	79887,

	86515,

	93435,

	 101103,

	109454,

	119164,

	129691,

141164,

154211,

169104,

185365 ,

203415,

222799,

244351,

267596,

291773,

316232,

339783,

360087,

374526,

375506

]

plt.figure()
plt.plot(range(min_year, max_year+1), per_giant_seq, '-o', color='black', markersize=2, linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Percenage (%)')
plt.ylim([0, 60])
plt.savefig('gscholar_evolution_giant.png')

plt.figure()
plt.loglog(num_node_seq, num_edge_seq, '-o', color='black', markersize=2, linewidth=0.5)
plt.xlabel('Number of Nodes')
plt.ylabel('Number of Edges')
plt.ylim([100, 1000000])
#    plt.title('Probability Density Function')
plt.savefig('gscholar_evolution_density.png')

plt.figure()
plt.plot(range(min_year, max_year+1), effective_diamater_seq, '-o', color='black', markersize=2, linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Effective Diameter')
plt.savefig('scholar_evolution_effective_diameter.png')

plt.figure()
plt.plot(range(min_year, max_year+1), sorted(effective_diamater_seq, reverse=True), '-o', color='black', markersize=2, linewidth=0.5)
plt.xlabel('Year')
plt.ylabel('Effective Diameter')
plt.ylim([0, 20])
plt.savefig('scholar_evolution_effective_diameter2.png')