#!/usr/bin/env bash
set -euo pipefail
source ../../fcm.sh

fcm fold_change 20180309_alternative_ligrna.yml -d 2e-3,5e0
