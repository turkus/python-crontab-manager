from flask import Flask
from crontab import CronTab

from python_crontab_manager import CronManager


app = Flask(__name__)

crontab_manager = CronManager(app, CronTab())
crontab_manager.run()


if __name__ == "__main__":
    app.run()



