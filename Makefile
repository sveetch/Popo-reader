PYTHON=python3
PIP=venv/bin/python -m pip

.PHONY: help install clean delpyc

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo
	@echo "  install              -- to proceed to a new install"

	@echo "  clean                -- to clean local repository from install"
	@echo

clean:
	rm -Rf venv
	find . -name "*\.pyc"|xargs rm -f
venv:
	$(PYTHON) -m venv venv

install: venv
	$(PIP) install -r requirements.txt
