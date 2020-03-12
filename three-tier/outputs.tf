# ELB address
output "elb_address" {
  value = "${aws_elb.web.dns_name}"
}

#EC2 details

output "ec2_hostname" {
  value = "${aws_instance.web.dns_name}"
}


#RDS details
output "subnet_group" {
  value = "${aws_db_subnet_group.default.name}"
}

output "db_instance_id" {
  value = "${aws_db_instance.default.id}"
}

output "db_instance_address" {
  value = "${aws_db_instance.default.address}"
}