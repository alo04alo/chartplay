# -*- coding: utf-8 -*-

from frienger.auth.funcs import login_api_required

app = create_app()
manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run(host="0.0.0.0", port=6969, debug=True)



@manager.command
def initdb():
    print "show tammao"


if __name__ == "__main__":
    manager.run()
