import os

class config:
    #keys required by flask extensions
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #database
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smoucha:mumo@localhost/blog'


    #set email configurations
    


class ProdConfig(Config):

    pass

class DevConfig(Config):

    DEBUG=True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}