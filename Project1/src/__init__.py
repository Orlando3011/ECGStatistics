import pandas as pd

df = pd.read_csv("data.txt")
stats = df.describe()

document = stats.to_html("statistics.html")

outputFile = open("statistics.html", "r")

data = outputFile.read()


outputFile.close()

head = "<!DOCTYPE=html>\n<html>\n<head>Basic information about echocardiogram data</head>\n<body>\n"
tail = "</body></html>"
data = head + data + tail

outputFile = open("statistics.html", "w")

outputFile.write(data)

outputFile.close()
