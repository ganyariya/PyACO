import numpy as np
import matplotlib.pyplot as plt
import math


def init_plot():
    plt.ion()
    plt.title("ACO")
    plt.xlim(0, 1000)
    plt.ylim(0, 1000)
    plt.xlabel("x")
    plt.ylabel("y")


def play_plot(coordinates, super_path, best_path, plot_time):
    X = [xy[0] for xy in coordinates]
    Y = [xy[1] for xy in coordinates]
    plt.plot(X, Y, "o", c="red")

    super_x = [[coordinates[super_path[i]][0], coordinates[super_path[i + 1]][0]] for i in range(len(coordinates) - 1)]
    super_y = [[coordinates[super_path[i]][1], coordinates[super_path[i + 1]][1]] for i in range(len(coordinates) - 1)]

    best_x = [[coordinates[best_path[i]][0], coordinates[best_path[i + 1]][0]] for i in range(len(coordinates) - 1)]
    best_y = [[coordinates[best_path[i]][1], coordinates[best_path[i + 1]][1]] for i in range(len(coordinates) - 1)]

    plt.plot(super_x, super_y, c="green", linewidth=2)
    plt.plot(best_x, best_y, c="blue", ls=":", alpha=0.7)

    plt.draw()
    plt.pause(plot_time)
    plt.cla()
