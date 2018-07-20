# Welcome to MovieRec4Parents!

## Executive Summary:

### Problem Statement:

Busy parents need a way to choose movies for their family that all members of the family will enjoy without exposing their children to objectionable material. Yet, every family has its own standards for determining what is or is not objectionable. Common Sense Media has a great website, but it takes precious time to page through all the movies at this site and glean all the valuable information.

To help parents solve this problem, MovieRec4Parents is a content-based recommender system that will produce a list of movies that are similar to a single movie entered by the user. Movie similarity is determined by comparing language used to describe the movies by Common Sense Media as described below (see [Notebook 5.1]https://github.com/Hadeishi/Capstone/blob/master/5.1_NLP-TF-IDF_Vectorizer.ipynb). If parents have a few minutes to answer several questions, MovieRec4Parents will filter this list of movies according to individual family standards. By doing so, parents will be provided with entertainment suggestions that the entire family will be able to enjoy.

Data was obtained by scraping https://www.commonsensemedia.org/movie-reviews and associated individual movie pages. A system_test function was built to assess the quality of recommendations but it has remained largely unutilized. Results of the system test and additional subjective analysis of recommendations shows about 80% accuracy of predictions. The kinds of errors the recommender makes are logical ones if you take into consideration the underlying method used by the recommender--- similar words in the associated text. Problems may be reduced or eliminated by restricting movie recommendations by filtering.

There are virtually no risks associated with using this recommender system. Parents are encouraged to double-check recommendations that are completely unfamiliar or seem "off." Parents can visit commonsensemedia.org to read movie descriptions in full or to double-check recommendations.


## Summary of Statistical Analysis:

Duplicate movies were discarded and movie data was extracted, cleaned, and separated into text and non-text data. Text data ("What's the Story?" and "What Parents Need to Know", etc.) was combined, tokenized and processed using Truncated SVD which Non-text data (parent ratings on a 0 to 5 scale on Sex, Violence, Educational Value, the MPAA rating, etc.). Text data was put through TF-IDF Vectorizer. TF-IDF gives the frequency of each word in the words associated with each movie (termed a "document") normalized by the frequency with which that word appears in all of the documents combined. In other words, words that appear frequently in text associated with all movies in general are not going to be counted as important as words that appear frequently in a small subset of documents.

The values assigned to each word after TF-IDF vectorization was examined to determine which words had the greatest influence on individual movie vectors. These can be viewed in Notebook 5.1. After vectorization, the number of features was reduced to 1000 components using truncated SVD. The word vectors that loaded onto these vectors were examined. A number of these components seemed to identify intuitive concepts (see [Notebook 5.1]https://github.com/Hadeishi/Capstone/blob/master/5.1_NLP-TF-IDF_Vectorizer.ipynb and the [google slide show]https://drive.google.com/open?id=15PWksQv20Jm-WssphfzZBZiurek8DNyz5BcoxmDmd2s for details).

These components were used to generate a cosine similarity matrix between individual movies. Cosine similarity is a procedure whereby movies whose associated text contains similar words will be described by vectors that "point in similar directions," if you will, through the vector space defined by truncatedSVD. Movies with vectors that point in similar directions will have higher cosine similarities and so are deemed similar to one another. Using 1000 components improved recommendations compared with 700, 2000, and 5000 components (data not shown), most likely by striking the right balance between leaving out important concepts and eliminating extraneous noise.

Non-text data included MPAA rating (G, PG, PG-13, R, NR, and NC-17), the minimum recommended age of viewership according to Common Sense Media, movie genre, and a group of ratings from 0 to 5 of various movie characteristics of  parental concern such as the amount of violence or sex in movies targeted at teens or the amount of 'violence and scariness' or 'sexy stuff' in movies targeted at younger kids. Graphs of exploratory data analysis of these data can be found in [Notebook 6]https://github.com/Hadeishi/Capstone/blob/master/6_EDA_of_Non-text_Features.ipynb. Generally, the movies on Common Sense Media's site can be divided into two sets of movies, those recommended for children younger than 9 and those recommended for tweens/teens and older. Consequently, two separate sets of questions were created depending upon the age of the children in the family. For instance, 80% of all movies--- typically those targetted at older children--- had no rating for 'educational value.' These movies were deemed to be different from those that had a zero for 'educational value,' so a boolean was created called is_educational to allow parents to restrict themselves to just a list of ostensibly educational movies. For more details, see [Notebook 6]https://github.com/Hadeishi/Capstone/blob/master/6_EDA_of_Non-text_Features.ipynb.

A user interface notebook was created to allow parents to enter either a single movie title or their answers to several questions to describing their family standards. Code for the functions to support this notebook are in a module called interface.py, also located in this repo. Backup copies of these functions are located in [Notebook 8]https://github.com/Hadeishi/Capstone/blob/master/8-User_Interface.ipynb.

#### Below is a list of Jupyter notebooks with working code that you can visit if you so desire. Notebooks are located in the same folder as this Technical Report. Below each notebook name is a brief description of what the code in each notebook does.

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

In the process of running code in these notebooks, a number of data files are generated (saved to the /data folder). Of these data files, three were larger than the 100MB file size limit imposed by GitHub and so were not uploaded to the site. Therefore, some of the functions **will not currently work**--- notably, the functions that generate movie recommendations themselves. To get this system to work, please download the necessary file (similarity_matrix_tfidfvec_truncSVD1000.pkl) by clicking on the following [link]https://drive.google.com/open?id=1MZv3t0YlG6VIQYRr5c0_e88stkJFFO1z. Alternative;ly, if you'd like to see the code in action, you can also run the notebooks sequentially. This will generate the correct intermediate files including the cosine similarity matrix necessary for a working project. If you wish to do so, you will have to "uncomment" the cells that have been commented out to avoid accidentally overwriting files and breaking the recommender. Be forewarned, though:  the web scrape in the first notebook will take about 40 minutes and the scrape in the second will take about 2 and a half hours to complete. Assorted other cells that take 10 minutes each have also been commented out for your convenience. This may break code further down in notebooks. The calculation of the cosine similarity matrix itself and several other steps may also take considerable time.

### Non-standard Packages and Libraries:

In writing the above code, I used the modules pandas, numpy, sklearn, matplotlib, seaborn, scipy.stats, nltk, fuzzywuzzy. I also imported time, math, random, requests, copy, re, json, csv, pickle, and BeautifulSoup. I also made a non-standard library called interface that is located in the lib folder, without which the last notebook above will not work.


> Written with [StackEdit](https://stackedit.io/).