# The MIT License
#
# Copyright (c) 2013 by Wojciech Rola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice shall be included in
# all copies or substantial portions of the Software.

import sys 


class CronManager(object):
    """ 
    This is manager to create and remove jobs from crontab. It takes as
    arguments flask app - to get application root_path - and crontab as an 
    instance of CronTab class from crontab module included in python-crontab
    package.

    Usage:
        from crontab import CronTab

        cron = CronManager(app, CronTab())
        cron.run()
    """

    def __init__(self, app, crontab):
        self.app = app
        self.cron = crontab 

    def run(self):
        self.get_commands()
        self.remove_commands()
        self.create_jobs()
        self.cron.write()

    def get_python_path(self):
        """ Returns application python path - if you want then customize it! """
        return '{0}/bin/python'.format(sys.prefix) 

    def create_command(self, filename, interpreter=None):
        """ Returns command for crontab by inserting name of file to run """
        if not interpreter:
            return '{0} {1}/scripts/{2}'.format(
                self.get_python_path(), self.app.root_path, filename)

        return '{0} {1}/scripts/{2}'.format(
            interpreter, self.app.root_path, filename)

    def get_commands(self):
        """ Collects commands for crontab """
        command_dummy = self.create_command('cron_dummy.py') 

        self.commands = {
            'command_dummy': command_dummy,
        }

    def remove_commands(self):
        """ Removes commands from user's crontab """
        for command in self.commands.values():
            self.cron.remove_all(command)

    def create_jobs(self):
        """ Creates commands for crontab """

        # Create dummy text file
        cron_tmp = self.cron.new(command=self.commands['command_dummy'])
        cron_tmp.minute.every(1)
