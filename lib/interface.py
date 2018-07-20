import pandas as pd
import numpy as np
import scipy.stats as stats
import requests, json, csv, copy, pickle
import math
import random
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import process

# Load json of movies_features_text
with open('data/movies_features_text.json') as json_file:
    movies_features_text = json.load(json_file)

# Load csv of movies_processed_nontext_features.csv
df = pd.read_csv('data/movies_processed_nontext_features.csv')

#Load pkl of similarity_matrix_tfidfvec_truncSVD1000.pkl
with open('data/similarity_matrix_tfidfvec_truncSVD1000.pkl', 'rb') as f:
    similarity_matrix_tfidfvec_truncSVD1000 = pickle.load(f)

def title_recommender(movie_name, movie_list, limit=3):
    results = process.extract(movie_name, movie_list, limit=limit)
    return results

def find_similar_movies():
    movie_name = input("Give me a movie title and I'll give you five titles you might also like:")
    for title in df['title']:
        if title == movie_name:
            sim_movies_text = similarity_matrix_tfidfvec_truncSVD1000[movie_name]
            print("Thanks! Here are my recommendations, along with review text similarity scores:")
            recommendations = pd.DataFrame(sim_movies_text.sort_values(ascending=False)[1:6])
            return recommendations
    limit = 3
    while title != movie_name:
        results = title_recommender(movie_name, df['title'], limit=limit)
        print("Sorry, that movie title isn't in my list. Did you mean", results, "?")
        movie_name = input("(I need the exact title, please...)")
        for title in df['title']:
            if title == movie_name:
                sim_movies_text = similarity_matrix_tfidfvec_truncSVD1000[movie_name]
                print("Thanks! Here are my recommendations, along with review text similarity scores:")
                recommendations = pd.DataFrame(sim_movies_text.sort_values(ascending=False)[1:6])
                return recommendations
            else:
                limit += 1
                if limit >= 10:
                    limit = 10

def find_all_similar_movies():
    movie_name = input("Give me a movie title and I'll give you five titles you might also like:")
    for title in df['title']:
        if title == movie_name:
            sim_movies_text = similarity_matrix_tfidfvec_truncSVD1000[movie_name]
            print("Thanks! Here are my recommendations, along with review text similarity scores:")
            recommendations = pd.DataFrame(sim_movies_text.sort_values(ascending=False)[1:8000])
            return recommendations
    limit = 3
    while title != movie_name:
        results = title_recommender(movie_name, df['title'], limit=limit)
        print("Sorry, that movie title isn't in my list. Did you mean", results, "?")
        movie_name = input("(I need the exact title, please...)")
        for title in df['title']:
            if title == movie_name:
                sim_movies_text = similarity_matrix_tfidfvec_truncSVD1000[movie_name]
                print("Thanks! Here are my movie recommendations:")
                recommendations = pd.DataFrame(sim_movies_text.sort_values(ascending=False)[1:8000])
                return recommendations
            else:
                limit += 1
                if limit >= 10:
                    limit = 10

def filter_movies_for_youngsters(parent_ratings, rec_movie_names, df):
    '''
    Will take in parent ratings, the indicies of recommended movies based on the single
    movie selection by the parent, and a df that contains nontext features of movies
    that are exclusively for youngsters (created by dropping all but movies that have
    a rating for Sexy Stuff, the most restrictive such screening variable). Function
    will filter the movie list according to family standards described by parents and
    generate the top 5 movies that meet parent expectations.
    '''
    _, wants_educational, prate_sexy_stuff, prate_violence_scariness, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_genre, prate_MPAA_rating = parent_ratings
    recs_filtered = []
    if wants_educational == 'y':
        want_educ = 1
    else:
        want_educ = 0

    movie_nums = get_index_nums(rec_movie_names)
    if len(movie_nums) == 0:
        print("Sorry, not enough movies in my list met your conditions. I recommend Toy Story!")
        return(4279)
    num_recs_filtered = []
    for num in movie_nums:
        if df.loc[num, 'is_educational'] == want_educ and df.loc[num, 'Sexy Stuff'] <= int(prate_sexy_stuff) and df.loc[num, 'Violence & Scariness'] <= int(prate_violence_scariness) and df.loc[num, 'Consumerism'] <= int(prate_consumerism) and df.loc[num, 'Drinking, Drugs & Smoking'] <= int(prate_drinking_drugs_smoking) and df.loc[num, 'Language'] <= int(prate_language) and df.loc[num, 'Positive Messages'] >= int(prate_positive_messages) and df.loc[num, 'genre'] == prate_genre and df.loc[num, 'MPAA_ordinal'] <= prate_MPAA_rating:
            num_recs_filtered.append(num)
        if len(num_recs_filtered) == 5:
            break
    if len(num_recs_filtered) < 5:
        print("Sorry, not enough movies in my list met your conditions. I recommend Toy Story!")
        return(4279)
    if len(num_recs_filtered) > 0:
        print("Here are your recommended movies:")
    recs_filtered = movie_nums_to_movies(num_recs_filtered)

    return recs_filtered

