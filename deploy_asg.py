import argparse
import boto3
import yaml
import sys


## LOAD CLOUDFORMATION TEMPLATE

def load_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()
  
CLOUDFORMATION_TEMPLATE = load_template('LaunchTemplate.yaml')

## DEPLOY THE STACK 
def deploy_stack(base_name, instance_count):
    # Convert YAML template to JSON for CloudFormation
    cloudformation = boto3.client('cloudformation')
    stack_name = f"{base_name}"

    # Load the template and replace parameters with user input
    template = CLOUDFORMATION_TEMPLATE.replace("awesome", base_name).replace("Default: 1", f"Default: {instance_count}")
    try:
        # Create CloudFormation stack
        response = cloudformation.create_stack(
            StackName=stack_name,
            TemplateBody=template,
            Parameters=[
                {"ParameterKey": "BaseName", "ParameterValue": base_name},
                {"ParameterKey": "DesiredCapacity", "ParameterValue": str(instance_count)},
            ],
            Capabilities=['CAPABILITY_NAMED_IAM'],
        )
        print(f"Stack creation initiated: {response['StackId']}")
    except Exception as e:
        print(f"Error creating stack: {e}")

## MAIN FUNCTION 
def main():
    parser = argparse.ArgumentParser(description="Deploy ASG and Launch Template with CloudFormation")
    parser.add_argument("-n", "--name", type=str, required=True, help="Base name for the created artifacts")
    parser.add_argument("-s", "--size", type=int, required=True, help="Number of instances for the ASG DesiredCapacity")

    args = parser.parse_args()

    base_name = args.name
    instance_count = args.size

    # Validate instance count
    if instance_count < 1 or instance_count > 10:
        print("Error: Instance count must be between 1 and 10.")
        sys.exit(1)

    # Deploy stack with provided parameters
    deploy_stack(base_name, instance_count)

if __name__ == "__main__":
    main()
