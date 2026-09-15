# Linux HA Edge Platform

An Ansible reference for a two-node Linux edge tier: HAProxy serves TLS
termination and health checks; Keepalived owns a floating virtual IP through
unicast VRRP; Prometheus exporters expose host and proxy health. It is a
deployable blueprint and local syntax-test target, not evidence of a production
failover or a claim of availability.

## Design

    clients --> floating VIP --> active HAProxy --> private application backends
                               |
    standby HAProxy <--- unicast VRRP ---> active HAProxy
    node_exporter + haproxy_exporter --> Prometheus

The floating address is never bound to an unconfigured interface. VRRP peers,
VIP, interface, TLS paths and authentication secret are supplied as inventory
or secret-manager variables, not hard-coded.

## Repository map

- roles/edge: idempotent HAProxy, Keepalived, exporter and systemd-hardening role.
- inventory/lab: non-routable example inventory; replace it for a real lab.
- playbooks: the explicit deployment entry point.
- tests: static guardrails for accidental secrets and unsafe example addressing.
- docs: preflight, failover drill and security boundaries.

## Lab use

1. Copy inventory/lab/group_vars.example.yml outside the repository and provide
   an encrypted value for ha_vrrp_password.
2. Replace example hosts and TLS paths with isolated lab values.
3. Review the plan before applying:

       ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --check --diff

4. Apply only in the authorised lab:

       ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml

5. Follow [the failover runbook](docs/failover-runbook.md). Do not test a
   production VIP with this repository.

## Safety controls

- The role asserts required topology and secret inputs before configuration.
- Keepalived uses unicast peers rather than multicast in the example.
- HAProxy configuration is validated before restart.
- Service overrides use no-new-privileges, private temporary directories and
  capability restrictions where service behaviour permits.
- Prometheus ports bind to the node address by default; protect them with a
  firewall, network policy and monitoring ACL in real deployments.

## Validate

    python -m pip install -r requirements-dev.txt
    ansible-playbook -i inventory/lab/hosts.yml playbooks/site.yml --syntax-check
    ansible-lint
    pytest
