from dotenv import load_dotenv
from sqlalchemy import create_engine
import mysql.connector.pooling as pooling
import boto3

import os

load_dotenv(dotenv_path=".env_bulletin")
DB_HOST=os.environ.get("DB_HOST")
DB_PORT=os.environ.get("DB_PORT")
DB_DATABASE=os.environ.get("DB_DATABASE")
DB_USERNAME=os.environ.get("DB_USERNAME")
DB_PASSWORD=os.environ.get("DB_PASSWORD")

S3_KEYID=os.environ.get("S3_KEYID")
S3_KEY=os.environ.get("S3_KEY")
REGION=os.environ.get("REGION")
BUCKET_NAME=os.environ.get("BUCKET_NAME")

client = boto3.client('s3',aws_access_key_id = S3_KEYID,aws_secret_access_key = S3_KEY,region_name=REGION)
url_object="mysql+pymysql://%s:%s@%s:%s/%s" %(DB_USERNAME,DB_PASSWORD,DB_HOST,int(DB_PORT),DB_DATABASE)
engine = create_engine(url_object)

from .message import MessageData