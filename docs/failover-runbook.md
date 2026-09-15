# Controlled failover drill

## Preconditions

Use two isolated lab hosts, a maintenance window, a documented rollback owner
and a monitoring observer. Verify the rendered HAProxy configuration and both
Keepalived configurations before touching either service.

## Evidence to collect

1. On the active node, record the VIP address and HAProxy health endpoint.
2. From an independent lab client, record a successful request through the VIP.
3. Record node exporter and HAProxy exporter scrape freshness.

## Drill

1. Stop HAProxy on the active *lab* node.
2. Observe the local health script fail and the VIP move to the peer.
3. Repeat the independent client request and record the outcome.
4. Restart HAProxy, wait for health checks to pass, and intentionally restore
   the preferred state only if the change procedure permits it.

## Abort and rollback

If both nodes claim the VIP, immediately isolate one node from the lab network
under the approved incident procedure. Do not keep experimenting. Restore a
known-good Keepalived configuration and validate ARP/neighbour convergence.

This document does not claim a measured recovery time; capture that evidence
only during an authorised drill.
