from django.db import models
import boto.ec2

class AWSServer(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, null=True, blank=True)
    aws_access_key = models.CharField(max_length=20)
    aws_secret_key = models.CharField(max_length=40)
    aws_region = models.CharField(max_length=20, default='us-east-1')
    user_name = models.CharField(max_length=20, default='Administrator')

    def __unicode__(self):
        return self.name

    def get_connection(self):
        conn = boto.ec2.connect_to_region(self.aws_region, aws_access_key_id=self.aws_access_key, aws_secret_access_key=self.aws_secret_key)
        inst = conn.get_all_instances(filters={'tag:Name': self.name})[0].instances[0]
        return inst

    def start_server(self):
        inst = self.get_connection()
        inst.start()

    def stop_server(self):
        inst = self.get_connection()
        inst.stop()

    def get_server_state(self):
        inst = self.get_connection()
        return inst.state

