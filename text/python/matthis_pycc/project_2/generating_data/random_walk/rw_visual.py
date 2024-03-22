import matplotlib.pyplot as plt

from random_walk import Randomwalk

# keep making new walks
while True:
    # make a random walk
    rw = Randomwalk()
    rw.fill_walk()

    # plot the point
    plt.style.use("classic")
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors="none",
        s=15,
    )
    plt.show()

    keep_running = input("make another walk? (y/n)")
    if keep_running == "n":
        break
