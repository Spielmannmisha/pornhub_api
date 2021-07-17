test:
	poetry3 -m pytest

build:
	poetry build

publishdr:
	poetry publish --dry-run

publish:
	poetry publish

package-install:
	python3 -m pip install --user dist/*.whl
	
	