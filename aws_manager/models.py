from django.db import models
import boto.ec2


class AWSNotFoundException(Exception):
    """Server not found at AWS"""

class AWSServer(models.Model):
    """
    AWSServer represents a single EC2 server at AWS
    """
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    aws_access_key = models.CharField(max_length=20)
    aws_secret_key = models.CharField(max_length=40)
    aws_region = models.CharField(max_length=20, default='us-east-1')
    user_name = models.CharField(max_length=20, default='Administrator')

    def __unicode__(self):
        return self.name

    def get_connection(self):
        """
        Connects to AWS and returns and instance
        """
        conn = boto.ec2.connect_to_region(self.aws_region, aws_access_key_id=self.aws_access_key, aws_secret_access_key=self.aws_secret_key)
        all_instances = conn.get_all_instances(filters={'tag:Name': self.name})
        if not all_instances:
            raise AWSNotFoundException("AWS Instance not found, check settings.")
        inst = all_instances[0].instances[0]
        return inst

    def start_server(self):
        """
        Sends a message to AWS to start the server
        """
        inst = self.get_connection()
        inst.start()

    def stop_server(self):
        """
        Sends a message to AWS to stop the server
        """
        inst = self.get_connection()
        inst.stop()

    def get_server_state(self):
        """
        returns the state of the server (e.g., 'running', 'stopped')
        """
        inst = self.get_connection()
        return inst.state

