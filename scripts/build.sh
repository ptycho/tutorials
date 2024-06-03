#!/bin/sh

# Copy notebooks
cd ./docs/
cp -r ../notebooks/* ../converted/
rm ./notebooks
ln -s ../converted ./notebooks 
cd ../

# Convert notebooks
module load ptypy
python ./scripts/convert.py

# Build Jupyter book
jupyter-book build docs/
