# Write code that explores your data set
import pandas as pd
import numpy as np
#import matplotlib
import matplotlib.pyplot as plt
from pandas.core.frame import DataFrame

def import_prepared_data():
    """A function that imports the data from the prepared_complete_data.csv file"""
    df = pd.read_csv('prepared_complete_data.csv', skiprows=0)

    return df

def tidy_for_exploration(df):
    """A function that tidies up the prepared data further, by removing columns we don't need for the data 
    exploration and renaming certain columns for ease of interpretation"""

    #Replace dataframe with the columns we need

    activeColumns = df[['Title','Genre 1','Genre 2','Popularity','Runtime (minutes)','Average Vote (/10)']]
    df = activeColumns.copy()

    #Rename certain columns
    df.rename(columns={'Runtime (minutes)':'Runtime (mins)'}, inplace=True)

    #Drop all rows with an average vote of less than 4
    #df = df[df['Average Vote (/10)'] >4 ]

    #Check for missing values
    #print(df.isna().any())

    return df

#def check_types():
    #A function that checks the type for the data"""
    #df = pd.read_csv('data.csv', dtype={'Title': str, 'Genre 1': str, 'Genre 2': str, 'Popularity': int, 'Runtime (mins)': int, 'Average Vote (/10)': int})
    #pass

def basic_stats(df, column):
    """A function that gets and returns some quick stats on your column of choice"""
    pass
    mean = df[column].describe()
    print(type(mean))
    print(mean)

def remove_outliers(df):
    stdPopularity = 32.77
    meanPopularity = 21.08
    stdAvgVote = 0.94
    meanAvgVote = 6.28

    maxOutlierPop = meanPopularity+(3*stdPopularity)
    minOutlierPop = meanPopularity-(3*stdPopularity)
    maxOutlierAvgVote = meanAvgVote+(3*stdAvgVote)
    minOutlierAvgVote = meanAvgVote-(3*stdAvgVote)


    #remove certain values from dataframe
    df = df[df['Average Vote (/10)'] > minOutlierAvgVote]
    df = df[df['Average Vote (/10)'] < maxOutlierAvgVote]
    df = df[df['Popularity'] > minOutlierPop]
    df = df[df['Popularity'] < maxOutlierPop]


    #remove rows with empty 
    df = df.dropna(axis=0, how='any')

    return df

def main():
    columnList = ['Title', 'Genre 1','Genre 2','Popularity','Runtime (minutes)','Average Vote (/10)']

    df = import_prepared_data()
    df = tidy_for_exploration(import_prepared_data())
    df = remove_outliers(df)

 #   for column in columnList:
 #       if type(df[column][1]) != str:
 #           basic_stats(df, column)
 #       else:
 #           pass

    x = df['Average Vote (/10)']
    y = df['Popularity']

    plt.scatter(x, y)
    plt.xlabel('Average Vote (/10)')
    plt.ylabel('Popularity')
    plt.show()
    pass

    
if __name__ == '__main__':
    main()


