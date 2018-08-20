import numpy as np
import sys

def format_data(data, number_of_bins):
    data = sorted(data)
    x = np.linspace(0, max(data), number_of_bins)
    print(max(data))
    print(x)
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
    
    return [x, y]

def get_plt():
    import matplotlib
    matplotlib.use('TkAgg')
    import matplotlib.pyplot as plt
    matplotlib.rcParams['mathtext.fontset'] = 'stix'
    matplotlib.rcParams['font.family'] = 'STIXGeneral'
    return plt

def get_formatter():
    from matplotlib import ticker
    formatter = ticker.ScalarFormatter(useMathText=True)
    formatter.set_scientific(True) 
    formatter.set_powerlimits((-1,1))
    return formatter

def cdf_plot(x, y, xlabel, ylabel, title, formatter, plt):
    ax=plt.gca()
    ax.xaxis.set_major_formatter(formatter) 
    ax.set_xlabel(xlabel, fontsize=12)
    ax.set_ylabel(ylabel, fontsize=12)
    plt.title(title)
    plt.plot(x[0:len(y)], y, color="black", linewidth=1.2)
    plt.show()

if __name__ == '__main__':
    f = open("all_pagerank.txt", 'r')
    v = map(lambda x: float(x.strip()), f)
    v = sorted(v)
    [x, y] = format_data(v[0:390000], 20)
    print(x)
    print(y)
    cdf_plot(x, y, 'PageRank', 'Percentage(%)', "PageRank", get_formatter(), get_plt())