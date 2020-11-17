import matplotlib.pyplot as plt
from random import randint
from math import atan2
import collections

def create_points(num_of_p, min=0, max=100):
    '''
    The create_point function returns a list of random points
    with integer values

    num_of_p: the integer number of points that we want to create
    (min,max): The value range of our points
    '''
    return [[randint(min,max), randint(min, max)] for _ in range(num_of_p)]


def lowest_point_index(data): 
    '''
    The lowest_point function returns the  index of the lowest 
    point of the input points according to the y-datainate

    data: list of lists 
    '''

    min = data[0][1]
    
    lowest_point_index = 0
    for index in range(1, len(data)):
        if data[index][1] < min:
            min = data[index][1]
            lowest_point_index = index
            
    return lowest_point_index


def distance_square(p, q):
    return (q[1]-p[1])**2 + (q[0]-p[0])**2

def polar_angle_dict(p, data):
    '''
    The polar_angle_dict function returns a dictionary with keys the
    polar angles of the lowest point with the rest points and values
    the corresponding points 

    p: list with the x,y datainates of the lowest point
    data: list of lists
    '''

    min_index = lowest_point_index(data)
    data[0], data[min_index] = data[min_index], data[0]
    dict_p_angle = {}
    for val in data[1:]:
        at2 = atan2(p[1]-val[1], p[0]-val[0])
        if at2 in dict_p_angle:
            d1 = distance_square(data[min_index], dict_p_angle[at2])
            d2 = distance_square(data[min_index], val)
            if d1 < d2:
                dict_p_angle[at2] = val
        else:
            dict_p_angle[at2] = val
    return dict_p_angle


def det(p1, p2, p3):
    '''
    The det function returns the determinant of the three points p1, p2, p3
    '''

    d = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
    return d


def sort_points(data):
    '''
    The sort_points function returns the dictionary from the polar_angle_function
    sorted based on keys

    '''

    d = polar_angle_dict(data[lowest_point_index(data)], data)
    od = collections.OrderedDict(sorted(d.items()))  
    return od

print(sort_points(create_points(10)))
def plot_func(data, convex_hull=None):
    '''
    The scatter_plot function plots the points and the Convex Hull

    convex_hull: if convex_hull is None then the scatter_plot function
    plots only the points
    '''
    x = [x for x, y in data]
    y = [y for x, y in data]
    plt.scatter(x, y, c='r')

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i==len(convex_hull): i = 0
            p1 =convex_hull[i-1]
            p2 = convex_hull[i]
            plt.plot((p1[0],p2[0]), (p1[1],p2[1]), 'b')

    
    plt.show()

def ch(data, show_flag=False):

    min_index = lowest_point_index(data)
    anchor = data[min_index]
    sorted_points =[]
    for v in sort_points(data).values():
        sorted_points.append(v)
    hull = [anchor, sorted_points[0]]
    for s in sorted_points[1:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)
        if show_flag: 
            plot_func(data, hull)

    return hull

pts = create_points(15)
hull = ch(pts)
plot_func(pts, hull)
