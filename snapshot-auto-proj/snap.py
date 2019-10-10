import boto3
import click
import sys

session = boto3.Session(profile_name = 'aws-snapshot-auto')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    for i in ec2.instances.all():
        print(' '.join(("ID :- ",
            i.id,
            "\nInstace Type :-",
            i.instance_type,
            "\nAvailability Zones :-",
            i.placement['AvailabilityZone'],
            "\nState :-",
            i.state['Name'],
            # i.public_dns_name
        )))

        return

if __name__ == '__main__':
    print(sys.argv)
    list_instances()
