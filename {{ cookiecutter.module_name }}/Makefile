SHELL := bash
.ONESHELL:
.SHELLFLAGS := -eu -o pipefail -c
.DELETE_ON_ERROR:
MAKEFLAGS += --warn-undefined-variables
MAKEFLAGS += --no-builtin-rules

TEST_FILTER ?= ""

all: help

.PHONY: clean
clean:  ## Clean build files
	@rm -rf dist
	@rm -rf site


.PHONY: env
env:  ## Create dev environment
	conda env create

.PHONY: help
help:  ## Show this help menu
	@grep -E '^[0-9a-zA-Z_-]+:.*?##.*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?##"; OFS="\t\t"}; {printf "\033[36m%-30s\033[0m %s\n", $$1, ($$2==""?"":$$2)}'

# ------------------------------------------------------------------------------
# Package build, test and docs

.PHONY: package
package:  ## Build Python package
	python setup.py sdist


.PHONY: check
check:  ## Check linting
	flake8 {{ cookiecutter.module_name }}
  isort --check-only --diff --recursive --project {{ cookiecutter.module_name }} --section-default THIRDPARTY
  black --check {{ cookiecutter.module_name }}


.PHONY: fmt
fmt:  ## Format source
	isort --recursive --project poliastro --section-default THIRDPARTY {{ cookiecutter.module_name }}
	black {{ cookiecutter.module_name }}


.PHONY: upload-pypi
upload-pypi:  ## Upload package to PyPI
	twine upload dist/*.tar.gz


.PHONY: upload-test
upload-test:  ## Upload package to PyPI test repository
	twine upload --repository testpypi dist/*.tar.gz


.PHONY: test tests
test: tests
tests:  ## Run tests
	pytest -vvv {{ cookiecutter.module_name }}/tests -k $(TEST_FILTER) --html=test-results/report.html --self-contained-html


.PHONY: serve-docs
serve-docs:  ## Serve docs
	mkdocs serve


.PHONY: netlify
netlify:  ## Build docs on Netlify
	$(MAKE) docs

# ------------------------------------------------------------------------------
# Project specific
