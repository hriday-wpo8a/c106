import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as csv_file:
        df = csv.DictReader(csv_file)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    Marks_In_Percentage=[]
    Days_Present=[] 
    with open(data_path) as csv_file :
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Marks_In_Percentage.append(float(row["Marks In Percentage"]))
            Days_Present.append(float(row["Days Present"]))
    return {"x":Marks_In_Percentage,"y":Days_Present}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print("correlation between marks in percentage and days present is : ",correlation[0,1])

def setup():
    data_path = "marksVSpresent.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)
    plotFigure(data_path)

setup()