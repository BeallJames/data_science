from plotly.graph_objs import Bar, Layout
from plotly import offline


from die import Die


# create a d6
die_1 = Die()
die_2 = Die()

# roll and store
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# analyze results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# visualize results
x_values = list(range(2, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Result", "dtick": 1}
y_axis_config = {"title": "Freq of Results"}
my_layout = Layout(
    title="results of 2xd6 * 1000", xaxis=x_axis_config, yaxis=y_axis_config
)
offline.plot({"data": data, "layout": my_layout}, filename="2d6.html")
