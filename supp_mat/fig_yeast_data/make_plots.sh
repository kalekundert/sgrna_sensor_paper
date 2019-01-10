#!/usr/bin/env bash
set -euo pipefail
source ../../fcm.sh

fcm fold_change 20171218_repeat_yeast_for_supp_gfp.yml -O 5x3 -d 1e-1,2e0
fcm fold_change 20171218_repeat_yeast_for_supp_rfp.yml -O 5x3 -d 1e-1,2e0
