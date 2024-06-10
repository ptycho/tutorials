# Introduction

The purpose of these tutorials is to provide a comprehensive collection of examples targeting a wide range of scientists and engineers interested in ptychography, from experimental users to algorithm and code developers.

## Overview

The table below gives an overview of all examples with associated data and a link for downloading the data.
| **Tutorial** 	| **Data** 	| **File Size** | **Reference**  |
| :-| :-| :-:|:-: |
| **The Basics** |
|  [](notebooks/basic_examples/00_the_parameter_tree)         |   No Data Required  | - | - |
|  [](notebooks/basic_examples/01_using_yaml_or_json_config)  |   No Data Required  | - | - |
|  [](notebooks/basic_examples/02_input_output_parameters)    |   No Data Required  | - | - |
|  [](notebooks/basic_examples/03_scan_models)            	  |   No Data Required  | - | - |
|  [](notebooks/basic_examples/04_choosing_engines)           |   No Data Required  | - | - |
|  [](notebooks/basic_examples/05_projectional_engines)       |   No Data Required  | - | - |
|  [](notebooks/basic_examples/06_stochastic_engines)         |   No Data Required  | - | - |
|  [](notebooks/basic_examples/07_gradient_based_engines)     |   No Data Required  | - | - |
| **Experimental X-ray Data** |
|  [](notebooks/experimental_xray_data/00_data_loading)            	    |  small_data.zip          	   |  126 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/01_working_with_large_data)      |  dls_i08_nanogold_spiral.zip |  1.11 GB |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/02_fixing_data_issues)           |  small_data.zip       	   |  126 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/03_partial_coherence)            |  dls_i08_nanogold_spiral.zip |  1.11 GB |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/04_position_refinement)          |  dls_i14_test_structure.zip  |  3.68 GB |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/05_missing_detector_frames)      |  dls_i08_nanogold_raster.zip |  993 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/06_testing_different_algorithms) |  dls_i13_butterfly.zip       |  286 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/experimental_xray_data/07_multi_gpu)            	    |  dls_i08_nanogold_spiral.zip |  1.11 GB |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
| **Electron Ptychography Data** |
|  [](notebooks/ptychography_with_electrons/00_electron_data)            	        | dls_epsic_80kV_graphene.zip  |  270 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/ptychography_with_electrons/01_chaining_multiple_engines)         	| dls_epsic_80kV_graphene.zip  |  270 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/ptychography_with_electrons/02_start_from_previous_reconstruction)  | dls_epsic_80kV_graphene.zip  |  270 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
| **Supplementary Examples** |
|  [](notebooks/supplementary_examples/00_nearfield_ptychography)  |  esrf_id16_AlNi_nearfield.zip        	|  532 MB  |        TBA       	|
|  [](notebooks/supplementary_examples/01_object_regularisation)   |  esrf_id16_AlNi_nearfield.zip        	|  532 MB  |        TBA       	|
|  [](notebooks/supplementary_examples/02_live_visualisation)      |  dls_i08_nanogold_spiral.zip           |  1.11 GB |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
|  [](notebooks/supplementary_examples/03_simulating_data)         |  No Data Required                      |  -       | -                                       |
|  [](notebooks/supplementary_examples/04_modified_initial_probe)  |  small_data.zip                        |  126 MB  |  [doi](https://zenodo.org/doi/10.5281/zenodo.11501764) |
 

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
