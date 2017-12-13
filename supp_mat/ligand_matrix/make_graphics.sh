#!/usr/bin/env bash
set -euo pipefail
source ../../fcm.sh

fcm=../../../../flow_cytometry
$fcm/ligand_matrix.py -o $.svg -O 6x8
