import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()
HOME = os.getenv('PROJECT_HOME')
DATAHOME = Path(HOME, 'data')
MODELHOME = Path(HOME, 'models')
