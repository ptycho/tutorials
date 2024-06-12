# Minimal installation

First, clone the nersc conda env

```
conda create --prefix /global/common/software/ntrain7/ptypy_env --clone /global/common/software/nersc/pe/conda/24.1.0/Miniconda3-py311_23.11.0-2
```

Activate the new conda env

```
conda activate /global/common/software/ntrain7/ptypy_env
```

Add additional packages that we need for ptypy with cupy

```
conda install -c conda-forge pyfftw cupy
```

Install Ptypy
```
git clone https://github.com/ptycho/ptypy.git
pip install .

```

Add kernel to user settings
```
python -m ipykernel install --user --name ptypy_env --display-name PtyPy
```


## Optional installation adding pycuda and cufft

Add additional packages that we need for ptypy with pycuda (optional, needed only for one extra tutorial)
```
conda install -c nvidia cuda-nvcc cuda-cudart-dev
conda install -c conda-forge reikna pycuda
```

Add additional packages for cufft (optional)
```
conda install -c nvidia libcufft-dev libcufft-static
conda install -c conda-forge cmake>=3.8.0 pybind11
```

Install cufft (optional)
```
cd cufft
pip install .
```
