from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2


def min_squared_divide_and_conquer(points):
    def recur_divide(point_list, min_dist):

        list_length = len(point_list)

        if list_length <= 2:
            if list_length == 2:
                # Check for smaller distances
                min_dist = min(min_dist, distance_squared(point_list[0], point_list[1]))
            return min_dist

        mid = list_length // 2
        min_dist_left = recur_divide(point_list[:mid], min_dist)
        min_dist_right = recur_divide(point_list[mid:], min_dist)

        # Get the smallest distance
        min_dist = min(min_dist_left, min_dist_right)

        # Get x-value that was used as the dividing line
        mid_x_val = point_list[mid].x

        # Filter out points too far away for the next comparison
        possible_points = [point for point in point_list if abs(point.x - mid_x_val) <= min_dist]

        # Now sort new list by y value
        possible_points.sort(key=lambda point: point[1])

        # Check point by point for any smaller squared distances
        # Start value used to reduce nested loop list length
        start = 1
        for point1 in possible_points:
            # Oddly, turns out only 7 items can be within range, otherwise difference in y val is > min_dist
            # This Key Lemma dramatically helps reduce time taken for this nest loop
            for point2 in possible_points[start:start+7]:

                min_dist = min(min_dist, distance_squared(point1, point2))

            # Move start forward for inner loop splice
            start += 1
        return min_dist

    # Sort points by x value, add index value for y sort matching within recursive calls
    points.sort()

    # Initialize min_distance to positive infinity
    min_distance = float("inf")

    # Call recursive divide and conquer function
    min_distance = recur_divide(points, min_distance)

    return min_distance


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(min_squared_divide_and_conquer(input_points))))

