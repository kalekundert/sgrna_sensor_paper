#!/usr/bin/env zsh
set -euxo pipefail
source ../fcm.sh

mkdir -p graphics
cd graphics

function multiple_spacers () {(
    python "../../../../notebook/20170329_test_multiple_spacers/$@"
)}

qpcr="../../../../notebook/20181115_measure_ligrna_induction_time_scale"

# I chose the 6.45" output width by trial-and-error to get the distribution 
# plot to be nearly 3.25" wide.  I chose the 12.00" height to get the traces to 
# fit comfortably in 2", such that the whole plot obeys the golden ratio.
#fcm fold_change 20170703_rfp2_rxb_mhf_validation.yml -I -d '2e-3,3e0' -O '6.45x12.00' -Q800 -v

## Old layout sizes
#fcm titration_curve 20170807_titrate_rfp2.yml -O '3.345x1.963' -Q '37'
#multiple_spacers make_heatmap.py -o '$.svg' -L -O '3.851x2.259'
#multiple_spacers make_bar_plot.py -o '$_bar_plot.svg' -O '3.674x2.615'

## Experiment w/ different layouts/sizes.

#fcm titration_curve 20170807_titrate_rfp2.yml -O '4.25x2.40' -Q '37' -ML
#multiple_spacers make_bar_plot.py -o '$_bar_plot.svg' -O '3.698x2.22'
$qpcr/gfp_mrna_vs_time.py $qpcr/data/20181201_ligrna_timecourse.toml -o $.svg -xH -O '4.163x1.52'
