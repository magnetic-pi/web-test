web-test
========

##Requirements
python
pip

##Getting Started
1. Create a virtualenv

    virtualenv func_test

2. CD into the virtualenv that was just created. Clone the repo into the vrtualenv:

    git clone https://github.com/jcostello84/web-test.git

3. CD to the web-test directory.

    cd web-test/

4. Install the required packages.

    pip install -r requirements.txt

5. To run the tests individually cd to the tests/ directory but DO NOT include the .py extension.

    python -m unittest testname (without the .py)

6. To run the entire suite of tests, cd to web-test root and execute the runAll.py file. This should only be ran if the testing environment
is set up for parallel testing with sauce labs.

    python run_all.py
