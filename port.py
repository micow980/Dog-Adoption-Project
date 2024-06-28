import pandas as pd
import boto3
import io
import psycopg2

# AWS S3 details
input_bucket_name = 'dog-adoption-micow-project'
input_s3_key = 'Austin_Animal_Center_Outcomes_20240618.csv'

# Amazon Redshift connection details
redshift_host = 'redshift-dogproject.654654471738.us-east-2.redshift-serverless.amazonaws.com'
redshift_port = 5439
redshift_dbname = 'dev'
redshift_user = 'admin'
redshift_password = 
redshift_table = 'dog_project'

# Create an S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Download the file from S3 into memory
try:
    obj = s3_client.get_object(Bucket=input_bucket_name, Key=input_s3_key)
    df = pd.read_csv(io.BytesIO(obj['Body'].read()))
    print("File successfully ingested from S3.")
except Exception as e:
    print(f"Error downloading file from S3: {e}")
    exit()

# Filter the DataFrame for 'Dog' rows
df = df[df['Animal Type'] == 'Dog']

# Convert 'DateTime' column to datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'], format='%m/%d/%Y %I:%M:%S %p')

# Define the date range
start_date = pd.Timestamp('2022-01-01')
end_date = pd.Timestamp.now()

# Filter the DataFrame for dates between start_date and end_date
df = df[(df['DateTime'] >= start_date) & (df['DateTime'] <= end_date)]

# Function to adjust the breed name
def adjust_breed(breed):
    first_breed = breed.split('/')[0].strip()
    if first_breed.endswith(" Mix"):
        return first_breed
    else:
        return first_breed + " Mix"

# Apply the function to the "Breed" column to create the new "breed_adjusted" column
df['breed_adjusted'] = df['Breed'].apply(adjust_breed)

# Rename columns to match Redshift table headers
df = df.rename(columns={
    'DateTime': 'datetime',
    'Outcome Type': 'outcome_type',
    'Sex upon Outcome': 'sex_upon_outcome',
    'Age upon Outcome': 'age_upon_outcome'
})

# Connect to Amazon Redshift
try:
    conn = psycopg2.connect(
        host=redshift_host,
        port=redshift_port,
        dbname=redshift_dbname,
        user=redshift_user,
        password=redshift_password
    )
    print("Connected to Amazon Redshift.")

    cursor = conn.cursor()

    # Create table in Redshift if it doesn't exist
    create_table_sql = f"""
    CREATE TABLE IF NOT EXISTS {redshift_table} (
        datetime TIMESTAMP,
        outcome_type VARCHAR(50),
        sex_upon_outcome VARCHAR(50),
        age_upon_outcome VARCHAR(50),
        color VARCHAR(50),
        breed_adjusted VARCHAR(100)
    );
    """
    cursor.execute(create_table_sql)
    conn.commit()

    # Insert data into Redshift
    for index, row in df.iterrows():
        insert_sql = f"""
        INSERT INTO {redshift_table} (datetime, outcome_type, sex_upon_outcome, age_upon_outcome, color, breed_adjusted)
        VALUES ('{row['datetime']}', '{row['outcome_type']}', '{row['sex_upon_outcome']}', '{row['age_upon_outcome']}', '{row['Color']}', '{row['breed_adjusted']}')
        """
        cursor.execute(insert_sql)
    conn.commit()
    print(f"Data inserted into Redshift table '{redshift_table}'.")

    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error connecting to Redshift or inserting data: {e}")
