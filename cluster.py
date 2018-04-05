import boto3

client = boto3.client('emr', region_name='region')

response = client.run_job_flow(
    Name="test cluster",
    ReleaseLabel='',
    Instances={
        'MasterInstanceType': 'm4.xlarge',
        'SlaveInstanceType': 'm4.xlarge',
        'InstanceCount': 3,
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,
        'Ec2SubnetId': 'my-subnet-id',
        'Ec2KeyName': 'my-key',
    },
    VisibleToAllUsers=True,
    JobFlowRole='EMR_EC2_DefaultRole',
    ServiceRole='EMR_DefaultRole'
)
