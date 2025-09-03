# Documentation for the Dice Project
---

The purpose of the dice project is to facilitate the process of generating random numbers.

The die project should provide the user with the ability to select the type of die that they want to use.

https://en.wikipedia.org/wiki/Dice

Some of the die options that are available include `D4`, `D6`, `D8`, `D10`, `D12`, and `D20`. There is also the possibility to create a `custom die`.

The program should allow for rolling a die to revil the new random number, shake a die to generate a random number before rolling, get the current face of a die, to get the type of die that is being used or to set the face of a die.

The test for the die program have been written using the default unittest library that comes preinstalled in python. 

We can run the tests using the following command:

`python -m unittest`

or

`python -m unittest discover tests`

or 

`python -m unittest discover -s tests -p 'test_*.py'`

Additional documentation on how to use the dice project is provided in the docs folder.

----
## Packaging the project

In order to package the project you will have to have a separate `venv` environment to isolate your project from the rest of your production environment.

You also will need to have `pip`, `setuptools`, `wheel` and `build` installed in your local `venv`.

If you have pip but do not have the rest of the dependencies installed you can add the rest of the dependencies using the following pip command:

`pip install build setuptools wheel`

In order to build the `dice` package you can run the following commad:

`python -m build`

the result will be inside a `dist` folder. It will contain the package name and version number.
There will be two files one as `whl` or `wheel` package that will be used for later installation and a `.tar.gz` file. 

In order to install the build package in a separate environment you will have to activate the environment where you want to install the package. Then you will use `pip install` to install the project inside the new environment as follows:

`pip install <file-location>\<package-name>-<version>-<py-version>.whl`

for example:

`pip install dice-0.0.1-py3-none-any.whl`