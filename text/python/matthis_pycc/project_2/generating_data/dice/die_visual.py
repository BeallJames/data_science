from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die


# create a d6
die = Die()

# roll and store
results = []
for roll_num in range(1000):
    results.append(die.roll())

# analyze results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title", "Result"}
y_axis_config = {"title", "Freq of Results"}
my_layout = Layout(
    title="results of d6 * 1000", xaxis=x_axis_config, yaxis=y_axis_config
)
offline.plot({"data": data, "layout": my_layout}, filename="d6.html")
