# Cookie Cutter for Data Science 

A template of data science projects - focused on tabular data.

## Setup

```bash
$ pip install cookiecutter
$ cookiecutter https://github.com/ADGEfficiency/cookiecutter-data-science
```

## Example projects

- [hacking-medium-headlines](https://github.com/ADGEfficiency/hacking-medium-headlines)
- [Rossman Kaggle Mini-Competition Model Solution](https://github.com/ADGEfficiency/minicomp-rossman-solution)


## Philosophy

### Changes from cookiecutterdatascience

- no check for Python 2 - Python 3 only
- data is stored in `$HOME/PROJECT_NAME`
- `make` is used only for project setup - other tasks like data cleaning, feature engineering etc are 
- generic useful functions included - see `notebooks/cookies.ipynb` for examples
