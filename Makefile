test:
	poetry run test-script

build:
	poetry build

publishdr:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
	