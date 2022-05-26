import sys
import numpy as np 
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.io import export_png
from bokeh.models import ColumnDataSource, DataTable, DateFormatter, TableColumn

def readInData(filePath):
    allHits = []
    BUSCOs = {}
    contigs = set()

    with open(filePath, 'r') as dataFile:
        line = dataFile.readline()
        for line in dataFile:
            if line.startswith('# D') or line.startswith('# F'):
                continue
            elif line.startswith('# B'):
                numUnique = len(contigs)
                BUSCOs[name] = [hits,numUnique]
                contigs = set()
            elif line.startswith("# Q"):
                queryLine = line.strip('\n').split(' ')
                name = queryLine[2]
            elif line.startswith("#") == False:
                contigLine = line.strip('\n').split('\t')
                contig = contigLine[1]
                contigs.add(contig)
            else:
                hitsLine = line.strip('\n').split(' ')
                hits = int(hitsLine[1])
                allHits.append(hits)
    return allHits, BUSCOs

def createHistogram(filePath, allHits):

    output_file(filePath + '_histogram.html')

    histogram, bins = np.histogram(allHits, bins=50)

    dataFrame = pd.DataFrame({'hits': histogram, 'left': bins[:-1], 'right': bins[1:]},)

    p = figure(plot_height = 600, plot_width = 600, title = filePath,
        x_axis_label = 'Number of Hits', y_axis_label = 'Frequency of Hits')

    p.quad(bottom=0, top=dataFrame['hits'], 
           left=dataFrame['left'], right=dataFrame['right'], 
           fill_color='powderblue', line_color='midnightblue')

    show(p)
    #export_png(p, filename=filePath + "_histogram.png")

def createDataFrame(BUSCOs, contigsOrHits):
    buscos = []
    hits = []
    unique = []
    for key,value in BUSCOs.items():
        buscos.append(key)
        hits.append(value[0])
        unique.append(value[1])
    allData = pd.DataFrame({'buscos': buscos, 'hits': hits, 'contigs': unique},)
    allDataSorted = allData.sort_values(contigsOrHits)
    return allDataSorted

def createLinePlot(filePath, allHits):
    allHits = sorted(allHits)
    buscos = [*range(0,len(allHits))]

    output_file(filePath + '_lineplot.html')
    p = figure(plot_height = 600, plot_width = 1200, 
               title = filePath,
              y_axis_label = 'Number of Hits', 
               x_axis_label = 'BUSCOs')
    p.line(x = buscos, y = allHits, line_width = 3, color = "midnightblue")
    #show(p)
    export_png(p, filename=filePath + "_lineplot.png")


def filterDataFrame(sortedDataFrame, contigsOrHits):

    quantile = sortedDataFrame[contigsOrHits].quantile(.75)

    condition = "{0} <= {1}".format(contigsOrHits,quantile)
    dataToQuantile = sortedDataFrame.query(condition)

    meanOfQuantile = dataToQuantile[contigsOrHits].mean()
    #print(meanOfQuantile)
    multiplier = 10
    cutoff = meanOfQuantile * multiplier
    #print(cutoff)

    repeatCondition = "{0} >= {1}".format(contigsOrHits, cutoff)
    repeatTable = sortedDataFrame.query(repeatCondition)

    return cutoff, repeatTable

def createTable(filePath, dataFrame, contigsOrHits):
    #output_file(filePath + "_" + contigsOrHits + '_table.html')
    #source = ColumnDataSource(dataFrame)
    #columns = [TableColumn(field="buscos", title="Name"),TableColumn(field="hits", title="Hits"),TableColumn(field="contigs", title="Unique Contigs")]
    #data_table = DataTable(source=source, columns=columns, width=400, height=600)
    
    dataFrame.to_csv(path_or_buf = filePath + ".csv", index = False) #can change to tsv with sep = '/t'
    #show(data_table)

if __name__ == '__main__':
    #   Comment out/in which commands you want based on what you want to output
    filePath = sys.argv[1]

    allHits, BUSCOs = readInData(filePath)

    #createHistogram(filePath, allHits)
    createLinePlot(filePath,allHits)

    #createTable(filePath, createDataFrame(BUSCOs, 'hits'), "")

    hitsCutoff, filterByHits = filterDataFrame(createDataFrame(BUSCOs, 'hits'), "hits")
    createTable(filePath, filterByHits, "hits")
    #index = filterByHits.index
    #numRowsHits = len(index) - 1

    #contigsCutoff, filterByContigs = filterDataFrame(createDataFrame(BUSCOs, 'contigs'), "contigs")
    #createTable(filePath, filterByContigs, "contigs")
    #index = filterByContigs.index
    #numRowsContigs = len(index) - 1

    #with open("resultsTable.txt", "a") as table:
    #    data = "{}\t{}\t{}\t{}\t{}\n".format(filePath, contigsCutoff, hitsCutoff, numRowsContigs, numRowsHits)
    #    table.write(data)
