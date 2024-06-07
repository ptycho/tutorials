#!/bin/sh

# Copy notebooks
cd ./docs/
cp -r ../notebooks/* ../converted/
rm ./notebooks
ln -s ../converted ./notebooks 

# Convert notebooks
module load ptypy
python ./scripts/convert.py

# Build Jupyter book
cd ../
jupyter-book build docs/
