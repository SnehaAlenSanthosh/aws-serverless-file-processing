import os
import boto3
import logging

# Initialize AWS clients
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

# Get environment variables
TABLE_NAME = os.getenv('TABLE_NAME')
BUCKET_NAME = os.getenv('BUCKET_NAME')

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    Lambda function triggered by S3 event to process uploaded files.
    """
    try:
        # Get bucket name and file key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        logger.info(f"Processing file: {file_key} from bucket: {bucket_name}")

        # Fetch file content from S3
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response['Body'].read().decode('utf-8')

        # Perform file processing (e.g., line count)
        line_count = len(file_content.splitlines())
        logger.info(f"File {file_key} contains {line_count} lines.")

        # Log result to DynamoDB
        table = dynamodb.Table(TABLE_NAME)
        table.put_item(
            Item={
                'FileName': file_key,
                'LineCount': line_count,
                'Status': 'Processed'
            }
        )
        logger.info(f"Logged processing result to DynamoDB for file: {file_key}")

    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        raise
