import matplotlib.pyplot as plt


def load_coordinates():
    with open('Lab_2/DS9.txt') as f:
        coordinates = f.readlines()
    return coordinates


def tuple_coordinates(coordinates):
    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i].split()
        coordinates[i][0] = int(coordinates[i][0])
        coordinates[i][1] = int(coordinates[i][1])
        coordinates[i] = tuple(coordinates[i])
    return coordinates


def get_coordinates() -> list[tuple[int, int]]:
    return tuple_coordinates(load_coordinates()) 


def jarvis_march(points):
    if len(points) < 3:
        return points

    start = min(points, key=lambda p: (p[0], p[1]))
    hull = [start]

    def orientation(p, q, r):
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        return 0 if val == 0 else (1 if val > 0 else -1)

    current = start
    while True:
        next_point = points[0]
        for point in points:
            if point == current:
                continue
            if next_point == current or orientation(current, next_point, point) == -1:
                next_point = point
        
        if next_point == start:
            break

        hull.append(next_point)
        current = next_point

    return hull


def plot_coordinates(coordinates, hull):
    x, y = zip(*coordinates)
    plt.figure(figsize=(9.6, 5.4)) 
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.scatter(x, y, color='black', marker='o', label='Coordinates from DS9')
    plt.plot(*zip(*hull), color='red', linestyle='-', linewidth=2, label='Convex Hull')
    plt.savefig('convex_hull_plot.png', dpi=100)
    plt.show()




if __name__ == "__main__":
    coordinates = get_coordinates()
    hull = jarvis_march(coordinates)

    print("Опукла оболонка:")
    for point in hull:
        print(point)

    plot_coordinates(coordinates, hull)
