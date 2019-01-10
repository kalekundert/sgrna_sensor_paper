#!/usr/bin/env bash
set -euo pipefail
source ../../fcm.sh

fcm fold_change 20171010_compare_promoters.yml \
    -o graphics/j23150.svg \
    -I \
    -d 1e-3,1e1

