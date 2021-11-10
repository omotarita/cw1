# Write code that prepares your 
import pandas as pd
import numpy as np
import requests, json, csv, os #Reference Tessa Xie from Towards Data Science (https://towardsdatascience.com/this-tutorial-will-make-your-api-data-pull-so-much-easier-9ab4c35f9af)


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



def remove_extras(deadColumns, result):
    """A function that removes the information we don't need: the rows containing null values and the unnecessary columns"""
    
    for i in deadColumns:
        if i in result:
            result = result.drop([i], axis = 1)

        else:
            pass

    result = result.dropna(axis=0, how='any')

    cleanData = result

    return cleanData



def write_to_csv(cleanDataList):
    """A function that concatenates this clean dataframe with our 'prepared_BFI.csv' file"""
    df = pd.concat(cleanDataList)
    df.to_csv("prepared_BFI.csv", index=False)

    pass



def remove_repeats():
    """A quality control function that removes all repeated data from a file"""
    df = pd.read_csv('prepared_BFI.csv', skiprows=0)
    df.drop_duplicates(inplace=True)

    df.to_csv('prepared_BFI.csv', index=False)
    pass



def concat_tmdb():
    """A function that pulls data from the TMDB API and merges it with data from our existing 'prepared_BFI.csv' file, then cleans it up"""
    
    #Read dataset as dataframe. Go through dataset and make a list of all the movie titles
    df = pd.read_csv('prepared_BFI.csv', skiprows=0)
    movieTitleList = []
    allMovieInfo = []
    n = 0

    for i in df.index:
        movieTitle = df['Title'][i]
        movieTitleList.insert(n, movieTitle)
        n=+1

    def search_and_query(movieTitle): #Reference Tessa Xie
        """Function to pull the movie query information"""
        movieFormatted = movieTitle.replace('  ', ' ') #Replace any double spaces with single spaces
        movieFormatted = movieFormatted.replace(' ', '+')
        query = f"https://api.themoviedb.org/3/search/movie?api_key=d84d20a84506bc77b4408e3a43fbba95&query={movieFormatted}"
        
        response =  requests.get(query)
        if response.status_code==200: 
            array = response.json()
            text = json.dumps(array)
            return (text)
        else:
            return ("error")

    def write_file_ID(text): #Reference Tessa Xie
        """Function to get the movie ID"""
        dataset = json.loads(text)
        """csvFile = open("prepared_complete_data.csv",'w')
        csvWriter = csv.writer(csvFile)"""

        try:
            movie_ID = dataset['results'][0]['id']
        except:
            movie_ID = None

        return movie_ID

    
    def get_details(movie_ID): #Reference Tessa Xie
        """Function to pull the movie details"""

        query = f"https://api.themoviedb.org/3/movie/{movie_ID}?api_key=d84d20a84506bc77b4408e3a43fbba95&language=en-US"
        response =  requests.get(query)
        if response.status_code==200: 
            array = response.json()
            details = json.dumps(array)
            return (details)
        else:
            return ("error")

    def write_file_details(details): #Reference Tessa Xie
        """Function to get the relevant details (id, genre, popularity, runtime, vote_average), then write them into a list beginning with the movie ID"""
       
        myMovieInfo = []

        dataset = json.loads(details)

        """csvFile = open("prepared_complete_data.csv",'w')
            csvWriter = csv.writer(csvFile)"""

        relevantDetails = ["original_title", "id", "genres", "popularity", "runtime", "vote_average"]
        n = 0
            
        for parameter in relevantDetails:
            if parameter != "genres":
                detail = dataset[parameter]
                myMovieInfo.insert(n, detail)
                n+=1
            elif parameter == "genres":
                result = dataset["genres"]
                for elem in result:
                    detail = elem["name"]
                    myMovieInfo.insert(n, detail)
                    n+=1
                    
                    if n>=4:
                        break
                    else:
                        continue

        return myMovieInfo

    step = 0
    dex = 0

    for movie in movieTitleList:
        movie_ID = write_file_ID(search_and_query(movieTitleList[dex]))
        try:
            myMovieInfo = write_file_details(get_details(movie_ID))
            allMovieInfo.insert(dex, myMovieInfo)
        except:
            pass
        dex+=1
        step+=1
        progress = (step/len(movieTitleList))*100
        if progress < 100:
            print(f"{progress:.2f}%", end = "\r")
        else:
            print(f"{progress}% - Done!")
        


    API_key = 'd84d20a84506bc77b4408e3a43fbba95' #For safekeeping

    df2 = pd.DataFrame (allMovieInfo, columns = ['Title', 'TMDB Movie ID', 'Genre 1', 'Genre 2', 'Popularity', 'Runtime (minutes)', 'Average Vote (/10)'])
    df1 = pd.read_csv('prepared_BFI.csv', skiprows=0)


    dfNew = pd.merge(df1, df2, on='Title')
    dfNew = dfNew.dropna(axis=0, how='any')

    dfNew.drop_duplicates(subset='Title', keep="first", inplace=True)

    dfNew.to_csv("prepared_complete_data.csv", index=False)
    pass



def main():

    filenames = ['2001_single_sheet.csv', '2002_single_sheet.csv', '2003_single_sheet.csv', '2004_single_sheet.csv', '2005_single_sheet.csv', '2006_single_sheet.csv']
    cleanDataList = []
    worksheetName = None

    n = 0
    deadColumns = ['Unnamed: 0', 'Gross', '% chg', 'Week #', 'Sites', 'Cum to date', 'Site Avg', 'Box office  to date', 'Box office to date', 'Unnamed: 8', 'Site avg']
    print("Getting started on the data...")

    for i in filenames:
        result = import_datasets(i, worksheetName)
        cleanData = remove_extras(deadColumns, result)
        cleanDataList.insert(n, cleanData)

    write_to_csv(cleanDataList)
    remove_repeats()

    concat_tmdb()

    pass

if __name__ == '__main__':
    main()


