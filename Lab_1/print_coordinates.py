import matplotlib.pyplot as plt

def start():
    print("Hi! This work was written by Mykola Bovan KM-31 (km-31fpm-23-169)")
    print('This program will print coordinates from DS9.txt file')


def load_coordinates():
    with open('DS9.txt') as f:
        coordinates = f.readlines()
    return coordinates


def tuple_coordinates(coordinates):
    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i].split()
        coordinates[i][0] = int(coordinates[i][0])
        coordinates[i][1] = int(coordinates[i][1])
        coordinates[i] = tuple(coordinates[i])
    return coordinates


def get_coordinates():
    return tuple_coordinates(load_coordinates()) 


def plot_coordinates(coordinates):
    x, y = zip(*coordinates)
    plt.figure(figsize=(9.6, 5.4)) 
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.scatter(x, y, color='black', marker='o', label='Coordinates from DS9')
    plt.savefig('coordinates_plot.png', dpi=100)
    plt.show()


def main():
    start()

    coordinates = get_coordinates()
    plot_coordinates(coordinates)


if __name__ == '__main__':
    main()

