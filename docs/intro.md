# Introduction

The purpose of these tutorials is to provide a comprehensive collection of examples targeting a wide range of scientists and engineers interested in ptychography, from experimental users to algorithm and code developers.

## Overview

The table below gives an overview of all examples with associated data and a link for downloading the data.
| **Tutorial** | **Download Data** | **File Size** | **Reference** |
| :-| :-| :-:|:-: |
| **The Basics** |
|  [](notebooks/basic_examples/00_the_parameter_tree)         |   No Data Required  | - | - |
|  [](notebooks/basic_examples/01_using_yaml_or_json_config)  |   No Data Required  | - | - |
|  [](notebooks/basic_examples/02_input_output_parameters)    |   No Data Required  | - | - |
|  [](notebooks/basic_examples/03_scan_models)                |   No Data Required  | - | - |
|  [](notebooks/basic_examples/04_choosing_engines)           |   No Data Required  | - | - |
|  [](notebooks/basic_examples/05_projectional_engines)       |   No Data Required  | - | - |
|  [](notebooks/basic_examples/06_stochastic_engines)         |   No Data Required  | - | - |
|  [](notebooks/basic_examples/07_gradient_based_engines)     |   No Data Required  | - | - |
| **Experimental X-ray Data** |
|  [](notebooks/experimental_xray_data/00_data_loading)                 |  [small_data.zip](https://zenodo.org/records/11501765/files/small_data.zip?download=1)                           |  126 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/01_working_with_large_data)      |  [dls_i08_nanogold_spiral.zip](https://zenodo.org/records/11501765/files/dls_i08_nanogold_spiral.zip?download=1) |  1.11 GB |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/02_fixing_data_issues)           |  [small_data.zip](https://zenodo.org/records/11501765/files/small_data.zip?download=1)                           |  126 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/03_partial_coherence)            |  [dls_i08_nanogold_spiral.zip](https://zenodo.org/records/11501765/files/dls_i08_nanogold_spiral.zip?download=1) |  1.11 GB |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/04_position_refinement)          |  [dls_i14_test_structure.zip](https://zenodo.org/records/11501765/files/dls_i14_test_structure.zip?download=1)   |  3.68 GB |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/05_missing_detector_frames)      |  [dls_i08_nanogold_raster.zip](https://zenodo.org/records/11501765/files/dls_i08_nanogold_raster.zip?download=1) |  993 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/06_testing_different_algorithms) |  [dls_i13_butterfly.zip](https://zenodo.org/records/11501765/files/dls_i13_butterfly.zip?download=1)             |  286 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/07_multi_gpu)                    |  [dls_i08_nanogold_spiral.zip](https://zenodo.org/records/11501765/files/dls_i08_nanogold_spiral.zip?download=1) |  1.11 GB |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/experimental_xray_data/08_data_from_soleil_swing)       |  TBA                                                                                                             | 4.8 GB   | TBA  |
|  [](notebooks/experimental_xray_data/09_wavefield_preconditioner)     |  TBA                                                                                                             | 4.8 GB   | TBA  |
|  [](notebooks/experimental_xray_data/10_data_from_nanomax)            |  NanoMax example dataset [10_keV.zip](https://zenodo.org/records/18241822/files/10_keV.zip?download=1)           | 432 MB   | [DOI](https://doi.org/10.5281/zenodo.18241822)  |
|  [](notebooks/experimental_xray_data/11_data_from_softimax)            |  [ptycho_on_siemensstar_MAXIV_SoftiMAX.zip](https://zenodo.org/records/23246616/files/ptycho_on_siemensstar_MAXIV_SoftiMAX.zip?download=1)  | 565 MB   | [DOI](https://doi.org/10.5281/zenodo.23246616) |
|  [](notebooks/experimental_xray_data/12_data_from_cosaxs)            |  [ptycho_on_siemensstar_MAXIV_CoSAXS.zip](https://zenodo.org/records/23210803/files/ptycho_on_siemensstar_MAXIV_CoSAXS.zip?download=1)           | 463 MB   | [DOI](https://doi.org/10.5281/zenodo.23210803)  |
| **Electron Ptychography Data** |
|  [](notebooks/ptychography_with_electrons/00_electron_data)                       | [dls_epsic_80kV_graphene.zip](https://zenodo.org/records/11501765/files/dls_epsic_80kV_graphene.zip?download=1)  |  270 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/ptychography_with_electrons/01_chaining_multiple_engines)           | [dls_epsic_80kV_graphene.zip](https://zenodo.org/records/11501765/files/dls_epsic_80kV_graphene.zip?download=1)  |  270 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/ptychography_with_electrons/02_start_from_previous_reconstruction)  | [dls_epsic_80kV_graphene.zip](https://zenodo.org/records/11501765/files/dls_epsic_80kV_graphene.zip?download=1)  |  270 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
| **Advanced Examples** |
|  [](notebooks/supplementary_examples/00_nearfield_ptychography)  |  esrf_id16_AlNi_nearfield.zip        	|  532 MB  |        TBA       	|
|  [](notebooks/supplementary_examples/01_object_regularisation)   |  esrf_id16_AlNi_nearfield.zip        	|  532 MB  |        TBA       	|
|  [](notebooks/supplementary_examples/02_live_visualisation)      |  [dls_i08_nanogold_spiral.zip](https://zenodo.org/records/11501765/files/dls_i08_nanogold_spiral.zip?download=1)  |  1.11 GB |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
|  [](notebooks/supplementary_examples/03_simulating_data)         |  No Data Required                      |  -       | -                                       |
|  [](notebooks/supplementary_examples/04_modified_initial_probe)  |  [small_data.zip](https://zenodo.org/records/11501765/files/small_data.zip?download=1)  |  126 MB  |  [DOI](https://doi.org/10.5281/zenodo.11501765) |
| **User Examples** |
|  [](notebooks/user_examples/00_template)                         |  -                                     |  -       |       -            |
|  [](notebooks/user_examples/01_super_resolution)                 |  [SiemensStar_ID16A_ESRF_farfieldptycho.zip](https://zenodo.org/records/13694455)       |  67 MB   |  [DOI](https://doi.org/10.5281/zenodo.13694456) |

## Jupyter Lab/Notebooks

```{note}
Most of the content of this tutorial has been created in the form of Jupyter Notebooks and the JupyterLab interface is the recommended way of working through these examples. JupyterLab is very easy to use, should you wish to learn more about the Jupyter project and the tools it provides, visit: [https://jupyter.org](https://jupyter.org).
``````

As a minimal introduction, a few words about Jupyter Notebooks, which offer a convenient way to provide executable code (e.g. Python) alongside formatted text (using markdown). All notebooks used here are structured in the same way, with some informative content at the top and a full code example at the bottom, separated by a horizontal line:

```{figure} ./jupyter_notebook_1.PNG
:name: jupyterlab1
```

In order to execute the code cell (or any other cell), simply select the cell and type **SHIFT+ENTER** or **ALT+ENTER**

```{figure} ./jupyter_notebook_2.PNG
:name: jupyterlab2
```

## Working with this tutorial within an HPC environment

It might not always be possible to run Jupyter Notebooks with access to accelerated GPU hardware, for example in the case of only having terminal-based access to an HPC cluster. Below are a few pointers as to how best to run the PtyPy tutorials on an interactive HPC compute node, e.g. using Slurm.

1. Start an interactive session in the terminal, e.g. single GPU on slurm: ```srun --ntasks 1 --cpus-per-task 1 --gpus 1 --time 02:00:00 --pty bash```

2. Create a new Python file and paste the full-length code block at the end of the Jupyter-based tutorial into it

3. Some of the settings in the PtyPy parameter tree are optimised for running it as a Jupyter Notebook, in particular the following should be modified when running interactively with Python

```python
# Give your reconstruction a name
p.run = "test"

# Set verbose level to info
p.verbose_level = "info"

# Set io settings (no files saved)
p.io = u.Param()
p.io.home = "./"
p.io.rfile = "recons/%(run)s/%(run)s_%(engine)s_%(iterations)04d.ptyr"
p.io.autosave = u.Param(active=False)
p.io.interaction = u.Param(active=False)
p.io.autoplot = u.Param(active=False)
```

this will turn off all interactive plotting that is configured in all Jupyter Notebook tutorials, and it will save the results in a folder called ```recons``` in the folder defined as ```p.io.home```.

## How to visualise PtyPy output from a .ptyr file

### From a terminal with Graphics

The simplest way to inspect the reconstruction results saved in the .ptyr file is to use the following command from a terminal with access to Graphics

```bash
ptypy.plot <PATH-TO-PTYR-FILE>
```

### From a Jupyter Notebook or a Python script

An alternative approach is to visualise the results in a Jupyter Notebook or from a Python script using the following code

```python
import os
import ptypy.utils.plot_client as pc
ptyr_filename = "<PATH-TO-PTYR-FILE>"
fig = pc.figure_from_ptyr(ptyr_filename)
```