# Basic Three-Tier AWS Architecture

This provides a template for running a simple three-tier architecture on Amazon
Web services. 
Three tiers are 
ELB Load Balancer
EC2 Instance having nginx and Tomcat
RDS Postgres Database 


This example will also create a new EC2 Key Pair in the specified AWS Region. 
The key name and path to the public key must be specified via the
terraform command vars.

After you run `terraform apply` on this configuration, it will
automatically output the DNS address of the ELB. After your instance
registers, this should respond with the default nginx web page.

To run, configure your AWS provider as described in 

https://www.terraform.io/docs/providers/aws/index.html

Run with a command like this:

```
git clone https://github.com/gvchandar/tech-challenge.git 
cd tech-challenge/three-tier
terraform plan -var 'key_name={your_aws_key_name}' \
   -var 'public_key_path={location_of_your_key_in_your_local_machine}'
terraform apply -var 'key_name={your_aws_key_name}' \
   -var 'public_key_path={location_of_your_key_in_your_local_machine}'
```

For example:

```
terraform apply -var 'key_name=terraform' -var 'public_key_path=/root/.ssh/id_rsa.pub'
```
