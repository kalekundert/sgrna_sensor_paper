#!/usr/bin/env python3

"""\
Create a table showing the data we collected to verify the sequences 
isolated from our screens.

Usage:
    ./make_table.py [-f]

Options:
    -f --force
        Recalculate the fold change values from the raw flow cytometry data.  
        This calculation is normally cached, because it can take a while.
"""

import docopt
import json
import yaml
import fcmcmp
import sgrna_sensor
import analysis_helpers
from pathlib import Path

# I got the list of hits by copying the `linkers` dictionaries from the 
# functions representing hits in `analysis/sgrna_sensor/designs.py`
hits = [
        'rbf/6',
        'rbf/8',
        'rbf/13',
        'rbf/26',
        'rbf/39',
        'rbf/40',
        'rbf/47',
        'rbf/50',
        'rbf/51',
        'rbf/53',
        'rbf/56',
        'rbf/68',
        'rbf/74',
        'rbf/99',
        'rbf/109',
        'rbf/134',

        'rbb/4',
        'rbb/15',
        'rbb/27',
        'rbb/29',
        'rbb/39',
        'rbb/42',
        'rbb/45',

        'rxb/2',
        'rxb/11',
        'rxb/11/1',
        'rxb/14',
        'rxb/22',
        'rxb/39',
        'rxb/44',
        'rxb/51',
        'rxb/91',
        'rxb/94',

        'rhf/6',

        'mhf/3',
        'mhf/4',
        'mhf/7',
        'mhf/13',
        'mhf/16',
        'mhf/20',
        'mhf/21',
        'mhf/25',
        'mhf/26',
        'mhf/30',
        'mhf/35',
        'mhf/37',
        'mhf/38',
        'mhf/41',

        'tpp/uhf/8',
        'tpp/uhf/30',
        'tpp/uhf/37',
        'tpp/uhf/49',
        'tpp/uhf/66',
        'tpp/uhf/71',
        'tpp/uhf/84',
        'tpp/uhf/132',
        'tpp/uhf/135',
        'tpp/uhf/160',
        'tpp/uhf/174',
]

# LaTeX names for the designs that are described in the paper.
names = {
        'rxb/11': r"*",
        'rxb/11/1': r"\ligrnaB{}",
        'mhf/30': r"\ligrnaF{}",
        'mhf/37': r"\ligrnaF[2]{}",

        'tpp/uhf/8':   r"Fig S?: 8",
        'tpp/uhf/30':  r"Fig S?: 30",
        'tpp/uhf/37':  r"Fig S?: 37",
        'tpp/uhf/49':  r"Fig S?: 49",
        'tpp/uhf/66':  r"Fig S?: 66",
        'tpp/uhf/71':  r"Fig S?: 71",
        'tpp/uhf/84':  r"Fig S?: 84",
        'tpp/uhf/132': r"Fig S?: 132",
        'tpp/uhf/135': r"Fig S?: 135",
        'tpp/uhf/160': r"Fig S?: 160",
        'tpp/uhf/174': r"Fig S?: 174",
}

# I got the counts by counting the entries in the `aliases` dictionaries from 
# the same functions.
counts = {
        'rbf/6':        (1, 18),
        'rbf/8':        (2, 18),
        'rbf/13':       (1, 18),
        'rbf/26':       (1, 18),
        'rbf/39':       (1, 18),
        'rbf/40':       (1, 18),
        'rbf/47':       (1, 18),
        'rbf/50':       (1, 18),
        'rbf/51':       (1, 18),
        'rbf/53':       (1, 18),
        'rbf/56':       (1, 18),
        'rbf/68':       (1, 18),
        'rbf/74':       (1, 18),
        'rbf/99':       (1, 18),
        'rbf/109':      (1, 18),
        'rbf/134':      (1, 18),
        'rbf/161':      (1, 18),

        'rbb/4':        (1, 21),
        'rbb/15':       (1, 21),
        'rbb/27':      (10, 21),
        'rbb/29':       (1, 21),
        'rbb/39':       (3, 21),
        'rbb/42':       (2, 21),
        'rbb/45':       (3, 21),

        'rxb/2':        (4, 20),
        'rxb/11':       (5, 20),
        'rxb/14':       (4, 20),
        'rxb/22':       (1, 20),
        'rxb/39':       (1, 20),
        'rxb/44':       (1, 20),
        'rxb/51':       (2, 20),
        'rxb/91':       (1, 20),
        'rxb/94':       (1, 20),

        'rhf/6':        (6,  6),

        'mhf/3':        (1, 15),
        'mhf/4':        (1, 15),
        'mhf/7':        (1, 15),
        'mhf/13':       (1, 15),
        'mhf/16':       (1, 15),
        'mhf/20':       (1, 15),
        'mhf/21':       (2, 15),
        'mhf/25':       (1, 15),
        'mhf/26':       (1, 15),
        'mhf/30':       (1, 15),
        'mhf/35':       (1, 15),
        'mhf/37':       (1, 15),
        'mhf/38':       (1, 15),
        'mhf/41':       (1, 15),

        'tpp/uhf/8':    (2, 20),
        'tpp/uhf/30':   (1, 20),
        'tpp/uhf/37':   (2, 20),
        'tpp/uhf/49':   (1, 20),
        'tpp/uhf/66':   (1, 20),
        'tpp/uhf/71':   (1, 20),
        'tpp/uhf/84':   (2, 20),
        'tpp/uhf/132':  (5, 20),
        'tpp/uhf/135':  (1, 20),
        'tpp/uhf/160':  (3, 20),
        'tpp/uhf/174':  (1, 20),
}