def filter_movies_for_tweens(parent_ratings, rec_movie_names, df):
    '''
    Will take in parent ratings, the indicies of recommended movies based on the single
    movie selection by the parent, and a df that contains nontext features of movies
    that are exclusively for youngsters (created by dropping all but movies that have
    a rating for Violence & Scariness, the most inclusive such screening variable). Function
    will filter the movie list according to family standards described by parents and
    generate the top 5 movies that meet parent expectations.
    '''
    _, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_sex, prate_violence, prate_genre, prate_MPAA_rating = parent_ratings

    movie_nums = get_index_nums(rec_movie_names)
    if len(movie_nums) == 0:
        print("Sorry, not enough movies in my list met your conditions. I recommend Back to the Future!")
        return(6357)
    num_recs_filtered = []
    for num in movie_nums:
        if df.loc[num, 'Consumerism'] <= int(prate_consumerism) and df.loc[num, 'Drinking, Drugs & Smoking'] <= int(prate_drinking_drugs_smoking) and df.loc[num, 'Language'] <= int(prate_language) and df.loc[num, 'Positive Messages'] >= int(prate_positive_messages) and df.loc[num, 'Sex'] >= int(prate_sex) and df.loc[num, 'Violence'] >= int(prate_violence) and df.loc[num, 'genre'] == prate_genre and df.loc[num, 'MPAA_ordinal'] <= prate_MPAA_rating:
            num_recs_filtered.append(num)
        if len(num_recs_filtered) == 5:
            break
    if len(num_recs_filtered) < 5:
        print("Sorry, not enough movies in my list met your conditions. I recommend Back to the Future!")
        return(6357)
    if len(num_recs_filtered) > 0:
        print("Here are your recommended movies:")
    recs_filtered = movie_nums_to_movies(num_recs_filtered)

    return recs_filtered

def get_index_nums(movie_titles):
    movie_nums = []
    for name in movie_titles:
        movie_nums.append(df.title[df.title==name].index.tolist()[0])
    return(movie_nums)

def movie_nums_to_movies(movie_nums):
    movie_names = [df['title'][num] for num in movie_nums]
    return(movie_names)

def system_test(trials):
    rate_recs = []
    for trial in reversed(range(trials)):
        print("Thank you for trying out MovieRec4Parents(tm)! You have", trial+1, "tries to go.")
        recommendations = find_similar_movies()
        print(recommendations)
        rate_recs.append(recommendations)
        for rec in range(len(recommendations)):
            print("On a scale of 1-5, how good is recommendation", rec+1,"? If you don't know the movie, enter 0.)")
            rating = input()
            rate_recs.append((trial, rec+1, rating))
    print("You're done! I hope you enjoyed using MovieRec4Parents(tm). Tell your friends!")
    return rate_recs

