# Welcome to MovieRec4Parents!

#### This repo comtains a content-based movie recommender system for busy parents. In the root directory of this repo are notebooks 1-8 containing the code to scrape the data and make the files to get the system to run, and a folder called /lib containing a module called interface.py containing code necessary to allow users to use the system.

   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****

This system will not work unless a cosine similarity matrix is downloaded and put into the /data folder.  To get to the file click [here](https://drive.google.com/open?id=1MZv3t0YlG6VIQYRr5c0_e88stkJFFO1z).

   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****   **** WARNING ****

### Problem Statement:
#### Busy parents need a way to choose movies for their family that all members of the family will enjoy without exposing their children to objectionable material. Yet, every family has its own standards for determining what is or is not objectionable. Common Sense Media has a great website, but it takes precious time to page through all the movies at this site and glean all the valuable information.

#### To help parents solve this problem, MovieRec4Parents is a content-based recommender system that will produce a list of movies that are similar to a single movie entered by the user.  Below is a list of Jupyter notebooks with working code that you can visit if you so desire. Notebooks are located in the same folder as this README, or you can simply click on each individual notebook name.

    Common Sense Media's website scraped for movie review pages URL's.
[MovieRec4Parents1_GetURL's.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/1_GetURL's.ipynb)

    Individual movie pages scraped for both text and non-text data.
[MovieRec4Parents2_ScrapingMoviePages.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/2_ScrapingMoviePages.ipynb)

    Duplicated movies eliminated, features extracted and partially cleaned.
[MovieRec4Parents3_Extracting_Features.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/3_Extracting_Features.ipynb)

    Data cleaned, organized, and separated into text and non-text features.
[MovieRec4Parents4_Cleaning_and Organizing_Features.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/4_Cleaning_and_Organizing_Features.ipynb)

    Text features vectorized using TF-IDF and reduced by truncated SVD. Cosine similarity computed.
[MovieRec4Parents5.1_NLP-TF-IDF_Vectorizer.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/5.1_NLP-TF-IDF_Vectorizer.ipynb)

    Exploratory Data Analysis of non-text features. Relationship between features characterized.
[MovieRec4Parents6_EDA_of_Non-text_Features.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/6_EDA_of_Non-text_Features.ipynb)

    Functions for interface.py, a lib file allows notebook 8 to work.
[MovieRec4Parents7_Functions_for_Parents_Who_Have_More_Time.ipynb](https://github.com/Hadeishi/Capstone2/blob/master/7_Functions_for_Parents_Who_Have_More_Time.ipynb)

    A mostly blank notebook to be used as a user interface. Allows parents to get movie reviews.
[MovieRec4Parents8-User_Interface](https://github.com/Hadeishi/Capstone2/blob/master/8-User_Interface.ipynb)


In the process of running code in these notebooks, a number of data files are generated. Files are saved to the /data folder. Of these data files, three were larger than the 100MB file size limit imposed by GitHub and so were not uploaded to the site. Therefore, **this project will not work** unless you add at least one of these missing large data files. To get the system to work you will need to download a file called similarity_matrix_tfidfvec_truncSVD4000.pkl. The simplest way to access this file is to click on the following [link](https://drive.google.com/open?id=1kcyVzlulQJ8ViMBCOa_nRxBTA4IaoNBy) and move it into the /data folder. Alternatively, you could run the notebook that generates this pkl file, [MovieRec4Parents5.1](https://github.com/Hadeishi/Capstone2/blob/master/5.1_NLP-TF-IDF_Vectorizer.ipynb). If you'd like to see the code in action, you can run this folder after "uncommenting" the cells that have been commented out to avoid the possibility that necessary files are accidentally overwritten, thus breaking the recommender. If you really want to see the code in action updated so as to have all the latest movies reviewed by Common Sense Media, you could even run all of the notebooks sequentially. Be forewarned: the web scrape in the first notebook will take about 40 minutes, the scrape in the second will take about 2 and a half hours to complete, and assorted cells in other notebooks could each take several minutes or longer.

To view the Technical Report, please click [here](https://github.com/Hadeishi/Capstone2/blob/master/Technical.md).
> Written with [StackEdit](https://stackedit.io/).# Capstone2
