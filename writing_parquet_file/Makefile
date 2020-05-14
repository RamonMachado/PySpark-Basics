
.ONESHELL:
PYTHON := ${PWD}/venv/bin/python3.7
PIP := ${PWD}/venv/bin/pip3.7

venv:
	@echo "Inicializa uma venv local."
	virtualenv venv -p python3.7

install: 
	$ make venv
	@echo "Instala as dependências numa venv local."
	${PIP} install -r requirements.txt

clean: 
	@echo "Remove a venv local."
	rm -rf venv