def get_parent_ratings_first():
    print("Welcome to MovieRec4Parents! Let me ask you a few questions before we begin.")
    num_children, children_ages = get_num_children_and_ages()
    youngsters = age_checker(children_ages)
    if youngsters == 1:
        wants_educational, prate_sexy_stuff, prate_violence_scariness, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_genre, prate_MPAA_rating = get_parent_ratings_youngsters()
        parent_ratings = youngsters, wants_educational, prate_sexy_stuff, prate_violence_scariness, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_genre, prate_MPAA_rating

    else:
        prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_sex, prate_violence, prate_genre, prate_MPAA_rating = get_parent_ratings_tweens()
        parent_ratings = youngsters, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_sex, prate_violence, prate_genre, prate_MPAA_rating
    movie_all_recs = find_all_similar_movies()
    movie_names = movie_all_recs.index
    if youngsters == 1:
        movie_recs = filter_movies_for_youngsters(parent_ratings, movie_names, df)
        return movie_recs
    else:
        movie_recs = filter_movies_for_tweens(parent_ratings, movie_names, df)
        return movie_recs

def get_parent_ratings_youngsters():
    print("I have just 9 more questions for you. Respond with a ? if you'd like some examples.")
    wants_educational = get_wants_educational()
    prate_sexy_stuff = get_prate_sexy_stuff()
    prate_violence_scariness = get_prate_violence_scariness()
    prate_consumerism = get_prate_consumerism()
    prate_drinking_drugs_smoking = get_prate_drinking_drugs_smoking()
    prate_language = get_prate_language()
    prate_positive_messages = get_prate_positive_messages()
    prate_genre = get_prate_genre()
    prate_MPAA_rating = get_prate_MPAA_rating()
    print("Thank you!")

    return wants_educational, prate_sexy_stuff, prate_violence_scariness, prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_genre, prate_MPAA_rating

def get_parent_ratings_tweens():
    print("I have just 8 more questions for you. Respond with a ? if you'd like some examples.")
    prate_consumerism = get_prate_consumerism()
    prate_drinking_drugs_smoking = get_prate_drinking_drugs_smoking()
    prate_language = get_prate_language()
    prate_positive_messages = get_prate_positive_messages()
    prate_sex = get_prate_sex()
    prate_violence = get_prate_violence()
    prate_genre = get_prate_genre()
    prate_MPAA_rating = get_prate_MPAA_rating()
    print("Thank you!")

    return prate_consumerism, prate_drinking_drugs_smoking, prate_language, prate_positive_messages, prate_sex, prate_violence, prate_genre, prate_MPAA_rating

def get_num_children_and_ages():
    num_children = input("How many children do you have?")
    child = 0
    children_ages = []
    while child < int(num_children):
        print("How old is your child", child + 1, "?")
        child_age = input()
        children_ages.append(float(child_age))
        child += 1
    print("Thank you!")
    return int(num_children), children_ages

def age_checker(children_ages):
    youngsters = 0
    for age in children_ages:
        if age <= 8:
            youngsters = 1
    return youngsters

def get_wants_educational():
    wants_educational = []
    print("Do you want to see an educational movie?")
    while True:
        wants_educational = input("Please enter y, n, or ?")
        if (wants_educational == '?' or
            wants_educational == 'y' or
            wants_educational == 'n'):
            if wants_educational == '?':
                print("An example of an \'educational movie\' is", df[df['Educational Value']==3]['title'].iloc[random.randint(0,len(df[df['Educational Value']==3])-1)])
                print("An example of a non-educational movie is", df[df['Educational Value']==0]['title'].iloc[random.randint(0,len(df[df['Educational Value']==0])-1)])
            else:
                return wants_educational

def get_prate_sexy_stuff():
    prate_sexy_stuff = []
    print("What amount of \"sexy stuff\" is okay for your kids, on a scale of 0 to 3?)")
    while True:
        prate_sexy_stuff = input("Please enter 0, 1, 2, 3, or ?")
        if (prate_sexy_stuff == '?' or
            prate_sexy_stuff == '0' or
            prate_sexy_stuff == '1' or
            prate_sexy_stuff == '2' or
            prate_sexy_stuff == '3'):
            if prate_sexy_stuff == '?':
                print("An example of a 0 is", df[df['Sexy Stuff']==0]['title'].iloc[random.randint(0, len(df[df['Sexy Stuff']==0])-1)])
                print("An example of a 3 is", df[df['Sexy Stuff']==3]['title'].iloc[random.randint(0, len(df[df['Sexy Stuff']==3])-1)])
                print("(There are no movies rated higher than a 3 for Sexy Stuff...)")
            else:
                return prate_sexy_stuff

