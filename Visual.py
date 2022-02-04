# importing the required module
import matplotlib.pyplot as plt
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

    def print_elaborate(self, x_arr, y_arr):
        for gra in y_arr:
            plt.plot(x_arr, gra)
        # Naming the x-axis, y-axis and the whole graph
        plt.xlabel("Delta")
        plt.ylabel("Rate")
        plt.title("Rate To Delta Bounds")
        # Adding legend, which helps us recognize the curve according to it's color
        plt.legend()
        # To load the display window
        plt.show()

    def calculate_delta_to_rate_plot(self):
        # delta axis values
        delta_arr = np.arange(1.0 / Config.n, 1, Config.res)
        graph_arr = [None] * len(Bounds.bounds_inst.bound_arr)
        for i in range(0, len(Bounds.bounds_inst.bound_arr)):
            bound = Bounds.bounds_inst.bound_arr[i]
            graph_arr[i] = [bound(Bounds.bounds_inst, Config.n, delta, Config.q) for delta in delta_arr]
        return delta_arr, graph_arr


