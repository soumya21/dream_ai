import boto3
from app.core.config import settings

dynamodb = boto3.resource('dynamodb', region_name=settings.dynamodb_region)
table = dynamodb.Table(settings.dynamodb_table)