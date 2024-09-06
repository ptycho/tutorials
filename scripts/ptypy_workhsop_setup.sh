# Last time we used this script: /global/common/software/ntrain3/ptypy_workshop_setup.sh
# This script should be copied into /global/common/software/ntrain7/
module load python
conda activate /global/common/software/ntrain3/ptypy_env
python -m ipykernel install --user --name ptypy_env --display-name PtyPy

# Clone tutorials and create link to data
git clone https://github.com/ptycho/tutorials.git $HOME/tutorials
ln -s /global/cfs/cdirs/ntrain7/ptypy_workshop $HOME/tutorials/data
