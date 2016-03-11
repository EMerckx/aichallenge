import os
from sqlalchemy.orm import sessionmaker

# Since this package is just a bunch of separate but interdependable scripts,
# but it's overkill to use distutils, we'll just make sure that the PYTHONPATH
# is always correctly set. This is e.g. needed for werkzeug.
# See https://github.com/mitsuhiko/werkzeug/issues/461#issuecomment-139369694
# and https://github.com/mitsuhiko/flask/issues/1246
__root_dir = os.path.dirname(os.path.dirname(__file__))
os.environ['PYTHONPATH'] = __root_dir

Session = sessionmaker(autoflush=False)
session = Session()