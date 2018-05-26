# -*- coding:utf-8 -*-
# from flask_script import Manager, Server
# from flask_migrate import Migrate, MigrateCommand
# from main import app, db, User, Role
#
# manager = Manager(app)
# migrate = Migrate(app, db)
#
# manager.add_command('runserver', Server())
# manager.add_command('db', MigrateCommand)
#
#
# @manager.shell
# def make_shell_context():
#     return dict(app=app, db=db, User=User, Role=Role)
#
#

import os
from app import create_app, db
from app.models import User, Role
from flask.ext.script import Manager, Shell, Server
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('runserver', Server())
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

# import os
# from flask_migrate import Migrate
# from app import create_app, db
# from app.models import User, Role
#
# app = create_app(os.getenv('FLASK_CONFIG') or 'default')
# migrate = Migrate(app, db)
#
#
# @app.shell_context_processor
# def make_shell_context():
#     return dict(db=db, User=User, Role=Role)
#
#
# @app.cli.command()
# def test():
#     """Run the unit tests."""
#     import unittest
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
