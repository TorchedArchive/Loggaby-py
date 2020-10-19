echo Running package publish script..
py setup.py sdist bdist_wheel
py -m twine upload dist/*