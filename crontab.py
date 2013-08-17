import os 


class CronManager(object):
    """ 
    This is manager to create and remove jobs from crontab. It takes as
    arguments flask app - to get application root_path - and crontab as an 
    instance of CronTab class from crontab package included in python-crontab
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
        return '{0}/bin/python'.format(os.environ['PWD']) 

    def create_command(self, filename):
        """ Returns command for crontab by inserting name of file to run """
        return '{0} {1}/scripts/{2}'.format(
            self.get_python_path(), self.app.root_path, filename)

    def get_commands(self):
        """ Collects commands for crontab """
        command_tmp = self.create_command('cron_tmp.py') 

        self.commands = {
            'command_tmp': command_tmp,
        }

    def remove_commands(self):
        """ Removes commands from user's crontab """
        for command in self.commands.values():
            self.cron.remove_all(command)

    def create_jobs(self):
        """ Creates commands for crontab """

        # Delete old files from TMP folder
        cron_tmp = self.cron.new(command=self.commands['command_tmp'])
        cron_tmp.minute.every(1)
