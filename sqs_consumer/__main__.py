import os

from loafer.managers import LoaferManager
from .routes import routes
from .settings import settings

os.environ['AWS_DEFAULT_REGION'] = settings.AWS_DEFAULT_REGION
os.environ['AWS_ACCESS_KEY_ID'] = settings.AWS_ACCESS_KEY_ID
os.environ['AWS_SECRET_ACCESS_KEY'] = settings.AWS_SECRET_ACCESS_KEY

manager = LoaferManager(routes=routes)
manager.run()
