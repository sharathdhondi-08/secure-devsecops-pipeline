# ==============================================================================
# INFRASTRUCTURE SCHEMAS BLUEPRINT MAP: variables.tf
# ==============================================================================

variable "aws_region" {
  type        = string
  description = "Target deployment cloud data center geographic region"
  default     = "us-east-1"
}

# DECLARE SECURE HOOK PLACEHOLDERS (No values assigned here!)
variable "database_master_password" {
  type        = string
  description = "High-security root password parameter for the cloud database cluster"
  sensitive   = true # Tells Terraform to explicitly mask this value inside CLI terminal screens
}

