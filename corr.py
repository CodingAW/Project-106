import numpy as npy
import csv
import plotly.express as px

def plot_figure(data_path, xvalue, yvalue):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df, x= xvalue, y = yvalue)
        fig.show()

def get_data_source(data_path, xval, yval):
    x = []
    y = []
    with open(data_path) as f:
        r = csv.DictReader(f)

        for a in r:
            x.append(float(a[xval]))
            y.append(float(a[yval]))

    return { "x": x, "y": y}

def find_correlation(data_source):
    correlation = npy.corrcoef(data_source["x"], data_source["y"])
    return correlation[0, 1]

p1 = "data1.csv"
p2 = "data2.csv"

d1X = "Marks In Percentage"
d1Y = "Days Present"

data_source1 = get_data_source(p1, d1X, d1Y)
print("Coefficent of Correlation in Data One:", find_correlation(data_source1))
plot_figure(p1, d1X, d1Y)

d2X = "Coffee in ml"
d2Y = "sleep in hours"

data_source2 = get_data_source(p2, d2X, d2Y)
print("Coefficent of Correlation in Data Two:", find_correlation(data_source2))
plot_figure(p2, d2X, d2Y)