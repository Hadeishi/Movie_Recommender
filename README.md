# Welcome to MovieRec4Parents!

#### This repo comtains a content-based movie recommender system for busy parents. In the root directory of this repo are notebooks 1-8 containing the code to scrape the data and make the files to get the system to run, and a folder called /lib containing a module called interface.py containing code necessary to allow users to use the system.

   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****

This system will not work unless a cosine similarity matrix is downloaded and put into the /data folder.  To get to the file click [here]https://drive.google.com/open?id=1MZv3t0YlG6VIQYRr5c0_e88stkJFFO1z.

   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****

### Problem Statement:
#### Busy parents need a way to choose movies for their family that all members of the family will enjoy without exposing their children to objectionable material. Yet, every family has its own standards for determining what is or is not objectionable. Common Sense Media has a great website, but it takes precious time to page through all the movies at this site and glean all the valuable information.

#### To help parents solve this problem, MovieRec4Parents is a content-based recommender system that will produce a list of movies that are similar to a single movie entered by the user.  Below is a list of Jupyter notebooks with working code that you can visit if you so desire. Notebooks are located in the same folder as this README, or you can simply click on each individual notebook name.

[MovieRec4Parents1_GetURL's.ipynb]https://github.com/Hadeishi/Capstone/blob/master/1_GetURL's.ipynb

    Scrape Common Sense Media's website for movie review pages for URL's.
[MovieRec4Parents2_ScrapingMoviePages.ipynb]https://github.com/Hadeishi/Capstone/blob/master/2_ScrapingMoviePages.ipynb

    Scrape individual movie pages for text and non-text data.
[MovieRec4Parents3_Extracting_Features.ipynb]https://github.com/Hadeishi/Capstone/blob/master/3_Extracting_Features.ipynb

    Eliminate duplicate movies, extract features and preliminary data cleaning.
[MovieRec4Parents4_Cleaning_and Organizing_Features.ipynb]https://github.com/Hadeishi/Capstone/blob/master/4_Cleaning_and_Organizing_Features.ipynb

    Data cleaned, organized, and separated into text and non-text features.
[MovieRec4Parents5.1_NLP-TF-IDF_Vectorizer.ipynb]https://github.com/Hadeishi/Capstone/blob/master/5.1_NLP-TF-IDF_Vectorizer.ipynb

    Text features vectorized using TF-IDF and reduced by truncated SVD. Cosine similarity computed.
[MovieRec4Parents6_EDA_of_Non-text_Features.ipynb]https://github.com/Hadeishi/Capstone/blob/master/6_EDA_of_Non-text_Features.ipynb

    Exploratory Data Analysis of non-text features. Relationship between features characterized.
[MovieRec4Parents7_Functions_for_Parents_Who_Have_More_Time.ipynb]https://github.com/Hadeishi/Capstone/blob/master/7_Functions_for_Parents_Who_Have_More_Time.ipynb

    Functions for interface.py, a lib file to allow parents to interface with functions from clean notebook.
[MovieRec4Parents8-User_Interface]https://github.com/Hadeishi/Capstone/blob/master/8-User_Interface.ipynb

    Notebook to allow parents to run simple commands without having to see the underlying code. Have parents use this notebook to generate recommendations.

In the process of running code in these notebooks, a number of data files are generated. Files are saved to the /data folder. Of these data files, three were larger than the 100MB file size limit imposed by GitHub and so were not uploaded to the site. Therefore, some of the functions **will not currently work**--- notably, the functions that generate movie recommendations themselves. To get the system to work you will need to download a file called similarity_matrix_tfidfvec_truncSVD1000.pkl. To access this file, click on the following [link]https://drive.google.com/open?id=1MZv3t0YlG6VIQYRr5c0_e88stkJFFO1z and save it to the /data folder. Alternatively, you can run the folder that generates this pkl file. If you'd like to see the code in action, you can also just run all of the notebooks sequentially. This will generate the correct intermediate files including the cosine similarity matrix necessary for a working project. If you wish to do so, you will have to "uncomment" the cells that have been commented out to avoid accidentally overwriting files and breaking the recommender. Be forewarned, though, the web scrape in the first notebook will take about 40 minutes, the scrape in the second will take about 2 and a half hours to complete, and assorted cells in other notebooks could eachg take several minutes or longer. These cells have been mostly commented out for your convenience. Incomplete running of the code in these notebooks could break code further down.

To view the Technical Report, please click [here]https://github.com/Hadeishi/Capstone/blob/master/Technical.md.
> Written with [StackEdit](https://stackedit.io/).# Capstone2
