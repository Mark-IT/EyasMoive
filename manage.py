#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Author:huchong

from app import create_app, db
from flask import render_template
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

app = create_app()

manager = Manager(app)
migrate = Migrate(app, db=db)

manager.add_command('db', MigrateCommand)
manager.add_command("runserver", Server())


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404


if __name__ == "__main__":
    manager.run()
