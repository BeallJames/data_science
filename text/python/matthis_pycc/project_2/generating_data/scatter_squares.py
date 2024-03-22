import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=10)

# title and axes
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("squared value", fontsize=14)

# set range for axes
ax.axis([0, 1100, 0, 1100000])

# tick
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
