# AWS Data Processing and Loading Script

This repository contains a Python script for processing data stored in an S3 bucket and loading it into an Amazon Redshift table. The script is designed to run on an EC2 instance and uses IAM roles to securely access AWS services.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Python Script](#python-script)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project demonstrates an end-to-end data processing pipeline using AWS services. The pipeline involves downloading raw data from an S3 bucket, preprocessing the data using a Python script on an EC2 instance, and loading the cleaned data into an Amazon Redshift table. Once the data is in Redshift, it can be used for analysis and visualization with tools like Tableau.

### Workflow Overview

1. **AWS S3**: Stores raw data files. S3 is a scalable storage service that allows easy access and management of data.
2. **EC2**: Runs a Python script that downloads the raw data from S3, cleans and preprocesses it, and then loads the cleaned data into Redshift. EC2 provides scalable computing capacity in the cloud.
3. **Amazon Redshift**: A fully managed data warehouse that makes it simple and cost-effective to analyze all your data using standard SQL. The cleaned data is loaded into Redshift for further analysis.
4. **Tableau**: A data visualization tool that can connect to Redshift to create interactive and shareable dashboards. It helps in visualizing the data and deriving insights.

### Data Processing Steps

1. **Download from S3**: The script downloads a CSV file from an S3 bucket.
2. **Preprocess Data**: The script filters, transforms, and cleans the data. For example, it filters rows, converts date formats, adjusts breed names, and renames columns.
3. **Load into Redshift**: The cleaned data is inserted into an Amazon Redshift table.
4. **Visualization with Tableau**: Once the data is in Redshift, you can connect Tableau to Redshift to create visualizations and dashboards.

## Prerequisites

Before you begin, ensure you have the following:

- An AWS account
- AWS CLI configured with your credentials
- Python 3.6 or higher installed
- Boto3 and Psycopg2 Python libraries installed
- An S3 bucket with your data file
- An Amazon Redshift cluster set up and accessible
- An EC2 instance with appropriate IAM roles to access S3 and Redshift

## Setup

### AWS IAM Roles

1. **Create an IAM Role for EC2**:
    - Go to the AWS Management Console.
    - Create a role with `AmazonS3FullAccess` and `AmazonRedshiftFullAccess` policies attached.
    - Attach this role to your EC2 instance.

## Python Script

The Python script is located in the `Script` folder and performs the following tasks:

1. **Download from S3**: Fetches the CSV file from the specified S3 bucket.
2. **Preprocess Data**: Filters, transforms, and cleans the data.
3. **Load into Redshift**: Inserts the cleaned data into an Amazon Redshift table.

Ensure that you update the script with your specific AWS details such as bucket name, Redshift cluster details, and table schema.

## Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install required Python libraries**:
    ```bash
    pip install boto3 psycopg2 pandas
    ```

3. **Run the script**:
    ```bash
    python Script/port.py
    ```
Ensure your EC2 instance has the necessary IAM roles attached and has network access to both S3 and Redshift.

## Dashboard

Dashboard created by Data Analyst Tammie Cheung posted to my own Tableau Account

![image](https://github.com/micow980/Dog-Adoption-Project/assets/110073973/0a430ba5-3b6d-426e-9e97-381c6b2591a2)

https://public.tableau.com/views/Dashboard_17191973842400/Dashboard1?:language=en-US&publish=yes&:sid=&:display_count=n&:origin=viz_share_link


