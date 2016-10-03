import math
import matplotlib.pyplot as plt


def get_distance((x1, y1), (x2, y2)):
    """
    Calculates distance between two points
    :return: "square" of (x2-x1)2 + (y2-y1)2
    """
    a_line = math.pow(x2, 2) - math.pow(x1, 2)
    b_line = math.pow(y2, 2) - math.pow(y1, 2)
    return math.sqrt(a_line + b_line)


def get_closest_point((x, y), coord_list):
    """
    :param coord_list: List of coordinates [(34.234, 35.344), (36.6445, 45.8989), (56.3435, 45.545)]
    :return: Closest point to (x, y) from coord_list
    """
    try:
        coord_list.remove((x, y))
    except ValueError:
        print('not in list any longer (%s, %s)' % (x, y))

    min_distance = get_distance((x, y), coord_list[0])
    closest_point = coord_list[0]

    for point in coord_list:
        curr_instance = get_distance((x, y), point)
        if min_distance > curr_instance:
            min_distance = curr_instance
            closest_point = point
    coord_list.remove(closest_point)
    return closest_point


def draw_graph(coord_list):
    x =[]
    y =[]

    for item in sorted_by_distance:
        x.append(item[0])
        y.append(item[1])

    plt.plot(x, y, linestyle="dotted", marker="o", color="red")

    #labels
    plt.xlabel("this is X")
    plt.ylabel("this is Y")
    plt.grid(True)
    plt.savefig('fastest_way.png')
    plt.show()


def main(preferable_point, coordinates):
    """
    :param preferable_point: starting point of search
    :param coordinates: List of coordinates [(34.234, 35.344), (36.6445, 45.8989), (56.3435, 45.545)]
    :return: new list of points, sorted by distance
    """
    result = [preferable_point]
    next_point = get_closest_point(preferable_point, coordinates)
    result.append(next_point)

    while coordinates:
        curr_point = result[-1]
        closest_point = get_closest_point(curr_point, coordinates)
        result.append(closest_point)
    result.append(result[0])
    return result


c = [(50.466121, 30.354348), (50.463315, 30.355400), (50.464955, 30.362249), (50.465978, 30.373452)]
sorted_by_distance = main((50.463315, 30.355400), c)
print(sorted_by_distance)
draw_graph(sorted_by_distance)