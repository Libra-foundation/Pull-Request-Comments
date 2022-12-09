# Contributing.

Welcome to the contributing guide of this repository. This documentation will guide you through the setup of the dev environement and give you the needed guidelines to help to ease the accepting of your contribution.

## Setup your development environment.

You will firt need to install conda. You can find the documentation about this installation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
As of the latest update of this documentation conda version `22.11.0` was used. Feel free to give feedback about the installation process with newer version of conda.

Once conda is installed fork this repository and clone your fork.Then open your command prompt in the root folder of the repos.
Run the following commands : 
- `conda env create -f environment.yml -p ./venv`
- `conda activate ./venv`
- `poetry install --with dev`
- `pre-commit install --install-hooks`

### Comand details
 - #### `conda env create -f environment.yml -p ./venv`
This command create a new conda virtual environment according to the specification provided in the `environment.yml` file.
The environment is stored inside the `venv`.
 - #### `conda activate ./venv`
This enable the newly created environment. You are now in the isolated python environment dedicated to this project.
 - #### `poetry install --with dev`
This command installs all the dependencies needed to develop. We use `poetry` to manage our dependencies you can find poetry's documentation [here](https://python-poetry.org/docs/)
Note that poetry has been installed through the first command runned. This mean that `poetry` is only accessible from the current virtual environment and won't interfer with any other possible installation of `poetry`
 - #### `pre-commit install --install-hooks`
This command will initialise `pre-commit` and install all hooks defined in this repository (which only occure once and may take a little while.).
`pre-commit` is a package that allow to automatically run tasks before commiting. The task are only runned on the filed changed in the commit making the process rather efficient.
We use hooks to reformat the code and the documentation as well as to export the dependencies in the format used by `pip`.


And tada ! Your development enviroment is ready !

