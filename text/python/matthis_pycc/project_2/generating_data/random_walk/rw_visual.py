import matplotlib.pyplot as plt

from random_walk import Randomwalk


# make a random walk
rw = Randomwalk()
rw.fill_walk()

# plot the point
plt.style.use("classic")
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
