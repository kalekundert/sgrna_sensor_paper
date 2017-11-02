#!/usr/bin/env bash
set -euo pipefail

fcm=../../../flow_cytometry

$fcm/fold_change.py \
    $fcm/data/20170315_test_w11_m11.yml \
    -p -m mode -O 7x9 -o $.svg -I -n SSC-A
    
