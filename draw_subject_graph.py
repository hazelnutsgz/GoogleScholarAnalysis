import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

import numpy as np
import sys
from matplotlib import ticker
formatter = ticker.ScalarFormatter(useMathText=True)
formatter.set_scientific(True) 
formatter.set_powerlimits((-1,1)) 
matplotlib.rcParams['mathtext.fontset'] = 'stix'
matplotlib.rcParams['font.family'] = 'STIXGeneral'
from draw_hist import format_data, get_formatter, get_plt


def cdf_plot_in_the_same_pic(data_list, titles, xlabel, ylabel, title, plt, formatter):
    ax=plt.gca()
    ax.xaxis.set_major_formatter(formatter) 
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    plt.title(title)

    color_list = ["red", "blue", "green", "black", "yellow"]
    for index in range(len(data_list)):
        plt.plot(data_list[index][0], data_list[index][1], \
                    color=color_list[index], label=titles[index])
    plt.legend()
    plt.show()

if __name__ == '__main__':
    subjects = ["cs", "bio", "soc", "phy"]
    data_list = []
    for subject in subjects:
        filename = "result_" + subject + "_citation_cdf.txt"
        f = open(filename, 'r')
        v = map(lambda x: float(x.strip()), f)
        f.close()
        v = sorted(v)
        [x, s] = format_data(v, 100)
        data_list.append((x, s))
    cdf_plot_in_the_same_pic(data_list, subjects, \
        'Citation', 'Percentage(%)', \
            "Citation CDF", get_plt(), get_formatter()) 