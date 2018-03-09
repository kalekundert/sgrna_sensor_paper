#!/usr/bin/env python3

from sgrna_sensor import from_name, t7_promoter as t7, spacer, aptamer
from sgrna_sensor import render_latex_table

context = {
    'components': [
        ('T7 promoter', t7()),
        ('AAVS spacer', spacer('aavs')),
        ('G1 spacer', spacer('gfp1')),
        ('R1 spacer', spacer('rfp1')),
        ('G2 spacer', spacer('gfp2')),
        ('R2 spacer', spacer('rfp2')),
        ('Theophylline aptamer', aptamer('theo')),
        ('3-Methylxanthine aptamer', aptamer('3mx')),
        ('Positive control', from_name('on')),
        (r'Negative control', from_name('off')),
        (r'\ligrnaF{}', from_name('mhf/30')),
        (r'\ligrnaF[2]{}', from_name('mhf/37')),
        (r'\ligrnaF[3]{}', from_name('w30/65')),
        (r'\ligrnaF[4]{}', from_name('w30/64/1')),
        (r'\ligrnaB{}', from_name('rxb/11/1')),
        (r'\ligrnaB[2]{}', from_name('w11/2')),
        (r'\ligrnaB[3]{}', from_name('m11/ga')),
    ]
}

render_latex_table('components.tex', context)

