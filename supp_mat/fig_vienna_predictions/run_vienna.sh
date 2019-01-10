#!/usr/bin/env bash
set -euo pipefail

sgrna_sensor -rc mhf/30 rxb/11/1

ligrna=$(sgrna_sensor rxb/11/1)
  ligrna='GUUUCAGAGCUAUGCUGGAAACAGCAUAGCAAGUUGAAAUAAGUGGGAUACCAGCCGAAAGGCCCUUGGCAGCCUACGUUAUCAACUUGAAAAAGUGGCACCGAGUCGGUGCUUUUUU'
unpaired='..........................................................................x...........................................'
holo='--motif GAUACCAGCCGAAAGGCCCUUGGCAGC,(...((((((....)))...)))...),-9.212741321099747'
rnafold="RNAfold --partfunc"

function free_energy () {
    stdin=$(cat)
    free_energy=$(pcregrep -o1 '\[([-.0-9]*)\]' <<< $stdin)
    echo "$stdin" 1>&2
    echo "Ensemble free energy: $free_energy kcal/mol" 1>&2
    echo $free_energy
}

echo -e "\nPartition function (apo):"
g_apo=$(echo -e "$ligrna" | $rnafold | free_energy)

echo -e "\nU95 unpaired macrostate (apo):"
g_apo_unpaired=$(echo -e "$ligrna\n$unpaired" | $rnafold --constraint | free_energy)

echo -e "\nPartition function (holo):"
g_holo=$(echo -e "$ligrna" | $rnafold $holo | free_energy)

echo -e "\nU95 unpaired macrostate (holo):"
g_holo_unpaired=$(echo -e "$ligrna\n$unpaired" | $rnafold $holo --constraint | free_energy)

python <<EOF
from math import *

kT = (1.987203611e-3) * (310)
f_unpaired_apo = exp(-($g_apo_unpaired - $g_apo) / kT)
f_unpaired_holo = exp(-($g_holo_unpaired - $g_holo) / kT)

print()
print(f'% of apo ensemble unpaired:  {100 * f_unpaired_apo:.2f}%')
print(f'% of holo ensemble unpaired: {100 * f_unpaired_holo:.2f}%')
EOF

