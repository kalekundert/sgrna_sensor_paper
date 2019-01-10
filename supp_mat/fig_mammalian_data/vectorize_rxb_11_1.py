#!/usr/bin/env python3

from pylab import *

# 1. Open `vectorize_rxb_11_1.xcf` in gimp.
# 2. Read coordinates off y-axis and into `bar_heights`.
# 3. Count height of each error bar into `error_heights`.
# 4. Run this script.
# 5. Import `vectorise_rxb_11_1.svg` into inkscape to make look nice.

bar_heights = array([
        289,
        290,
        288,
        4,
        287,
        283,
        285,
        278,
        275,
        3,
        268,
        267,
        266,
        260,
])
error_heights = array([
        6,
        3,
        5,
        2,
        7,
        6,
        5,
        7,
        7,
        2,
        4,
        4,
        9,
        8,
])

x = range(len(bar_heights))

bar(x, bar_heights, yerr=error_heights-2)

savefig('vectorize_rxb_11_1.svg')
show()
