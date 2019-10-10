import boto3

if __name__ == '__main__':
    session = boto3.Session(profile_name = 'aws-snapshot-auto')
    ec2 = session.resource('ec2')

    ec2.instances.all()
    for i in ec2.instances.all():
        print(i)
