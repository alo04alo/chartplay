# -*- coding: utf-8 -*-
#print this is comment of tammao :)
from flask.ext.script import Manager

from fbone.app import create_app
from fbone.app import create_app
from fbone.extensions import db
from frienger.user import User, UserDetail, ADMIN, ACTIVE
from fbone.utils import MALE
# from docs.doc import app_doc

from frienger.auth.funcs import login_api_required

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run(host="0.0.0.0", port=6969, debug=True)


# @manager.command
# def run_doc():
#     app_doc.run(host="0.0.0.0", port=5001, debug=True)


@manager.command
def initdb():
    """Init/reset database."""

    db.drop_all()
    db.create_all()

    admin = User(
        name=u'admin',
        email=u'admin@example.com',
        password=u'123456',
        role_code=ADMIN,
        status_code=ACTIVE,
        user_detail=UserDetail(
            sex_code=MALE,
            age=10,
            url=u'http://admin.example.com',
            deposit=100.00,
            location=u'Hangzhou',
            bio=u'admin Guy is ... hmm ... just a admin guy.'))
    db.session.add(admin)
    db.session.commit()


manager.add_option('-c', '--config',
                   dest="config",
                   required=False,
                   help="config file")

if __name__ == "__main__":
    manager.run()
