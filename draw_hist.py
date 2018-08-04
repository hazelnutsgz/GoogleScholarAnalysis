import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import statsmodels.api as sm
import sys
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
  

# def cdf_plot(data, name, number):
#     ecdf = sm.distributions.ECDF(data)
#     print(ecdf)
#     x = np.linspace(min(data), max(data), number)
#     y = ecdf(x)

#     #plt.step(x, y, label=name)
#     plt.plot(x, y, label=name)
#     plt.savefig("test.png")

def cdf_plot(data, color, name, xlabel, ylabel, number_of_bins):
    data = sorted(data)
    x = np.linspace(min(data), max(data), number_of_bins)
    y = [0]
    current_item_count = 0
    current_index = 0
    for item in data:
        if current_index + 1 >= number_of_bins:
            break
        current_item_count += 1
        if item >= x[current_index] and item < x[current_index+1]:
            continue
        else:
            while current_index < number_of_bins and item > x[current_index]:
                y.append(float(current_item_count)/len(data))
                current_index += 1
    print(float(current_item_count)/len(data))
    print(x)
    print(y)
    
    ax=plt.gca()
    ax.xaxis.set_major_formatter(formatter) 
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    plt.plot(x[0:len(y)], y, color="black", linewidth=1.2)
    plt.show()

if __name__ == '__main__':
    f = open("all_pagerank.txt", 'r')
    v = map(lambda x: float(x.strip()), f)
    v = sorted(v)
    cdf_plot(v[0:390000], 'red', 'cc', 'PageRank', 'Percentage(%)', 20)    



