import boto3
import psycopg2
import pandas
from sqlalchemy import create_engine
from configparser import ConfigParser


region = 'eu-west-1'
bucket_name = 'payminute'

config = ConfigParser()
config.read('.env')

access_key = config['AWS']['access_key']
secret_key =  config['AWS']['secret_key']


def create_bucket():
    client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key
    )

    client.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': region
        }
    )
