from Project1.src.service.dataframeService import DataframeService


class OutputFileService:
    dataframeService = DataframeService("data/data.txt")
    documentName = "output/statistics.html"
    head = "<!DOCTYPE=html>\n<html>\n<head>\n<link rel='stylesheet'" \
           " type='text/css' href='style.css'>\n</head>\n<body>\n"
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
        statsDf = self.dataframeService.computeStats()
        statsFile = open("output/stats.html")
        stats = statsFile.read()
        stats = "\n<h2>Basic information regarding given dataset</h2>" + stats
        self.updateDocument(stats)
        self.addBarplot(statsDf, "barplot1.png", "mean", 1)
        self.addBarplot(statsDf, "barplot2.png", "standard deviation", 2)
        self.addBarplot(statsDf, "barplot3.png", "minimum value", 3)
        self.addBarplot(statsDf, "barplot4.png", "maximum value", 7)
        statsFile.close()

    def addCorrelations(self):
        corrs = self.dataframeService.computeCorrelations()
        corrFile = open("output/correlations.html")
        correlations = corrFile.read()
        correlations = "\n<h2>Correlations between parameters</h2>\n" + correlations
        corrFile.close()
        self.updateDocument(correlations)
        self.addBarplot(corrs, "barplot5.png", "correlations of survival", 1)
        self.addBarplot(corrs, "barplot6.png", "correlations of still_alive", 2)
        self.addBarplot(corrs, "barplot7.png", "correlations of age_at_heart_attack", 3)
        self.addBarplot(corrs, "barplot8.png", "correlations of pericardial_effusion", 4)
        self.addBarplot(corrs, "barplot9.png", "correlations of fractional_shortening", 5)
        self.addBarplot(corrs, "barplot10.png", "correlations of epss", 6)
        self.addBarplot(corrs, "barplot11.png", "correlations of lvdd", 7)
        self.addBarplot(corrs, "barplot12.png", "correlations of wall_motion_score", 8)
        self.addBarplot(corrs, "barplot13.png", "correlations of wall_motion_index", 9)
        self.addBarplot(corrs, "barplot14.png", "correlations of alive_at_1", 10)

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

    def addBarplot(self, dataframe, fileName, argument, rowNum):
        self.dataframeService.makeBarplot(dataframe, fileName, rowNum)
        plot = "<h2>Barplot of " + argument + ":</h2>\n<img src='" + fileName + "'>"
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
        self.addHistogram("still_alive", "histogram2.png")
        self.addHistogram("age_at_heart_attack", "histogram3.png")
        self.addHistogram("pericardial_effusion", "histogram4.png")
        self.addHistogram("fractional_shortening", "histogram5.png")
        self.addHistogram("epss", "histogram6.png")
        self.addHistogram("lvdd", "histogram7.png")
        self.addHistogram("wall_motion_score", "histogram8.png")
        self.addHistogram("wall_motion_index", "histogram9.png")
        self.addHistogram("alive_at_1", "histogram10.png")
        self.finishDocument()
