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


def cdf_plot_in_the_same_pic(data_list, titles, xlabel, ylabel, title, plt, formatter, filename="none"):
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
    if filename != "none":
        plt.savefig("draw_cdf/" + filename)
    plt.close()

if __name__ == '__main__':
    subjects = ["cs", "bio", "soc", "phy"]
    index_types = [
            ["result_", "_citation_cdf.txt"],
            ["result_", "_g_idx_cdf.txt"],
            ["result_", "_deg_cdf.txt"],
            ["result_", "_h_idx_cdf.txt"],
            ["result_", "_cc_cdf.txt"]
        ]
    pic_name = ["citation_cdf.png", "g_index_cdf.png",
                "deg_cdf.png", "h_index_cdf.png", "cc_cdf.png"]
    titles = ["Citation", "G_Index", "Degree", "H_Index", "Clustering Coefficient"]
    for (index, index_type) in enumerate(index_types):
        data_list = []
        for subject in subjects:
            filename = index_type[0] + subject + index_type[1]
            f = open(filename, 'r')
            v = map(lambda x: float(x.strip()), f)
            f.close()
            v = sorted(v)
            [x, s] = format_data(v, 100)
            data_list.append((x, s))
        cdf_plot_in_the_same_pic(data_list, subjects, \
            'Citation', 'Percentage(%)', \
                titles[index], get_plt(), get_formatter(), pic_name[index]) 