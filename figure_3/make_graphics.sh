#!/usr/bin/env zsh
set -euxo pipefail

mkdir -p graphics

notebook=../../../notebook
lacz=$notebook/20180621_target_endogenous_loci
pa14=$notebook/20180711_test_ligrnas_in_pseudomonas_aeruginosa

#$lacz/miller_units.py \
#  $lacz/plate_reader/20180809_target_lac.toml \
#  $lacz/plate_reader/20180810_target_lac.toml \
#  $lacz/plate_reader/20180813_target_lac.toml \
#  --output 20180809_target_lac_triplicate \
#  --figure-mode 

$pa14/plot_ligrna.py -o graphics/20180711_test_ligrnas_in_pa14.svg
