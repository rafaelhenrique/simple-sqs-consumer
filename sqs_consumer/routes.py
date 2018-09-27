from loafer.ext.aws.routes import SQSRoute
from .handlers import print_handler, error_handler
from .settings import settings


routes = (
    SQSRoute(
        settings.SQS_QUEUE_NAME,
        {'options': {'WaitTimeSeconds': 3}},
        handler=print_handler,
        error_handler=error_handler,
    ),
)
