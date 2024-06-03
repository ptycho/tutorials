# Introduction

Welcome to the hands-on tutorial session of the [1{sup}`st` PtyPy workshop](https://www.diamond.ac.uk/Home/Events/2023/Ptychography--PtyPy--Software-Workshop-2023.html), 
held on January 12th and 13th 2023 at the [Diamond Light Source](https://www.diamond.ac.uk). The purpose of these tutorials is to provide a comprehensive collection of examples targeting a wide range of scientists and engineers interested in ptychography, from experimental users to algorithm and code developers. 

```{note}
Most of the content of this tutorial has been created in the form of Jupyter Notebooks and throughout this workshop, we are going to use JupyterLab to execute and interact with the content prepared for this workshop. The JupyterLab interface is very easy to use, but should you wish to learn more about the Jupyter project and the tools it provides, visit: [https://jupyter.org](https://jupyter.org).
```

## How to Get Started
For the duration of this workshop, all participants will be able to run the tutorials on compute resources at NERSC. In preparation for the workshop, you should have already been asked to register for a training account and should hopefully have your login credentials ready.

In a browser, go to [https://jupyter.nersc.gov](https://jupyter.nersc.gov) and login with your personal training account credentials. Once your resources are allocated, you should see a JupyterLab interface looking like this

```{figure} ./jupyter_hub.PNG
:name: jupyterlab

```


First, we need to clone the GitHub repository containing all the tutorials into the ```$HOME``` directory by a opening a terminal (click on "+" and then "Terminal") and executing this command:
```bash
git clone https://github.com/ptycho/tutorials.git
```

followed by running this set up command

```bash
/global/common/software/ntrain3/ptypy_workshop_setup.sh
```

Now that we have cloned the tutorials and set up the correct environment, we can simply navigate to ```tutorials``` in the file panel on the left and open the [first tutorial](./notebooks/01_05_Getting_Started_with_PtyPy/1_the_parameter_tree) from within the ```notebooks``` folder.


## How to use a Jupyter Notebook
Before we get started with PtyPy, a few words about Jupyter Notebooks, which offer a convenient way to provide executable code (e.g. Python) alongside formatted text (using markdown). All notebooks used here are structured in the same way, with some informative content at the top and a full code example at the bottom, separated by a horizontal line:

```{figure} ./jupyter_notebook_1.PNG
:name: jupyterlab1
```

In order to execute the code cell (or any other cell), simply select the cell and type **SHIFT+ENTER** or **ALT+ENTER**

```{figure} ./jupyter_notebook_2.PNG
:name: jupyterlab2
```

## Table of Contents
The content of this tutorial is structured into 6 different topics from beginner level to advanced topics:

```{tableofcontents}
```