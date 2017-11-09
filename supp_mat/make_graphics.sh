#!/usr/bin/env bash
set -euo pipefail
source ../fcm.sh

function predict_spacer_quality () {(
    supp_mat=$(pwd)
    cd -P ../../../notebook/20170329_test_multiple_spacers
    ./predict_spacer_quality.py -o ${supp_mat}/affinity_correlation.pdf
)}


fcm fold_change 20160304_combined_rational_designs_with_paper_labels.yml \
    -o in_vitro_in_vivo.pdf -d 6e-4,6e0 -p

predict_spacer_quality
