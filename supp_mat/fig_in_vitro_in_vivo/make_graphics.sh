#!/usr/bin/env bash
set -euo pipefail
source ../../fcm.sh

fcm fold_change 20160304_combined_rational_designs_with_paper_labels.yml \
    -d 6e-4,6e0 \
    -p -S
fcm fold_change 20160304_combined_rational_designs_with_paper_labels_24_25_61_85.yml \
    -d 6e-4,6e0 \
    -p -S
