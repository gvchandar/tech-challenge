output ec2_"address" {
  #value = "${aws_elb.web.dns_name}"
   value = "${aws_instance.web.private_ip}"
}
