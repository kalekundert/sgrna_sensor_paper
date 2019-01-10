#!/usr/bin/env bash
set -euo pipefail

./notebook/miller_units.py \
  notebook/plate_reader/20180809_target_lac.toml \
  notebook/plate_reader/20180810_target_lac.toml \
  notebook/plate_reader/20180813_target_lac.toml \
  --output 20180809_target_lac_triplicate \
  --figure-mode \

