import pandas as pd

# user inputs movie with year in bracket
x = input("Enter the movie name:")
# reading and saving ratings
ratings = pd.read_csv('C:/Users/ABHI/Desktop/ratings.csv')
# reading and saving name and genre
movie_titles_genre = pd.read_csv("C:/Users/ABHI/Desktop/movies.csv")
# merging both the dfs
ratings = ratings.merge(movie_titles_genre, on='movieId', how='left')
# calculating and storing avg rating of a movie
Average_ratings = pd.DataFrame(ratings.groupby('title')['rating'].mean())
Average_ratings['Total Ratings'] = pd.DataFrame(ratings.groupby('title')['rating'].count())  #
movie_user = ratings.pivot_table(index='userId', columns='title', values='rating')
correlations = movie_user.corrwith(movie_user[f'{x}'])
recommendation = pd.DataFrame(correlations, columns=['Correlation'])
recommendation.dropna(inplace=True)
recommendation = recommendation.join(Average_ratings['Total Ratings'])
recc = recommendation[recommendation['Total Ratings'] > 100].sort_values('Correlation', ascending=False).reset_index()
recc = recc.merge(movie_titles_genre, on='title', how='left')
#print(correlations.head())
#print(recommendation.head())
print(recc.head(10))
