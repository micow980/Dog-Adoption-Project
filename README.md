# Dog Adoption Project

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

This project demonstrates how to use AWS services like S3, EC2, and Redshift together to process and load data securely and efficiently. The Python script downloads data from an S3 bucket, processes it, and loads it into an Amazon Redshift table.

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

1. Downloads a CSV file from an S3 bucket.
2. Processes the data to filter and transform it.
3. Loads the processed data into an Amazon Redshift table.

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

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
