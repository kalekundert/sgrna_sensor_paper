#!/usr/bin/env bash
set -euo pipefail
source ../fcm.sh

function predict_spacer_quality () {(
    supp_mat=$(pwd)
    cd -P ../../../notebook/20170329_test_multiple_spacers
    ./predict_spacer_quality.py -o ${supp_mat}/affinity_correlation.pdf
)}

predict_spacer_quality

fcm fold_change 20171010_compare_promoters.yml \
    -o graphics/j23150.svg \
    -I \
    -d 1e-3,1e1

