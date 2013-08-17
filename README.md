python-crontab-manager
======================


This is manager to create and remove jobs from crontab. It takes as
arguments flask app - to get application root_path (optional) - and 
crontab as an instance of CronTab class from crontab package included
in python-crontab package.

Usage:
    
```
from crontab import CronTab

cron = CronManager(app, CronTab())
cron.run()
```

Requirements
------------

python-crontab==1.3
Flask (optional)
