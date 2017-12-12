#!/usr/bin/env python3

from sgrna_sensor import from_name, t7_promoter as t7, spacer, aptamer
from sgrna_sensor import render_latex_table

context = {
    'components': [
        ('T7 promoter', t7()),
        ('AAVS spacer', spacer('aavs')),
        ('RFP1 spacer', spacer('rfp1')),
        ('RFP2 spacer', spacer('rfp2')),
        ('GFP1 spacer', spacer('gfp1')),
        ('GFP2 spacer', spacer('gfp2')),
        ('Theophylline aptamer', aptamer('theo')),
        ('3-Methylxanthine aptamer', aptamer('3mx')),
        ('Positive control', from_name('on')),
        (r'Negative control \autocite{briner2014}', from_name('off')),
        (r'\ligrnaF{}', from_name('mhf/30')),
        (r'\ligrnaFF{}', from_name('mhf/37')),
        (r'\ligrnaB{}', from_name('rxb/11/1')),
    ]
}

render_latex_table('components.tex', context)

