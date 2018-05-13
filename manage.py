#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:huchong

from app import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db=db)

manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
