from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app.settings import app
from app.models.user import *

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
