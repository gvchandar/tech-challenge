#EC2 specific variable
variable "public_key_path" {
  description = <<DESCRIPTION
Path to the SSH public key to be used for authentication.
Ensure this keypair is added to your local SSH agent so provisioners can
connect.

Example: ~/.ssh/terraform.pub
DESCRIPTION
default = "/root/.ssh/id_rsa.pub"
}

variable "key_name" {
  description = "Desired name of AWS key pair"
  default = "techChallengeKey"
}

variable "aws_region" {
  description = "AWS region to launch servers."
  default     = "eu-west-2"
}

# Ubuntu Precise 18.04 LTS (x64)
variable "aws_amis" {
  default = {
    eu-west-2 = "ami-006a0174c6c25ac06"
  }
}
# RDS specific variables
variable "identifier" {
  default     = "mydb-rds"
  description = "Identifier for your DB"
}

variable "storage" {
  default     = "10"
  description = "Storage size in GB"
}

variable "engine" {
  default     = "postgres"
  description = "Engine type, example values mysql, postgres"
}

variable "engine_version" {
  description = "Engine version"

  default = {
    mysql    = "5.7.21"
    postgres = "9.6.8"
  }
}

variable "instance_class" {
  default     = "db.t2.micro"
  description = "Instance class"
}

variable "db_name" {
  default     = "mydb"
  description = "db name"
}

variable "username" {
  default     = "myuser"
  description = "User name"
}

variable "password" {
  description = "password, provide through your ENV variables"
}