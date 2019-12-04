import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.txt")
stats = df.describe()
correlations = df.corr()

df.plot(kind='scatter', x='epss', y='lvdd')
plt.savefig("scatterplot1")
df.hist(column="survival")
plt.savefig("histogram1")

document = stats.to_html("statistics.html")
corrDocument = correlations.to_html("correlations.html")

outputFile = open("statistics.html", "r")
corrFile = open("correlations.html", "r")
infoFile = open("echocardiogram.names", "r")

data = outputFile.read()
info = infoFile.read()
corr = corrFile.read()

outputFile.close()
corrFile.close()
infoFile.close()

head = "<!DOCTYPE=html>\n<html>\n<head>Basic information about echocardiogram data</head>\n<body>\n"
image1 = "<h2>Scatterplot of EPSS and LVDD variables</h2>\n<img src='scatterplot1.png'>"
image2 = "<h2>Histogram of survival length after the heart attack (in months)</h2>\n<img src='histogram1.png'>"
tail = "</body></html>"
text = head + info + "\n<h2>Basic information regarding given dataset</h2>" \
       + data + "\n<h2>Correlations between parameters</h2>\n" + corr + image1 + image2 + tail

outputFile = open("statistics.html", "w")

outputFile.write(text)
outputFile.close()
