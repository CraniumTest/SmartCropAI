import boto3

def download_data_from_s3(bucket_name, s3_file_key):
    s3 = boto3.client('s3')
    local_file_name = '/tmp/' + s3_file_key
    s3.download_file(bucket_name, s3_file_key, local_file_name)
    return local_file_name
