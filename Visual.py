# importing the required module
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import Config
import Bounds

class Visual:
    def print_simple(self):
        # x axis values
        x = [1, 2, 3]
        # corresponding y axis values
        y = [2, 4, 1]
        # plotting the points
        plt.plot(x, y)
        # naming the x axis
        plt.xlabel('x - axis')
        # naming the y axis
        plt.ylabel('y - axis')
        # giving a title to my graph
        plt.title('My first graph!')
        # function to show the plot
        plt.show()

    def print_elaborate(self, x_arr, y_arr, legend_array=None):
        for gra in y_arr:
            plt.plot(x_arr, gra)
        # Naming the x-axis, y-axis and the whole graph
        plt.xlabel("Delta")
        plt.ylabel("Rate")
        plt.title("Rate To Delta Bounds")
        # Adding legend, which helps us recognize the curve according to it's color
        plt.legend(legend_array)
        # To load the display window
        plt.show()

    def fig_elaborate(self, x_arr, y_arr, legend_array=None):
        fig = matplotlib.figure.Figure(figsize=(8, 4), dpi=100)
        plt_inst = fig.add_subplot(111,
                                   xlabel = "Delta",
                                   ylabel = "Rate",
                                   title = "Rate To Delta Bounds")
        for gra in y_arr:
            plt_inst.plot(x_arr, gra)
        # Adding legend, which helps us recognize the curve according to it's color
        fig.legend(legend_array,
                   shadow = True)
        return fig


vis_inst = Visual()


