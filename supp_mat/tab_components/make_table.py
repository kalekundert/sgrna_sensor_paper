#!/usr/bin/env python3

import yaml
from sgrna_sensor import from_name, t7_promoter as t7, spacer, aptamer
from sgrna_sensor import render_latex_table

components = [
        ('T7 promoter', t7()),
        ('AAVS spacer', spacer('aavs')),
        ('sgG1 spacer', spacer('gfp1')),
        ('sgR1 spacer', spacer('rfp1')),
        ('sgG2 spacer', spacer('gfp2')),
        ('sgR2 spacer', spacer('rfp2')),
        ('folA spacer', spacer('fol1')),
        ('Theophylline (theo) aptamer', aptamer('theo')),
        ('3-Methylxanthine (3mx) aptamer', aptamer('3mx')),
        ('Thiamine pyrophosphate (tpp) aptamer', aptamer('tpp')),
        ('Positive control', from_name('on')),
        (r'Negative control (G63C, G64C)', from_name('off')),
        (r'\ligrnaF{}', from_name('mhf/30')),
        (r'\ligrnaF[2]{}', from_name('mhf/37')),
        (r'\ligrnaF[3]{}', from_name('w30/65')),
        (r'\ligrnaF[4]{}', from_name('w30/64/1')),
        (r'\ligrnaB{}', from_name('rxb/11/1')),
        (r'\ligrnaB[2]{}', from_name('w11/2')),
        (r'\ligrnaB[3]{}', from_name('m11/ga')),
]

with open('manual_alignments.yml') as file:
    manual_alignments = yaml.load(file)

# Make sure there aren't any typos.
for name, sgrna in components:
    if name in manual_alignments:
        aligned_seq = ''.join(x for x in manual_alignments[name] if x in 'ATCG')
        assert sgrna.dna.upper() == aligned_seq.upper(), f"""\
Name:     {name}
Expected: {sgrna.dna.upper()}
Actual:   {aligned_seq.upper()}
"""

render_latex_table('components.tex', locals())

