# aws-serverless-file-processing
A scalable serverless solution built on AWS to automate file processing, from upload to data storage using Lambda, S3, and DynamoDB

## Project Overview

This repository contains code for a serverless file processing pipeline that:
- Uploads files to **Amazon S3**.
- Automatically triggers **AWS Lambda** functions to process the uploaded files.
- Logs processing results and stores metadata in **Amazon DynamoDB**.
- Provides a scalable and cost-effective solution without the need for managing traditional servers.
