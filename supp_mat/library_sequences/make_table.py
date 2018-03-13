#!/usr/bin/env python3

"""\
Tabulate the E. coli libraries screened during this project.

Usage:
    make_table.py
    make_table.py reset_alignment [-f]

Options:
    -f --force
        Overwrite any existing manual alignment.  Be careful, because it's a 
        lot of work to make those alignments!
"""

import math
import docopt
import yaml
import jinja2
import sgrna_sensor
import pandas as pd
from enum import Enum
from pathlib import Path
from sgrna_sensor import densiometry
from pprint import pprint

libraries_path = Path('library_names.yml')
alignment_path = Path('manual_alignment.yml')

midrules = {
        'rx/5/5',
        'rb/6/6',
}

def tabulate_sequences():
    with libraries_path.open() as file:
        designs = yaml.load(file)

    # The alignments won't exist if we're creating the file for the first time.
    try:
        with alignment_path.open() as file:
            manual_alignment = yaml.load(file)
    except FileNotFoundError:
        manual_alignment = {}

    rows = []

    for id, name in enumerate(designs, 1):
        row = {}
        row['id'] = id
        row['name'] = name
        row['domain'] = name_to_domain(name)
        row['sequence'] = sgrna_sensor.from_name(name).dna
        row['manual_alignment'] = manual_alignment.get(name)
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
    df = tabulate_sequences()

    # Initialize the manual alignment file.
    if args['reset_alignment']:
        if alignment_path.exists() and not args['--force']:
            print(f"{alignment_path} already exists, pass -f to overwrite.")
            raise SystemExit

        print(df)
        sequences = {
                row['name']: row['sequence']
                for i, row in df.iterrows()
        }
        with alignment_path.open('w') as file:
            yaml.dump(sequences, file)

    # Make the table.
    else:
        sgrna_sensor.render_latex_table('library_sequences.tex', locals())
