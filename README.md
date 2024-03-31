# Piscine-python

This repository regroups three piscines (ecol42 course) for learning python. The readme is a repository for notes on how to setup the env for development, either through a docker or using a venv.

## Venv

This is the proper way to do python dev I think.

Create a venv with this command, at the root of the project, in folder venv

```bash
python -m venv .venv
```

Now to activate the venv when on POSIX
```bash
source .venv/bin/activate
```

Set vscode to use the venv we just created, `cmd + shift + p` then `>Python: select interpreter`, now `/training/py1/.venv` for instance.

Installing from requirments file, ofc should be from the `venv`
```bash
pip install -r requirments.txt
```

Make the requirmet file
```
pip freeze >requirments.txt
```

## Python for data science

An overvier of python, from basic functions, list comprehension, modules, classes, data manipulation and graphing.

- Python - 0 - Starting
- Python - 1 - Array
- Python - 2 - DataTable
- Python - 3 - OOP
- Python - 4 - Dod

### Links

 - https://py-pkgs.org/03-how-to-package-a-python#a-brief-introduction
 - https://stackoverflow.com/questions/15746675/how-to-write-a-python-module-package#comment77240793_33770042
 - https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Piscine Data Science

- Data engineer
- Data Warehouse
- Data Analyst
- Data Scientist part 1
- Data Scientist part 2

## Piscine Django

### Links

 - https://docs.docker.com/language/python/develop/

## Piscine Django
