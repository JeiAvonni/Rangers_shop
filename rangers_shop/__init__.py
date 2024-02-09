from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .helpers import JSONEncoder

# Internal exports
from config import Config
from .models import login_manager, db
from .blueprints.site.routes import site # Importing blueprint objects
from .blueprints.auth.routes import auth
from .blueprints.api.routes import api


#instantiate our Flask app
app = Flask(__name__) #Is passing in the name of our directory as the name of our app


# Going to tell our app class to look for configuration
app.config.from_object(Config)
jwt = JWTManager(app) # allows our app to use JWTMaanager from anywhere

# Wrap our whole app in pur login_manager so we can use it whenever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_id'
login_manager. login_message = 'Hey you! Login Please'
login_login_message_category = 'Warning'
#creating our first route using the @route decorator
#we are going to use a decorator to create our first route


app.register_blueprint(site) # Pass in site blueprint object to register
app.register_blueprint(auth)
app.register_blueprint(api)
# Instantiate our database & wrap our app in it
db.init_app(app)
migrate = Migrate(app, db) # Things we are connecying and migrating (our application to our database)
app.json_encoder = JSONEncoder # we are not instantiating this but rather poitning to this class 
cors = CORS(app) #Cross Origin Resource Sharing aka allowing other apps to talk to our API
