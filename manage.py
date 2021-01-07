import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import db, create_app

app = create_app()

migrate = Migrate(app=app, db=db)

manager = Manager(app=app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
  manager.run()