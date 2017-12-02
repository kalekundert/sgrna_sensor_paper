#!/usr/bin/env python3

"""\
Tabulate the E. coli libraries screened during this project.

Usage:
    make_table.py
"""

import math
import docopt
import yaml
import jinja2
import sgrna_sensor
import pandas as pd
from enum import Enum
from sgrna_sensor import densiometry
from pprint import pprint

def tabulate_sequences():
    with open('library_names.yml') as file:
        designs = yaml.load(file)

    rows = []

    for id, name in enumerate(designs, 1):
        row = {}
        row['id'] = id
        row['domain'] = name_to_domain(name)
        row['sequence'] = sgrna_sensor.from_name(name).dna
        row['complexity'] = sgrna_sensor.library_size(row['sequence'])
        row['log4_complexity'] = math.log(row['complexity'], 4)
        rows.append(row)

    return pd.DataFrame(rows)

def name_to_domain(name):
    if name[1] == 'b':
        return 'Upper Stem'
    if name[1] == 'x':
        return 'Nexus'
    if name[1] == 'h':
        return 'Hairpin'

    raise ValueError(f"can't determine domain for {name}")


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    context = {'df': tabulate_sequences()}
    sgrna_sensor.render_latex_table('library_sequences.tex', context)
