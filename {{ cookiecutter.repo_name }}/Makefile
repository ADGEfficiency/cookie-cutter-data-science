.PHONY: requirements

PROJECT_NAME = {{ cookiecutter.repo_name }}
PROJECT_HOME = $(HOME)/$(PROJECT_NAME)
PYTHON_INTERPRETER = python3

requirements:
	$(PYTHON_INTERPRETER) -m pip install --upgrade pip
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt
	$(PYTHON_INTERPRETER) -m pip install -e .

dotenv:
	echo "PROJECT_NAME=$(PROJECT_NAME)" > .env
	echo "PROJECT_HOME=$(PROJECT_HOME)" > .env

init-data:
	mkdir -p $(PROJECT_HOME)/data/raw
	mkdir -p $(PROJECT_HOME)/data/final

init-models:
	mkdir -p $(PROJECT_HOME)/models

init:
	make init-data
	make init-models

clean-data:
	rm -rf $(PROJECT_HOME)/data
	make init-data

clean-models:
	rm -rf $(PROJECT_HOME)/data
	make init-data

clean:
	make clean-data
	make clean-models
