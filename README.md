# MovieHype
A Python based movie recommender hosted using Flask

## Overview
This movie recommender is made using Python3 and [pandas](https://pandas.pydata.org/), a powerful open source data analysis and manipulation tool and hosted on local server using [Flask](https://flask.palletsprojects.com/en/1.1.x/), a python web framework.
It uses a vast dataset of movies and their user reviews, to derive correlation between a user's rating of various movies. Generalising this correlation for all movies and users, it provides you with accurate and relevant recommendations, based on the movie entered.


![img](https://github.com/Karan-Malik/MovieHype/blob/master/Capture.PNG)

## Dataset
The dataset used consists of 100,000 ratings applied to 9,000 movies and is avaiable on the [Group Lens Website](https://grouplens.org/).This application uses the Small dataset available on the webiste.

You can access the dataset [here](https://grouplens.org/datasets/movielens/)

## How to Use

1. Clone this repository onto your system. On Command Prompt, run the following command:

```
git clone https://github.com/Karan-Malik/MovieHype
```
2. Change your directory to MovieHype:
```
cd MovieHype
```

3. Then run the follwing commands to run the application:
```
set FLASK_APP=movie.py
flask run
```

4. Enter the url provided after running the previous commands into your web browser


The movie recommender is now ready for use!

Enter the name of a movie and you will receive recommendations of similar movies. Click on the movie recommended to check out its reviews and ratings. 

Never run out of movies!!



##### To install flask follow this [link](https://flask.palletsprojects.com/en/1.1.x/installation/)

###### If application does not work after completing the previous steps, run it in a [virtual environment](https://djangocentral.com/how-to-a-create-virtual-environment-for-python/)




