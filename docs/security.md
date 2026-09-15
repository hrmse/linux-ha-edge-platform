# Security boundary

Keep VRRP authentication material out of Git and deliver it through Ansible
Vault or a secret manager. Restrict SSH to named operators, limit Prometheus
scraping to the monitoring network and use a firewall around exporter ports.
Terminate only approved TLS certificates; the example disables backend
certificate verification solely because a lab may use private test PKI. Replace
that setting with CA verification in a real deployment.
