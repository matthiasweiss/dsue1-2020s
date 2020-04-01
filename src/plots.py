from helpers import *
import imdb


# use decades histogram to create bar plot
def bar_plot_decades(histogram=None):
    if histogram is None:
        return bar_plot(imdb.get_decades_histogram())

    return bar_plot(histogram)


# scatter plot of all actresses*actors
def lollipop_plot_actresses():
    lollipop_plot(imdb.get_top_n_actresses(10))


# bar plot for all genres
def bar_plot_genres():
    bar_plot(imdb.get_most_popular_genres_by_name())


# generate desired plots
bar_plot_decades()
lollipop_plot_actresses()
bar_plot_genres()
