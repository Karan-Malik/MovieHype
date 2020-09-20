from movie import app
from flask import render_template,flash
from movie.forms import MovieForm

@app.route('/',methods=['GET','POST'])
def movierec():
    form=MovieForm()
    if form.validate_on_submit():
        import pandas as pd
        import numpy as np

        ratings=pd.read_csv('ratings.csv')
        movies=pd.read_csv('movies.csv')

        movie_data=pd.merge(ratings,movies,on='movieId')

        movie_data.groupby('title')['rating'].mean().sort_values(ascending=False)

        movie_data.groupby('title')['rating'].count().sort_values(ascending=False)
        rating_mean=pd.DataFrame(movie_data.groupby('title')['rating'].mean())
        rating_mean['rating_count']=pd.DataFrame(movie_data.groupby('title')['rating'].count())

        user_movie_rating=movie_data.pivot_table(index='userId',columns='title',values='rating')

        x=form.moviename.data
        x=x.split()
        for i in range(0,len(x)):
            x[i]=x[i].capitalize()
        x=' '.join(x)

        flag=-1
        for i in range(0,len(movies)):
            if x in movies.iloc[i,1]:
                x=movies.iloc[i,1]
                flag=1
                
        if flag==-1:
            flash('There was some error. The admin has been notified. Please try another movie. Sorry for the inconvenience!!')
        else:
            movie=x
            movie_ratings=user_movie_rating[movie]

            movies_like_movie=user_movie_rating.corrwith(movie_ratings)
            corr_movie=pd.DataFrame(movies_like_movie,columns=['Correlation'])
            corr_movie.dropna(inplace=True)
            corr_movie=corr_movie.sort_values('Correlation',ascending=False)

            corr_movie=corr_movie.join(rating_mean['rating_count'])

            final=corr_movie[corr_movie['rating_count']>40].sort_values('Correlation',ascending=False)
            final=final.index
            for i in range(1,5):
                flash(final[i])
                
    return render_template('main.html',form=form)
