import pandas as pd
import matplotlib.pyplot as plt


class DataframeService:
    correlations = 0
    stats = 0
    df = 0

    def __init__(self, datafileName):
        self.datafileName = datafileName
        self.loadData()

    def loadData(self):
        self.df = pd.read_csv(self.datafileName)

    def computeStats(self):
        self.stats = self.df.describe()
        self.stats.to_html("output/stats.html")
        return self.stats

    def computeCorrelations(self):
        self.correlations = self.df.corr()
        self.correlations.to_html("output/correlations.html")
        return self.correlations

    def makeScatterplot(self, Xaxis, Yaxis, fileName):
        self.df.plot(kind='scatter', x=Xaxis, y=Yaxis)
        fileName = "output/" + fileName
        plt.savefig(fileName)
        plt.close()

    def makeHistogram(self, argument, fileName):
        self.df.hist(column=argument)
        fileName = "output/" + fileName
        plt.savefig(fileName)
        plt.close()

    def makeBoxplot(self, argument, fileName):
        self.df.boxplot(argument)
        fileName = "output/" + fileName
        plt.savefig(fileName)
        plt.close()

    @staticmethod
    def makeBarplot(dataframe, fileName, rowNum):
        row = dataframe.iloc[rowNum]
        row.plot(kind='bar')
        fileName = "output/" + fileName
        plt.savefig(fileName)
        plt.close()

