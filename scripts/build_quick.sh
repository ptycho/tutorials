#!/bin/sh

# Point notebooks to source
cd ./docs/
rm ./notebooks
ln -s ../notebooks ./notebooks 
cd ../

# Build Jupyter book
module load ptypy
jupyter-book build docs/
