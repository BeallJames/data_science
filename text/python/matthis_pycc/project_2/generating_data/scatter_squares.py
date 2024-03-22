import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-darkgrid")
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# title and axes
ax.set_title("square numbers", fontsize=24)
ax.set_xlabel("value", fontsize=14)
ax.set_ylabel("squared value", fontsize=14)

# tick
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
