import matplotlib.pyplot as plt
from random import randint
from math import atan2
import collections

def create_points(num_of_p, min=0, max=50):
    '''
    The create_point function returns a list of random points
    with integer values

    num_of_p: the number of points that we want to create
    (min,max): The value range of our points
    '''
    return [[randint(min,max), randint(min, max)] for _ in range(num_of_p)]


def lowest_point_index(coord): 
    '''
     The lowest_point function calculates the lowest point 
     of the input points according to the y-coordinate

     coord: list of lists
    '''

    min = coord[0][1]
    
    low_p_index = 0
    for index in range(1, len(coord)):
        if coord[index][1] < min:
            min = coord[index][1]
            low_p_index = index
            
            

    return low_p_index


# def distance_square(p, q):
#     return (q[1]-p[1])**2 + (q[0]-p[0])**2

def polar_angle(p, coord):
    min_index = lowest_point_index(coord)
    coord[0], coord[min_index] = coord[min_index], coord[0]
    atan2_val = []
    dict_p_angle = {}
    for val in coord[1:]:
        atan2_val.append(atan2(p[1]-val[1], p[0]-val[0]))
        dict_p_angle[atan2_val[-1]] = val
    return dict_p_angle

# coord = create_points(20)
# d = polar_angle(lowest_point(coord)[0], coord)
# od = collections.OrderedDict(sorted(d.items()))
# for k in od.keys():
#     print(k, '\n')

def det(p1, p2, p3):
    d = (p2[0]-p1[0])*(p3[1]-p1[1]) - (p2[1]-p1[1])*(p3[0]-p1[0])
    return d
    # if d < 0:
    #     return -1
    # if d > 0:
    #     return 1
    # if d == 0:
    #     return 0


def sort_points(coord):
    """Return point_array sorted by leftmost first, then by slope, ascending."""

    d = polar_angle(coord[lowest_point_index(coord)], coord)
    od = collections.OrderedDict(sorted(d.items()))
    return od


def scatter_plot(coord, convex_hull=None):
    x = [x for x, y in coord]
    y = [y for x, y in coord]
    plt.scatter(x, y)

    if convex_hull != None:
        for i in range(1, len(convex_hull)+1):
            if i==len(convex_hull): i = 0
            c0 =convex_hull[i-1]
            c1 = convex_hull[i]
            plt.plot((c0[0],c1[0]), (c0[1],c1[1]), 'r')

    
    plt.show()

def ch_plot(coord, show_flag=False):

    min_index = lowest_point_index(coord)
    anchor = coord[min_index]
    sorted_points =[]
    for v in sort_points(coord).values():
        sorted_points.append(v)
    hull = [anchor, sorted_points[0]]
    for s in sorted_points[1:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], s) <= 0:
            hull.pop()
        hull.append(s)
        if show_flag: 
            scatter_plot(coord, hull)

    return hull

pts = create_points(15)
hull = ch_plot(pts)
scatter_plot(pts, hull)