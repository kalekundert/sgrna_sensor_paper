#!/usr/bin/env zsh
set -euxo pipefail

mkdir -p graphics

function fcm () {(
    # <script name> <yaml file> [<other args>...]
    fcm=$(realpath ../../../flow_cytometry)

    cd graphics
    $fcm/$1.py $fcm/data/$2 "${@:3}" -Io '$.svg'
)}

#fcm bar_chart 20170706_theo_3mx.yml -y0.11 -O4x3

fcm bar_chart 20170831_multiplex_timecourse_theo_3mx.yml -O6x3 -y1.0
fcm bar_chart 20170831_multiplex_timecourse_3mx.yml -O6x3 -y1.0

