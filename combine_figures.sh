#!/usr/bin/env bash
set -euo pipefail

pdfunite \
    figure_1/figure_1.pdf \
    figure_2/figure_2.pdf \
    figure_3/figure_3.pdf \
    all_figures.pdf
