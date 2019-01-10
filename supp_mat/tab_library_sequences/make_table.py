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

alignment_path = Path('manual_alignment.yml')

midrules = {
        'rx/5/5',
        'rb/6/6',
        'mh/7',
        #'tpp/uh/6/6',
        #'rbi/4/8',
        #'ux/5/4',
}

def tabulate_sequences():
    with alignment_path.open() as file:
        manual_alignment = yaml.load(file)

    rows = []

    for id, name in enumerate(manual_alignment, 1):
        row = {}
        row['id'] = id
        row['name'] = name
        row['domain'] = name_to_domain(name)
        row['sequence'] = sgrna_sensor.from_name(name).dna
        row['manual_alignment'] = manual_alignment.get(name)
        row['complexity'] = sgrna_sensor.library_size(row['sequence'])
        row['log4_complexity'] = math.log(row['complexity'], 4)
        rows.append(row)

        if manual_alignment:
            real_seq = row['sequence']
            aligned_seq = ''.join(
                    x for x in row['manual_alignment']
                    if x in 'ACGTN')

            if real_seq != aligned_seq:
                raise ValueError(f"""\
Alignment for {name} has the wrong sequence:

> {real_seq}
> {aligned_seq} """)

    return pd.DataFrame(rows)

def name_to_domain(name):
    if name.startswith('tpp/'):
        name = name[4:]

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
