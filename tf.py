import math
import numpy as np
from sklearn.preprocessing import minmax_scale
import matplotlib.pyplot as plt
import pysvg
from svg.path import parse_path


def tf(x, y, y_scale=(0.2, 1)):

    x = minmax_scale(x, (0, 1))
    y = minmax_scale(y, y_scale)

    TWOPI = 2 * np.pi

    l = x.max()
    r = l / TWOPI

    nx = r * np.cos(TWOPI * x / l) * y
    ny = r * np.sin(TWOPI * x / l) * y
    return nx, ny


def tf_spiral(x, y, turns=1, x_scale=(0, 1), y_scale=(0.2, 1)):
    x = minmax_scale(x, (0, 1))
    y = minmax_scale(y, y_scale)

    MULTIPI = 2 * turns * np.pi

    l = x.max()
    r = l / MULTIPI

    nx = r * np.cos(MULTIPI * x / l) * y
    ny = r * np.sin(MULTIPI * x / l) * y

    # x = t .. time
    # t = x
    # b = r
    # a = y
    # nx = (a + b * t) * np.cos(t)
    # ny = (a + b * t) * np.sin(t)

    # nx = (a + b * t) * np.cos(t)
    # ny = (a + b * t) * np.sin(t)
    return nx, ny


def tf_spiral_single(x, y, turns=1, xmax=1):

    MULTIPI = 2 * turns * np.pi

    l = xmax  # x.max()
    r = l / MULTIPI

    nx = r * math.cos(MULTIPI * x / l) * y
    ny = r * math.sin(MULTIPI * x / l) * y

    # x = t .. time
    # t = x
    # b = r
    # a = y
    # nx = (a + b * t) * np.cos(t)
    # ny = (a + b * t) * np.sin(t)

    # nx = (a + b * t) * np.cos(t)
    # ny = (a + b * t) * np.sin(t)
    return nx, ny


def plot_ekg(x, y):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.plot(x, y, 'r-')
    return fig, ax


def plot_circle(x, y):
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal')
    ax.plot(x, y, 'r-')
    return fig, ax


def try_tf(x, y, start=None, end=None, y_scale=(0.4, 0.6)):

    if start is None:
        start = 59
    if end is None:
        end = len(x)

    x, y = x[start:end], y[start:end]
    plot_ekg(x, y)

    x, y = tf(x, y, y_scale=y_scale)
    plot_ekg(x, y)
    return x, y


def try_tf_spiral(x, y, turns=1, start=None, end=None, x_scale=(0, 1), y_scale=(0.4, 0.6)):

    if start is None:
        start = 59
    if end is None:
        end = len(x)

    x, y = x[start:end], y[start:end]
    plot_ekg(x, y)

    x, y = tf_spiral(x, y, turns, x_scale, y_scale)
    plot_ekg(x, y)
    return x, y


def read_svg(path, num_samples=1000):
    # pysvg
    f = pysvg.parser.parse(path)

    path = f
    while type(path) != pysvg.shape.Path:
        path = path.getAllElements()[0]

    # parse_path from svg.path
    path_data = parse_path(path.getAttribute('d'))
    return np.array([path_data.point(i) for i in np.linspace(0, 1, num_samples)])
