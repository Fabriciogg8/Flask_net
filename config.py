
class Config(object):   
    DEBUG = False
    TESTING = False
    
    SECRET_KEY = "Super_secret_nobody_knows_key"
    
    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "Fabricio/Programacion/Flask/Scocial_net/static/img"
    
    SESSION_COOKIE_SECURE = True


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):   
    DEBUG = True

    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "Fabricio/Programacion/static/img"
    
    SESSION_COOKIE_SECURE = False

class TestingConfig(Config):
    TESTING = True
    
    DB_NAME = "development-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "example"
    
    UPLOADS = "Fabricio/Programacion/static/img"
    
    SESSION_COOKIE_SECURE = False
