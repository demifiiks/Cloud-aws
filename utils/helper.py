import boto3
import psycopg2
import pandas
from sqlalchemy import create_engine

region = 'eu-west-1'
bucket_name = 'payminute'




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
