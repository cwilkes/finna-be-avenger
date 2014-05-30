Setup
-----

virtualenv-2.7 venv
. venv/bin/activate
pip install -r requirements.txt


Notes
-----

If you add something via pip do
  pip freeze > requirements.txt
check that in.  Then others can easily download those modules with the install command above

scipy looks like it requires gfortran.  With brew you can get that with "brew install gcc".


kNN example using numpy scipy:
http://insideourminds.net/python-simple-k-nearest-neighbours-classifier/
