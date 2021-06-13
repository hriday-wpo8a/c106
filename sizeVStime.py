import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig=px.scatter(df,x="Size of TV",y="time spent")
        fig.show()

def getDataSource(data_path):
    Size_of_TV=[]
    time_spent=[] 
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row["Size of TV"]))
            time_spent.append(float(row["time spent"]))
    return {"x":Size_of_TV,"y":time_spent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between size of tv and time spent is : ",correlation[0,1])

def setup():
    data_path = "sizeVStime.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()