def get_prate_violence_scariness():
    prate_violence_scariness = []
    print("What level of violence and cartoon scariness is okay for your kids? (0 to 4)")
    while True:
        prate_violence_scariness = input("Please enter 0, 1, 2, 3, 4, or ?")
        if (prate_violence_scariness == '?' or
            prate_violence_scariness == '0' or
            prate_violence_scariness == '1' or
            prate_violence_scariness == '2' or
            prate_violence_scariness == '3' or
            prate_violence_scariness == '4'):
            if prate_violence_scariness == '?':
                print("An example of a 0 is", df[df['Violence & Scariness']==0]['title'].iloc[random.randint(0, len(df[df['Violence & Scariness']==0])-1)])
                print("An example of a 2 is", df[df['Violence & Scariness']==2]['title'].iloc[random.randint(0, len(df[df['Violence & Scariness']==2])-1)])
                print("An example of a 4 is", df[df['Violence & Scariness']==4]['title'].iloc[random.randint(0, len(df[df['Violence & Scariness']==4])-1)])
                print("(There are no movies with a 5 rating for Violence & Scariness...)")
            else:
                return prate_violence_scariness

def get_prate_consumerism():
    prate_consumerism = []
    print("What level of exposure to consumerism is okay for your kids? (0 to 5)")
    while True:
        prate_consumerism = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_consumerism == '?' or
            prate_consumerism == '0' or
            prate_consumerism == '1' or
            prate_consumerism == '2' or
            prate_consumerism == '3' or
            prate_consumerism == '4' or
            prate_consumerism == '5'):
            if prate_consumerism == '?':
                print("An example of a 0 is", df[df['Consumerism']==0]['title'].iloc[random.randint(0, len(df[df['Consumerism']==0])-1)])
                print("An example of a 3 is", df[df['Consumerism']==3]['title'].iloc[random.randint(0, len(df[df['Consumerism']==3])-1)])
                print("An example of a 5 is", df[df['Consumerism']==5]['title'].iloc[random.randint(0, len(df[df['Consumerism']==5])-1)])
            else:
                return prate_consumerism

def get_prate_drinking_drugs_smoking():
    prate_drinking_drugs_smoking = []
    print("What level of drinking, drugs, & smoking is okay for your kids? (0 to 5)")
    while True:
        prate_drinking_drugs_smoking = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_drinking_drugs_smoking == '?' or
            prate_drinking_drugs_smoking == '0' or
            prate_drinking_drugs_smoking == '1' or
            prate_drinking_drugs_smoking == '2' or
            prate_drinking_drugs_smoking == '3' or
            prate_drinking_drugs_smoking == '4' or
            prate_drinking_drugs_smoking == '5'):
            if prate_drinking_drugs_smoking == '?':
                print("An example of a 0 is", df[df['Drinking, Drugs & Smoking']==0]['title'].iloc[random.randint(0, len(df[df['Drinking, Drugs & Smoking']==0])-1)])
                print("An example of a 3 is", df[df['Drinking, Drugs & Smoking']==3]['title'].iloc[random.randint(0, len(df[df['Drinking, Drugs & Smoking']==3])-1)])
                print("An example of a 5 is", df[df['Drinking, Drugs & Smoking']==5]['title'].iloc[random.randint(0, len(df[df['Drinking, Drugs & Smoking']==5])-1)])
            else:
                return prate_drinking_drugs_smoking

def get_prate_language():
    prate_language = []
    print("What level of exposure to bad language is okay for your kids? (0 to 5)")
    while True:
        prate_language = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_language == '?' or
            prate_language == '0' or
            prate_language == '1' or
            prate_language == '2' or
            prate_language == '3' or
            prate_language == '4' or
            prate_language == '5'):
            if prate_language == '?':
                print("An example of a 0 is", df[df['Language']==0]['title'].iloc[random.randint(0, len(df[df['Language']==0])-1)])
                print("An example of a 3 is", df[df['Language']==3]['title'].iloc[random.randint(0, len(df[df['Language']==3])-1)])
                print("An example of a 5 is", df[df['Language']==5]['title'].iloc[random.randint(0, len(df[df['Language']==5])-1)])
            else:
                return prate_language

