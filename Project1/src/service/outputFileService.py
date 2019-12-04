from Project1.src.service.dataframeService import DataframeService


class OutputFileService:
    dataframeService = DataframeService("data/data.txt")
    documentName = "output/statistics.html"
    head = "<!DOCTYPE=html>\n<html>\n<body>\n"
    tail = "</body></html>"

    def resetDocument(self):
        outputFile = open(self.documentName, "w")
        outputFile.write("")
        outputFile.close()

    def updateDocument(self, addition):
        outputFile = open(self.documentName, "r")
        output = outputFile.read()
        output = output + addition
        outputFile.close()

        outputFile = open(self.documentName, "w")
        outputFile.write(output)
        outputFile.close()

    def startDocument(self):
        self.updateDocument(self.head)

    def finishDocument(self):
        self.updateDocument(self.tail)

    def addBasicInfo(self):
        infoFile = open("data/echocardiogram.names", "r")
        info = infoFile.read()
        infoFile.close()
        self.updateDocument(info)

    def addStats(self):
        self.dataframeService.computeStats()
        statsFile = open("output/stats.html")
        stats = statsFile.read()
        stats = "\n<h2>Basic information regarding given dataset</h2>" + stats
        statsFile.close()
        self.updateDocument(stats)

    def addCorrelations(self):
        self.dataframeService.computeCorrelations()
        corrFile = open("output/correlations.html")
        correlations = corrFile.read()
        correlations = "\n<h2>Correlations between parameters</h2>\n" + correlations
        corrFile.close()
        self.updateDocument(correlations)

    def addScatterplot(self, Xaxis, Yaxis, filename):
        self.dataframeService.makeScatterplot(Xaxis, Yaxis, filename)
        plot = "<h2>Scatter plot of variables " + Xaxis + ", and " + Yaxis \
               + ":</h2>\n<img src='" + filename + "'>"
        self.updateDocument(plot)

    def addHistogram(self, argument, fileName):
        self.dataframeService.makeHistogram(argument, fileName)
        plot = "<h2>Histogram of variable " + argument + ":</h2>\n<img src='" + fileName + "'>"
        self.updateDocument(plot)

    def addBoxplot(self, argument, fileName):
        self.dataframeService.makeBoxplot(argument, fileName)
        plot = "<h2>Boxplot of variable " + argument + ":</h2>\n<img src='" + fileName + "'>"
        self.updateDocument(plot)

    def assembleDocument(self):
        self.resetDocument()
        self.startDocument()
        self.addBasicInfo()
        self.addStats()
        self.addCorrelations()
        self.addScatterplot("epss", "lvdd", "scatterplot1.png")
        self.addScatterplot("age_at_heart_attack", "survival", "scatterplot2.png")
        self.addHistogram("survival", "histogram1.png")
        self.addHistogram("age_at_heart_attack", "histogram2.png")
        self.addHistogram("epss", "histogram3.png")
        self.addHistogram("lvdd", "histogram4.png")
        self.addHistogram("still_alive", "histogram5.png")
        self.finishDocument()


