# AWS Auto Scaling Group Deployment Tool

A Python-based CLI tool for deploying AWS Auto Scaling Groups (ASG) with Launch Templates and VPC infrastructure using CloudFormation.

## Overview

This tool automates the deployment of a complete AWS infrastructure including:
- VPC with public subnet
- Internet Gateway and routing
- Auto Scaling Group with Launch Template
- EC2 Key Pair for instance access

## Prerequisites

- Python 3.x
- AWS credentials configured
- Required Python packages:
  - boto3
  - pyyaml

## Installation

1. Clone this repository
2. Install required packages:

```
pip install boto3 pyyaml
```

## Infrastructure Components

The tool creates the following AWS resources:

1. **Networking:**
   - VPC (CIDR: 10.0.0.0/16)
   - Public Subnet (CIDR: 10.0.1.0/24)
   - Internet Gateway
   - Route Table with public routing

2. **Security:**
   - EC2 Key Pair (automatically generated)

3. **Compute:**
   - Launch Template with t3.micro instances
   - Auto Scaling Group with configurable capacity

## Usage

Run the deployment script using the following command:

```
python deploy_asg.py -n <base_name> -s <instance_count>
```

### Parameters

- `-n, --name`: Base name for all resources (e.g., "myapp")
- `-s, --size`: Number of EC2 instances (1-10)

### Example

```
python deploy_asg.py -n awesome -s 3
```

This will create:
- VPC named `awesome-VPC`
- Key Pair named `awesome-key`
- Launch Template named `awesome-LaunchTemplate`
- Auto Scaling Group with 3 instances with named `awesome-AutoScalingGroup`
- Instances tagged with `awesome-instance`

## Resource Naming

All resources are automatically tagged with the provided base name:
- VPC: `{basename}-VPC`
- Internet Gateway: `{basename}-IGW`
- Public Subnet: `{basename}-PublicSubnet`
- Route Table: `{basename}-PublicRT`
- Key Pair: `{basename}-key`
- Launch Template: `{basename}-LaunchTemplate`
- EC2 Instances: `{basename}-instance`

## CloudFormation Outputs

The stack provides the following outputs:
- Key Pair Name
- Public Subnet ID
- VPC ID

## Error Handling

The tool includes validation for:
- Instance count (must be between 1 and 10)
- CloudFormation stack creation errors

## Important Notes

1. The AMI ID is currently set to `ami-0866a3c8686eaeeba`. Update this in the template for your region.
2. The VPC is created with a default CIDR of 10.0.0.0/16
3. The public subnet uses 10.0.1.0/24 CIDR range
4. The Auto Scaling Group has a maximum limit of 5 instances

## Security Considerations

- The Key Pair is automatically generated and should be stored securely
- All instances are launched in a public subnet with internet access
- Remember to clean up resources when no longer needed



