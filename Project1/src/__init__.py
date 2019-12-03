import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.txt")
stats = df.describe()

df.plot(kind='scatter', x='epss', y='lvdd')
plt.savefig("scatterplot1")

document = stats.to_html("statistics.html")

outputFile = open("statistics.html", "r")

data = outputFile.read()

outputFile.close()

head = "<!DOCTYPE=html>\n<html>\n<head>Basic information about echocardiogram data</head>\n<body>\n"
image = "<img src='scatterplot1.png'>"
tail = "</body></html>"
data = head + data + image + tail

outputFile = open("statistics.html", "w")

outputFile.write(data)
outputFile.close()
