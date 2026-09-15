#!/usr/bin/env bash
set -euo pipefail

curl --fail --silent --show-error --max-time 1 http://127.0.0.1:8404/metrics >/dev/null
