# COMP0035 Coursework 1 



## Select a project methodology

The success of any project, from the simplest problem-solving exercises to the most complex endeavours, is underpinned by the methods used in carrying it out. For this reason, project management has emerged as an up and coming high demand work industry. The most successful teams and businesses value project management and methodology considerations as an unmissable first step to any project undertaking.

Software engineering and data science projects are usually fairly complex and often involve lots of moving parts and dozens of team members all working towards one shared goal. In order to best align these stakeholders, an appropriate project methodology must be chosen and subsequently followed by everyone involved. And in order to do that, the team's project manager (usually someone who has expert knowledge of the target domain, as well as project management experience) must analyse and carefully consider a project's requirements against the strengths of a number of existing project methodologies.

For this project, our team will be working with a dataset from the BFI, to address the following problem statement:
> *The excessive amount of time it takes to pick what movies to watch often results in viewers wasting the majority of their leisure time by spending it looking for something to watch.*


The **Data-driven Scrum** method (an Agile framework optimised for data science teams which integrates elements of Scrum and Kanban) stands out as the most suitable methodology for the project at hand. Given my experience using Scrum in numerous projects undertaken during internships and summer work in the past, I'm highly familiar with the way it works and felt that it permits the iteration and flexibility this project might need due to its short timeframe and its inherent volatility (due to the ever-changing climate of the film industry). The Data-driven Scrum method permits all the benefits of the traditional Scrum method, but with some added functionality:

1. **Variable length duration**: allows more flexibility for teams who mispredict the duration of certain tasks. The traditional Scrum method has fixed sprint lengths
2. **Reviews on an As and When basis**: project retrospectives and item reviews happen as frequently as the team would like, as opposed to happening at the end of each iteration like in traditional Scrum
3. **Collective analysis**: the entire project team contributes to any hypothesis analysis efforts - the onus doesn't fall solely on the product owner to analyse ideas which means this analysis can benefit from team members' aggregate technical expertise.



## Defining the Business Need

In order to define the business need, given the fact that my dataset quantifies information to do with the film industry, I decided to first think about my needs and wants, as a movie-viewer.

Although I am an avid cinemagoer, my most common avenue for filmwatching is through online streaming platforms; specifically Netflix. The platform does a great job at simplifying the movie-viewing experience by providing viewers with everything they need from the comfort of their home. However, all of the benefits Netflix offers end up going to waste when a viewer is left stumped in the process of choosing a movie. This phenomenon, termed "choice fatigue" by the Wall Street Journal, is widespread across the internet community; as such, it provides a huge gap for new business development.


### Problem Statement

Netflix recently delivered a new feature "Play Something" which aims to address this issue. However it doesn't take any user input (such as questions like "movie or TV show?", "what genre?") into consideration before making a choice. This means there's an extremely high probability that the choice made by Netflix won't be something the viewer wants to watch, meaning their choice fatigue will be left unalleviated. I believe the following problem statement clearly elaborates the problem at hand, which will permit the development of a more effective solution to address it:

> *The excessive amount of time it takes to pick what movies to watch often results in viewers wasting the majority of their leisure time by spending it looking for something to watch.*


### Target Audience

As this problem is widespread across Netflix users, our target audience should align closely with that of the platform. According to the Consumer & Media View Survey carried out by Nielsen in 2015, approximately 89% of Netflix users are young adults (aged 18-24), with a large skew aged between 25-39.

The following user persona exemplifies the target audience further:

[see persona_image.png]


### The Product Solution

To address this problem, I suggest a solution which requests the user input of their movie genre preferences and time they have set aside for watching and returns a list of movies to match. However, if a user is really stumped for choice and has no genre preferences nor time limit, the app will show them a data visualisation highlighting the genres they are most likely to find entertaining and prompt them again for their genre preferences. In response, users can either select one of these genres and be shown a list of movies that match or they can decline to choose (by pressing the "Choose for me" button); in this case, the web-app would make a random selection of movies and visualise their entertainment value.

In line with our target audience's preference for internet streaming, the solution should come in the form of a web-app to maintain the same level of convenience Netflix users are used to in their streaming experience.

To ensure the solution is effective at solving the problem at hand, I suggest focusing on addressing the following data-focused questions. In brackets I also describe the statistical processes that could be used to solve each of these questions, using our data:

- *What combination of movies is the most entertaining to a user given specific preferences (their preferred genres & the ideal maximum length of marathon)?* - **Recommendation**
- *Is there a correlation between movie genre and movie popularity? What are the most popular movie genres?* - **Regression**
- *What are the most popular movies within each genre?* - **Regression**
- *Which movies fit into the category of the genres they'd like to watch?* - **Classification**
- *How many movies of this genre can they fit into their allotted marathon time?* - **Summation**



## Data exploration and preparation

For this project, I've been working with two datasets: 

1. **The British Film Institute (BFI) data** which provides a report on the top 15 most popular movies at the Box Office, their gross box office revenue and some related statistics (e.g. how many weeks they've spent on the Box Office charts, their cumulative revenue etc.)
2. **The Movie Database (TMDB) data** which is an enormous community-built database containing an extensive set of data on almost 1 million movies. For developers, any data you need from TMDB can be requested using their API. 


### Steps

To format their data, filter out irrelevant datapoints and merge these two datasets, I wrote a [data preparation script](data_preparation.py). Here's a breakdown of the steps I followed to write the code, and consequently prepare my data for exploration.

- I started off my downloading the 2001 to 2006 BFI xlsx files from their [website](https://www.bfi.org.uk/industry-data-insights/weekend-box-office-figures) and uploading them to my Google Drive. The files were formatted such that they had their data broken up into different worksheets for every month. I manually imported each worksheet into the first, leaving me with one worksheet per file which contained all the data for the year. 

- I downloaded all 6 files as csv's and moved them to my Coursework 1 folder, the current directory. The files are named as follows: [2001_single_sheet.csv](2001_single_sheet.csv), [2002_single_sheet.csv](2002_single_sheet.csv), [2003_single_sheet.csv](2003_single_sheet.csv), [2004_single_sheet.csv](2004_single_sheet.csv), [2005_single_sheet.csv](2005_single_sheet.csv), [2006_single_sheet.csv](2006_single_sheet.csv),
