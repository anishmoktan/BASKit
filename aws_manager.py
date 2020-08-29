import boto3

class AWS_Manager:

    def __init__(self):
        self.s3_client = boto3.client('s3')

    
    def upload_file(self):
        try:
            self.s3_client.upload_file(
                    Filename="accounts.json", Bucket="lmtd-team-alpha", Key="accounts.json")

        except:
            print('there is an err')

    def download_file(self):
        try:
            self.s3_client.download_file(
                'lmtd-team-alpha', 'accounts.json', 'accounts.json')
        
        except:
            print('there is an err')
