from app import app
from flask_script import Manager, Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User
from app import pitch_app,db
from config import config_options


app = pitch_app('development')
manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User )

if __name__ =='__main__':
    manager.run()