def get_prate_positive_messages():
    prate_positive_messages = []
    print("How important are positive messages in movies to you and kids? (0 to 5)")
    while True:
        prate_positive_messages = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_positive_messages == '?' or
            prate_positive_messages == '0' or
            prate_positive_messages == '1' or
            prate_positive_messages == '2' or
            prate_positive_messages == '3' or
            prate_positive_messages == '4' or
            prate_positive_messages == '5'):
            if prate_positive_messages == '?':
                print("An example of a 0 is", df[df['Positive Messages']==0]['title'].iloc[random.randint(0, len(df[df['Positive Messages']==0])-1)])
                print("An example of a 3 is", df[df['Positive Messages']==3]['title'].iloc[random.randint(0, len(df[df['Positive Messages']==3])-1)])
                print("An example of a 5 is", df[df['Positive Messages']==5]['title'].iloc[random.randint(0, len(df[df['Positive Messages']==5])-1)])
            else:
                return prate_positive_messages

def get_prate_sex():
    prate_sex = []
    print("What degree of exposure to sex in movies is okay for your kids? (0 to 5)")
    while True:
        prate_sex = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_sex == '?' or
            prate_sex == '0' or
            prate_sex == '1' or
            prate_sex == '2' or
            prate_sex == '3' or
            prate_sex == '4' or
            prate_sex == '5'):
            if prate_sex == '?':
                print("An example of a 0 is", df[df['Sex']==0]['title'].iloc[random.randint(0, len(df[df['Sex']==0])-1)])
                print("An example of a 3 is", df[df['Sex']==3]['title'].iloc[random.randint(0, len(df[df['Sex']==3])-1)])
                print("An example of a 5 is", df[df['Sex']==5]['title'].iloc[random.randint(0, len(df[df['Sex']==5])-1)])
            else:
                return prate_sex

def get_prate_violence():
    prate_violence = []
    print("What level of movie violence is okay for your kids (0 to 5)")
    while True:
        prate_violence = input("Please enter 0, 1, 2, 3, 4, 5, or ?")
        if (prate_violence == '?' or
            prate_violence == '0' or
            prate_violence == '1' or
            prate_violence == '2' or
            prate_violence == '3' or
            prate_violence == '4' or
            prate_violence == '5'):
            if prate_violence == '?':
                print("An example of a 0 is", df[df['Violence']==0]['title'].iloc[random.randint(0, len(df[df['Violence']==0])-1)])
                print("An example of a 3 is", df[df['Violence']==3]['title'].iloc[random.randint(0, len(df[df['Violence']==3])-1)])
                print("An example of a 5 is", df[df['Violence']==5]['title'].iloc[random.randint(0, len(df[df['Violence']==5])-1)])
            else:
                return prate_violence

