terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
    datadog = {
      source = "datadog/datadog"
    }
  }
}

provider "aws" {
  region  = "us-east-1"
  profile = "vscode"
}

provider "datadog" {
  api_key = var.datadog_api_key
}

variable "datadog_api_key" {
  description = "Datadog API key"
  type        = string
}

# Your resources and configurations go here
