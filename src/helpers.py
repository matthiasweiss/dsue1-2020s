import itertools
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd

##
# helper functions for dictionaries
##

# get top n items of a sorted dictionary
def get_top_n(sorted_dict, n=None):
    if n is None:
        n = len(sorted_dict)

    return dict(itertools.islice(sorted_dict.items(), 0, n))


# sort a dictionary on its key
def sort_dict_by_key(unsorted_dict):
    sorted_dict = {}

    for key in sorted(unsorted_dict):
        sorted_dict[key] = unsorted_dict[key]

    return sorted_dict


# sort a dictionary on its value
def sort_dict_by_value(unsorted_dict):
    sorted_dict = {}

    for a in sorted(unsorted_dict, key=unsorted_dict.get, reverse=True):
        sorted_dict[a] = unsorted_dict[a]

    return sorted_dict


##
# helper functions for plots
##

# create bar plot of given histogram
def bar_plot(histogram):
    # set figure and font size
    plot.figure(figsize=(15, 8))
    plot.rc('font', size=8)

    height = histogram.values()
    bars = histogram.keys()
    y_pos = np.arange(len(bars))

    # create bars
    plot.bar(y_pos, height)

    # create names on the x-axis
    plot.xticks(y_pos, bars)

    # show graphic
    plot.show()


# create lollipop plot of given histogram
def lollipop_plot(histogram):
    # set figure size
    plot.figure(figsize=(15, 8))
    plot.rc('font', size=8)

    # create a dataframe
    df = pd.DataFrame({'group': list(histogram.keys()),
                       'values': list(histogram.values())})

    # reorder it following the values
    ordered_df = df.sort_values(by='values', ascending=False)
    my_range = range(0, len(df.index))

    # draw plot
    plot.stem(ordered_df['values'], use_line_collection = True)
    plot.xticks(my_range, ordered_df['group'])

    plot.show()


# create scatter plot of given histogram
def scatter_plot(histogram):
    # create data
    x = 10 * np.random.rand(len(histogram))
    y = 10 * np.random.rand(len(histogram))

    # use the scatter function
    plot.scatter(x, y, s=list(histogram.values()), alpha=0.5)
    plot.show()
