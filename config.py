import secrets


class Config:
    token = secrets.token_urlsafe()
    SECRET_KEY = token


class DevelopmentConfig(Config):

    DEBUG = True


config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
