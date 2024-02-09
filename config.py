# Our configuration file which configures the Flask app aka tells it all the specific details
# It needs to know about this specific app via variables

from datetime import timedelta
import os # Operatioon system, neccessary for python applications so python can be interpreted on any os

from dotenv import load_dotenv # Allows us to load our environment variables from a different file (so we can secure them)

# Establish our base directory so we can use "." In our app it knows that rangers_shop is our base dir
basedir = os.path.abspath(os.path.dirname(__file__))


#Establish where our environment variables are coming from
load_dotenv(os.path.join(basedir, '.env'))


# Create our Config class
class Config():

    """"
    Create Config class which will setup our configuration variable.
    Using environment variables where avai;ab;e otherwise create config variable.
    """

    FLASk_APP = os.environ.get('FLASK_APP') # Looking for key of FLASK_APP in .env file
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Literally can be whatever you want'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICACTIONS = False # We dont want a message every single time   
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)                                                                                     