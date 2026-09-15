# Interview discussion guide

This blueprint is useful for discussing the operational trade-offs of VRRP:
split-brain risk, neighbour/ARP convergence, health-check sensitivity, priority
design, monitoring from an independent client and an explicit abort condition.

It also demonstrates why a valid configuration is not enough: a planned drill
needs a rollback owner, observable evidence and an isolated environment. The
repository intentionally does not report failover time or availability because
those values depend on the authorised environment and measured drill data.
