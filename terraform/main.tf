terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "cv_bucket" {
  bucket = "emma-oatley-cv-bucket"
}

resource "aws_s3_object" "provision_source_files" {
  bucket = aws_s3_bucket.cv_bucket.bucket

  # ../CV/ is the Directory containing files to be uploaded to S3
  for_each = fileset("../CV/", "**/*.*")

  key    = each.value
  source = "../CV/${each.value}"
  content_type = each.value
}
