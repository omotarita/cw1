# Write code that prepares your 
import pandas as pd
import numpy as np
import os

from pandas.core.frame import DataFrame

def import_datasets(filename, worksheetName):
    """A function that only reads the key sections of the raw CSV files, then stores these key sections in another variable"""

    dataRange = []
    dataRangeList = []
    i = 0

    with open(filename) as myData:
        for num, line in enumerate(myData, 1):

            if 'Title' in line:
                dataRange.insert(0, num)
        
            elif 'Comments' in line:
                dataRange.insert(1, num)
                
                dataRangeList.insert(i, dataRange)
                dataRange = []
                i+=1

            else:
                pass
    

    result = DataFrame
    dfList = []
    dex = 0

    for i in dataRangeList:
        startLine = i[0]
        endLine = i[1]

        dataLen = endLine - startLine - 2

        df = pd.read_csv(filename, header = startLine - 1, nrows = dataLen)
        #Reference Chris from Stack Overflow (https://stackoverflow.com/questions/65569901/how-create-a-dataframe-from-a-csv-file-using-only-certain-lines)
        dfList.insert(dex, df)
        dex+=1    # 'dex' represents the index as 'i' is already used in this loop

        result = pd.concat(dfList)
    

    return result



def remove_extras(result):
    """A function that removes the information we don't need: the rows containing null values and the unnecessary columns"""

    deadColumns = ['Unnamed: 0', 'Gross', '% chg', 'Week #', 'Sites', 'Cum to date', 'Site Avg', 'Box office  to date', 'Box office to date', 'Unnamed: 8', 'Site avg']
    
    for i in deadColumns:
        if i in result:
            result = result.drop([i], axis = 1)

        else:
            pass
    #result = result.drop(result.columns[[3,4]], axis = 1)


    result = result.dropna(axis=0, how='any')

    cleanData = result

    return cleanData



def write_to_csv(cleanDataList):
    """A function that concatenates this clean dataframe with our 'prepared_data.csv' file"""
    df = pd.concat(cleanDataList)
    df.to_csv("prepared_data.csv", index=False)

    pass



def remove_repeats():
    """A quality control function that removes all repeated data from the 'prepared_data.csv' file"""
    df = pd.read_csv('prepared_data.csv', skiprows=0)
    df.drop_duplicates(inplace=True)

    df.to_csv("prepared_data.csv", index=False)
    pass



def main():

    filenames = ['2001_single_sheet.csv', '2002_single_sheet.csv', '2003_single_sheet.csv', '2004_single_sheet.csv', '2005_single_sheet.csv', '2006_single_sheet.csv']
    cleanDataList = []
    #filename = '2001_single_sheet.csv'
    worksheetName = None

    # Test 1: what is the dataset
    #print(import_datasets(filename, worksheetName))

    # Test 2: is it clean?
    #result = import_datasets(filename, worksheetName)
    #print(remove_extras(result))

    # Test 3: can we write this to a new file?
    n = 0

    for i in filenames:
        result = import_datasets(i, worksheetName)
        cleanData = remove_extras(result)
        cleanDataList.insert(n, cleanData)

    write_to_csv(cleanDataList)
    remove_repeats()

    pass


if __name__ == '__main__':
    main()


