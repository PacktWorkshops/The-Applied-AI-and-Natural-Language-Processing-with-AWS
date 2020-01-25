import boto3

def lambda_handler(event, context):
    # create a s3 object
    s3 = boto3.client("s3")
    
    # enter the specific bucket name to the 'bucket' variable
    bucket = 'account-balance-202001241911' # <input_bucket_name>
    
    print('Bucket = ' + bucket)
    filename = 'balance.txt'
	
    # print the filename 
    print('filename: ', filename)

    # create the file object
    file_obj = s3.get_object(Bucket = bucket, Key = filename)
    
    # extract account balance from the objet in the bucket
    account_balance =  (float(file_obj['Body'].read()))

    return 'Your balance is ' + str(account_balance)