# I got the library indices from Table LIBRARIES.
libraries = {
        'rbf/6':        '1--6',
        'rbf/8':        '1--6',
        'rbf/13':       '1--6',
        'rbf/26':       '1--6',
        'rbf/39':       '1--6',
        'rbf/40':       '1--6',
        'rbf/47':       '1--6',
        'rbf/50':       '1--6',
        'rbf/51':       '1--6',
        'rbf/53':       '1--6',
        'rbf/56':       '1--6',
        'rbf/68':       '1--6',
        'rbf/74':       '1--6',
        'rbf/99':       '1--6',
        'rbf/109':      '1--6',
        'rbf/134':      '1--6',
        'rbf/161':      '1--6',

        'rbb/4':        '1--6',
        'rbb/15':       '1--6',
        'rbb/27':       '1--6',
        'rbb/29':       '1--6',
        'rbb/39':       '1--6',
        'rbb/42':       '1--6',
        'rbb/45':       '1--6',

        'rxb/2':        '7--22',
        'rxb/11':       '7--22',
        'rxb/14':       '7--22',
        'rxb/22':       '7--22',
        'rxb/39':       '7--22',
        'rxb/44':       '7--22',
        'rxb/51':       '7--22',
        'rxb/91':       '7--22',
        'rxb/94':       '7--22',

        'rhf/6':        '23--28',

        'mhf/3':        '29--30',
        'mhf/4':        '29--30',
        'mhf/7':        '29--30',
        'mhf/13':       '29--30',
        'mhf/16':       '29--30',
        'mhf/20':       '29--30',
        'mhf/21':       '29--30',
        'mhf/25':       '29--30',
        'mhf/26':       '29--30',
        'mhf/30':       '29--30',
        'mhf/35':       '29--30',
        'mhf/37':       '29--30',
        'mhf/38':       '29--30',
        'mhf/41':       '29--30',

        'tpp/uhf/8':    '31--35',
        'tpp/uhf/30':   '31--35',
        'tpp/uhf/37':   '31--35',
        'tpp/uhf/49':   '31--35',
        'tpp/uhf/66':   '31--35',
        'tpp/uhf/71':   '31--35',
        'tpp/uhf/84':   '31--35',
        'tpp/uhf/132':  '31--35',
        'tpp/uhf/135':  '31--35',
        'tpp/uhf/160':  '31--35',
        'tpp/uhf/174':  '31--35',
}

midrules = {
        'rbf/134': True,
        'rbb/45': True,
        'rxb/94': True,
        'rhf/6': True,
        'mhf/41': True,
}

def calc_fold_changes(rebuild_cache=False):
    json_path = Path('fold_changes.json')
    fcm_path = Path('../../../data/facs/20180312_library_hits_with_tpp.yml')

    # Cache the fold changes because they take a while to calculate.

    try:
        if rebuild_cache:
            raise FileNotFoundError
        with json_path.open() as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        fold_changes = {}
        experiments = fcmcmp.load_experiments(fcm_path)
        shared_steps = analysis_helpers.SharedProcessingSteps()
        shared_steps.process(experiments)
        analysis_helpers.analyze_wells(experiments)

        for pair in analysis_helpers.yield_related_wells(experiments):
            fold_change, _ = pair.calc_fold_change_with_sign()

            if fold_change < 1:
                fold_changes[pair.label] = 1/fold_change, False
            else:
                fold_changes[pair.label] = fold_change, True

        with json_path.open('w') as file:
            json.dump(fold_changes, file)

        return fold_changes

def load_manual_alignments():
    yml_path = Path('manual_alignments.yml')
    with yml_path.open() as file:
        manual_alignments = yaml.load(file)

    for hit in hits:
        real_seq = sgrna_sensor.from_name(hit).rna
        aligned_seq = ''.join(
                x for x in manual_alignments[hit]
                if x in 'ACGU'
        )
        if real_seq != aligned_seq:
            raise ValueError(f"""\
The manual alignment for {hit} has the wrong sequence!

> {real_seq}
> {aligned_seq}""")

    return manual_alignments

if __name__ == '__main__':
    args = docopt.docopt(__doc__)

    fold_changes = calc_fold_changes(args['--force'])
    fold_change_strs = {
            k: fr"{v[0]:.1f}\textsuperscript{{{'−+'[v[1]]}}}"
            for k,v in fold_changes.items()
    }
    manual_alignments = load_manual_alignments()
    ligands = {k: sgrna_sensor.from_name(k).ligand or 'theo' for k in hits}
    sgrna_sensor.render_latex_table('library_hits.tex', locals())
