# -*- coding: utf-8 -*-

manager = Manager(app)


@manager.command
def run():
    """Run in local machine."""

    app.run(host="0.0.0.0", port=6969, debug=True)



@manager.command
def initdb():


if __name__ == "__main__":
    manager.run()
