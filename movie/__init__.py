from flask import Flask
from movieconfig import Config

app=Flask(__name__)
app.config.from_object  (Config)



from movie import routes
