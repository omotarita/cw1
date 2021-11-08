# Write code that prepares your 
import pandas as pd
import numpy as np
import os

from pandas.core.frame import DataFrame

def import_datasets(filename, worksheetName):
    #google_sheet_link = link
    #clean_link = google_sheet_link.replace('/edit#gid=', '/export?format=csv&gid=')

    dataRangeList = []


    with open(filename) as myData:
        for num, line in enumerate(myData, 1):
            dataRange = []

            if 'Title' in line:
                dataRange.append(num)
            elif 'Comments' in line:
                dataRange.append(num)

            dataRangeList.append(dataRange)
    
    result = DataFrame


    for i in dataRangeList:
        startLine = dataRangeList[i][0]
        endLine = dataRangeList[i][1]

        df = pd.read_csv(filename, header = startLine, skipfooter = endLine)  

        result = pd.concat(df)


                

            

    df = pd.read_csv(filename, worksheetName, header = dataStarts - 1)
        #Reference Chris from Stack Overflow (https://stackoverflow.com/questions/65569901/how-create-a-dataframe-from-a-csv-file-using-only-certain-lines)
    
    #(clean_link, worksheetName, index_col = False)
    #df = pd.read_csv(clean_link, worksheetName, skiprows=2, index_col = False)

    return df

def clean_comments(df):
    for index in df.index:
        print(df[0][index])
    #if list[0]

    pass

def main():

    # Test 1: what is the dataset
    
    #link = 'https://docs.google.com/spreadsheets/d/1ErknXQyMM8nsZxEk142MtaGeOAJEOfMr/edit?usp=sharing&ouid=112212588645125254077&rtpof=true&sd=true'
    filename = '2001_single_sheet.csv'
    worksheetName = None

    print(import_datasets(filename, worksheetName))

    pass


if __name__ == '__main__':
    main()


