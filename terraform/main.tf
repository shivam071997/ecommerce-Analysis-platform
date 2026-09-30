terraform {
  required_version = ">= 1.0"
}

resource "local_file" "project_info" {
  filename = "${path.module}/project-info.txt"

  content = <<EOT
Project: E-Commerce Analytics Platform
Environment: Development
Managed by: Terraform
EOT
}
