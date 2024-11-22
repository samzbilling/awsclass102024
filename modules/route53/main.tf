resource "aws_route53_zone" "main" {
  name = var.domain_name

  tags = merge(
    var.tags,
    {
      Name = "${var.domain_name}"
    }
  )
}

resource "aws_route53_record" "a_record" {
  zone_id = aws_route53_zone.main.zone_id
  name    = var.domain_name
  type    = "A"
  ttl    = "300"
  records = [var.instance_eip]

  depends_on = [aws_route53_zone.main]  # Depend on the zone creation
}

