from prettyconf import config


class Settings:
    AWS_DEFAULT_REGION = config('AWS_DEFAULT_REGION')
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

    SQS_QUEUE_NAME = config('SQS_QUEUE_NAME')


settings = Settings()
