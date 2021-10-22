import boto3
from pprint import pprint
aws_mag_con=boto3.session.Session(profile_name="default")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
response=ec2_con_cli.describe_instances()
pprint(response)