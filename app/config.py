class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    RESTX_JSON = {'ensure_ascii': False, 'indent': 4}
