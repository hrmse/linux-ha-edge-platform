from pathlib import Path

import yaml

ROOT = Path(__file__).parents[1]


def test_example_inventory_uses_documentation_addresses() -> None:
    inventory = yaml.safe_load((ROOT / "inventory/lab/hosts.yml").read_text())
    hosts = inventory["all"]["children"]["edge"]["hosts"]
    assert {host["ansible_host"] for host in hosts.values()} == {"192.0.2.11", "192.0.2.12"}


def test_vrrp_secret_is_not_committed() -> None:
    example = (ROOT / "inventory/lab/group_vars.example.yml").read_text()
    assert "REPLACE_WITH_A_SECRET" in example
    assert "vault_edge_vrrp_password:" in example


def test_haproxy_template_has_tls_and_health_checks() -> None:
    template = (ROOT / "roles/edge/templates/haproxy.cfg.j2").read_text()
    assert "ssl crt {{ edge_haproxy_tls_certificate }}" in template
    assert "option httpchk GET /healthz" in template
