from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Role, Comment,Pitch
from  flask_migrate import Migrate, MigrateCommand

#creating an app instance  
app = create_app('production')  
# configure_uploads(app, (csvfiles,), lambda app: '/var/uploads')


manager = Manager(app)
manager.add_command('server',Server)

manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Pitch = Pitch, Role = Role, Comment = Comment ) 

if __name__ == '__main__':
    manager.run()