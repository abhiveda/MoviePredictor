import pandas as pd

# user inputs movie with year in bracket
movie = input("Enter the movie name")
rating = int(input("Enter your rating"))

# reading and saving ratings
ratings = pd.read_csv('C:/Users/ABHI/Desktop/ratings.csv')
# reading and saving name and genre
movie_titles_genre = pd.read_csv("C:/Users/ABHI/Desktop/movies.csv")
# merging both the dfs
ratings = pd.merge(movie_titles_genre, ratings).drop(['genres', 'timestamp'], axis=1)
# dropping columns
# print(data.head())
dataframe = ratings.pivot_table(index=['userId'], columns=['title'], values='rating')
# altering table shape
# print(dataframe.head())
dataframe = dataframe.dropna(thresh=10, axis=1).fillna(0)
# data cleaning
similarity_df = dataframe.corr(method="pearson")
# algo used


# print(similarity_df.head())


def get_similar(movie_name, user_rating):
    similar_score = similarity_df[movie_name] * (user_rating - 2.5)
    similar_score = similar_score.sort_values(ascending=False)
    return similar_score
# function used to get prediction

similar_prediction = pd.DataFrame()
similar_prediction = similar_prediction.append(get_similar(movie, rating), ignore_index=True)
# function call
# print(similar_prediction.head())
print(similar_prediction.sum().sort_values(ascending=False))