def get_prate_genre():
    prate_genre = []
    print("What genre of movie would you like to see?")
    while True:
        print("Please enter Drama, Family and Kids, Comedy, Action/Adventure, Documentary, Thriller,")
        prate_genre = input("Horror, Science Fiction, Fantasy, Romance, Musical, Classic, Western, or ?")
        if (prate_genre == '?' or
            prate_genre == 'Drama' or
            prate_genre == 'Family and Kids' or
            prate_genre == 'Comedy' or
            prate_genre == 'Action/Adventure' or
            prate_genre == 'Documentary' or
            prate_genre == 'Thriller' or
            prate_genre == 'Horror' or
            prate_genre == 'Science Fiction' or
            prate_genre == 'Fantasy' or
            prate_genre == 'Romance' or
            prate_genre == 'Musical' or
            prate_genre == 'Classic' or
            prate_genre == 'Western'):
            if prate_genre == '?':
                print("An example of a Drama is", df[df['genre']=='Drama']['title'].iloc[random.randint(0, len(df[df['genre']=='Drama'])-1)])
                print("An example of a Family and Kids movie is", df[df['genre']=='Family and Kids']['title'].iloc[random.randint(0, len(df[df['genre']=='Family and Kids'])-1)])
                print("An example of a Comedy is", df[df['genre']=='Comedy']['title'].iloc[random.randint(0, len(df[df['genre']=='Comedy'])-1)])
                print("An example of an Action/Adventure movie is", df[df['genre']=='Action/Adventure']['title'].iloc[random.randint(0, len(df[df['genre']=='Action/Adventure'])-1)])
                print("An example of a Documentary is", df[df['genre']=='Documentary']['title'].iloc[random.randint(0, len(df[df['genre']=='Documentary'])-1)])
                print("An example of a Thriller is", df[df['genre']=='Thriller']['title'].iloc[random.randint(0, len(df[df['genre']=='Thriller'])-1)])
                print("An example of a Horror movie is", df[df['genre']=='Horror']['title'].iloc[random.randint(0, len(df[df['genre']=='Horror'])-1)])
                print("An example of a Science Fiction movie is", df[df['genre']=='Science Fiction']['title'].iloc[random.randint(0, len(df[df['genre']=='Science Fiction'])-1)])
                print("An example of a Fantasy movie is", df[df['genre']=='Fantasy']['title'].iloc[random.randint(0, len(df[df['genre']=='Fantasy'])-1)])
                print("An example of a Romance is", df[df['genre']=='Romance']['title'].iloc[random.randint(0, len(df[df['genre']=='Romance'])-1)])
                print("An example of a Musical is", df[df['genre']=='Musical']['title'].iloc[random.randint(0, len(df[df['genre']=='Musical'])-1)])
                print("An example of a Classic film is", df[df['genre']=='Classic']['title'].iloc[random.randint(0, len(df[df['genre']=='Classic'])-1)])
                print("An example of a Western is", df[df['genre']=='Western']['title'].iloc[random.randint(0, len(df[df['genre']=='Western'])-1)])
            else:
                return prate_genre

def get_prate_MPAA_rating():
    prate_MPAA_rating = []
    print("Finally, what MPAA rating is the most extreme MPAA Rating for your kids (G, PG, PG-13, R, NR (not rated), or NC-17?)")
    while True:
        prate_MPAA_rating = input("Please enter G, PG, PG-13, R, NR (not rated), NC-17, or ?")
        print(prate_MPAA_rating)
        if (prate_MPAA_rating == '?' or
            prate_MPAA_rating == 'G' or
            prate_MPAA_rating == 'PG' or
            prate_MPAA_rating == 'PG-13' or
            prate_MPAA_rating == 'R' or
            prate_MPAA_rating == 'NR' or
            prate_MPAA_rating == 'NC-17'):
            if prate_MPAA_rating == 'G':
                prate_MPAA_rating = 0
            if prate_MPAA_rating == 'PG':
                prate_MPAA_rating = 1
            if prate_MPAA_rating == 'PG-13':
                prate_MPAA_rating = 2
            if prate_MPAA_rating == 'R':
                prate_MPAA_rating = 3
            if prate_MPAA_rating == 'NR':
                prate_MPAA_rating = 4
            if prate_MPAA_rating == 'NC-17':
                prate_MPAA_rating = 5
            if prate_MPAA_rating == '?':
                print("An example of a G rated movie is", df[df['MPAA_rating']=='G']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='G'])-1)])
                print("An example of a PG rated movie is", df[df['MPAA_rating']=='PG']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='PG'])-1)])
                print("An example of a PG-13 rated movie is", df[df['MPAA_rating']=='PG-13']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='PG-13'])-1)])
                print("An example of an R rated movie is", df[df['MPAA_rating']=='R']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='R'])-1)])
                print("An example of an NR rated movie is", df[df['MPAA_rating']=='NR']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='NR'])-1)])
                print("An example of an NC-17 rated movie is", df[df['MPAA_rating']=='NC-17']['title'].iloc[random.randint(0, len(df[df['MPAA_rating']=='NC-17'])-1)])
            else:
                return prate_MPAA_rating
