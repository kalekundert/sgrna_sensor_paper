#!/usr/bin/env python3

"""\
Tabulate the E. coli libraries screened during this project.

Usage:
    make_table.py
"""

import docopt
import yaml
import jinja2
import sgrna_sensor
import pandas as pd
from enum import Enum
from sgrna_sensor import densiometry
from pprint import pprint

def make_table(df):
    render_template(df, 'library_tabular.tex')
    xelatex('library_table.tex')

def tabulate_sequences():
    with open('library_names.yml') as file:
        designs = yaml.load(file)

    rows = []

    for id, name in enumerate(designs, 1):
        row = {}
        row['id'] = id
        row['domain'] = name_to_domain(name)
        row['sequence'] = sgrna_sensor.from_name(name).dna
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

def render_template(df, path):
    loader = jinja2.FileSystemLoader('.')
    env = jinja2.Environment(
            loader=loader,
            trim_blocks=True,
            lstrip_blocks=True,
    )
    template = env.get_template(f'jinja_{path}')
    template.stream(df=df).dump(path)

def xelatex(path):
    import subprocess
    subprocess.run(['xelatex', '--halt-on-error', path])


if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    df = tabulate_sequences()
    make_table(df)
