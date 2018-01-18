import boto3

ec2 = boto3.resource('ec2')

instances = ec2.instances.all()

for i in instances:
    print(i.instance_id)

instance = ec2.instances.filter(
    InstanceIds=['i-092a0104ab8b27478']
)

for i in instance:
    print(i.public_ip_address)