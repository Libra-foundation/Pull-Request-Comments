# Contributing.

Welcome to the contributing guide of this repository. This documentation will guide you through the setup of the dev environment and give you some guidelines to help to ease the accepting of your contribution.

## Set up your development environment.

You will first need to install Conda. You can find the documentation about this installation [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
As of the latest update of this documentation, Conda version `22.11.0` was used. Feel free to give feedback about the installation process with newer version of Conda.

Once Conda is installed, fork this repository and clone your fork. Then open your command prompt in the root folder of the repository.
Run the following commands : 
- `conda env create -f environment.yml -p ./venv`
- `conda activate ./venv`
- `poetry install --with dev`
- `pre-commit install --install-hooks`

### Commands details
 - #### `conda env create -f environment.yml -p ./venv`
This command create a new Conda virtual environment according to the specification provided in the `environment.yml` file.
The environment is stored inside the `venv` folder.
 - #### `conda activate ./venv`
This enables the newly created environment. You are now in the isolated python environment dedicated to this project.
 - #### `poetry install --with dev`
This command installs all the dependencies needed to develop. We use `poetry` to manage our dependencies, you can find poetry's documentation [here](https://python-poetry.org/docs/)
Note that poetry has been installed through the first command ran. This mean that `poetry` is only accessible from the current virtual environment and won't interfere with any other possible installation of `poetry`
 - #### `pre-commit install --install-hooks`
This command will initialize `pre-commit` and install all hooks defined in this repository (which only occur once and may take a little while.).
`pre-commit` is a package that allow to automatically run tasks before committing. The tasks are only run on the file changed in the commit, making the process rather efficient.
We use hooks to reformat the code and the documentation, as well as to export the dependencies in the format used by `pip`.


And tada ! Your development environment is ready !

## Tips and tricks :
Don't forget to document your code, your functions etc… </br>
We make an extensive use of the typing so do not forget to type your variables, parameters etc…
Try to make your code as lightweight and fast as possible. As this code is meant to run many, many times, small optimizations does matter.
