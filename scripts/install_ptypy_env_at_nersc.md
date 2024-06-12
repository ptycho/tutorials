First, clone the nersc conda env

```
conda create --prefix /global/common/software/ntrain7/ptypy_env --clone /global/common/software/nersc/pm-2022q3/sw/python/3.9-anaconda-2021.11
```

Activate the new conda env

```
conda activate /global/common/software/ntrain7/ptypy_env
```

Add additional packages that we need for ptypy with cupy

```
conda install -c conda-forge pyfftw cupy
```

Add additional packages that we need for ptypy with pycuda
```
conda install -c nvidia cuda-nvcc cuda-cudart-dev
conda install -c conda-forge reikna pycuda
```

Add additional packages for cufft
```
conda install -c nvidia libcufft-dev libcufft-static
conda install -c conda-forge cmake>=3.8.0 pybind11
```

Install Ptypy
```
git clone https://github.com/ptycho/ptypy.git
pip install .

```

Install cufft
```
cd cufft
pip install .
```

Add kernel to user settings
```
python -m ipykernel install --user --name ptypy_env --display-name PtyPy
```
