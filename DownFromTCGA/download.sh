#!/bin/sh
set -x

gdc_executable_path=$1
source_folder=$2

python main.py --gdc $gdc_executable_path $source_folder

