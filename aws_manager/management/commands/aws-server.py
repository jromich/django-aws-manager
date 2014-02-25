from django.core.management.base import BaseCommand
from django.utils import timezone

from aws_manager.models import AWSServer

class Command(BaseCommand):
    """
    Can be used to manage EC2 servers from the command line
    or a scheduler
    """
    help = 'starts an aws ec2 server.  requires server name as argument'
    usage_str = "Usage: ./manage.py start-stop server_name action"

    def is_weekday(self):
        """ check to see if it's a weekday"""
        d = timezone.now()
        return d.isoweekday() in range(1, 6)

    def handle(self, server_name=None, action=None,*args, **options):
        # make sure a server name is passed
        if not server_name:
            print "Please specify a server name matching the EC2 name."
            return

        # made sure an action is passed
        if not action:
            print "Please specify an action: 'start', 'stop', 'state', 'start-wkdays-only', 'stop-wkdays-only'."
            return


        # See if the server exists
        servers = AWSServer.objects.filter(name=server_name)
        if not servers:
            print 'Server named %s not found.  Check admin settings.' % server_name
            return

        server = servers[0]

        if action == 'start':
            print 'starting ' + server_name
            server.start_server()

        elif action == 'stop':
            print 'stopping ' + server_name
            server.stop_server()

        elif action == 'start-wkdays-only':
            if self.is_weekday():
                print 'starting ' + server_name
                server.start_server()

        elif action == 'stop-wkdays-only':
            if self.is_weekday():
                print 'stopping ' + server_name
                server.stop_server()

        elif action == 'state':
            print server_name + ' state: ' + server.get_server_state()

        else:
            print 'action not found'






