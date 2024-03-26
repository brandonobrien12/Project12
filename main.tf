provider "aws" {
  region = "us-east-2a" 
  
}

resource "aws_instance" "instance1"{

  ami = "ami-019f9b3318b7155c5"
  instance_type = "t2.micro"

  tags ={
    name = "ZebedeeDemo"
  } 
}