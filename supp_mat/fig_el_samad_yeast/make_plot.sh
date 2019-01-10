#!/usr/bin/env bash
set -euo pipefail

FCM=../../../../flow_cytometry/
FLAGS='-o $.svg -O 6x4 -d 8e-2,2e0 -f 5 -p'

$FCM/fold_change.py $FLAGS $FCM/data/20171218_repeat_yeast_for_supp_rfp.yml
$FCM/fold_change.py $FLAGS $FCM/data/20171218_repeat_yeast_for_supp_gfp.yml
