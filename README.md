web-test
========

##Requirements
python
pip

##Getting Started
1. Clone the repo:

    git clone https://github.com/jcostello84/web-test.git

2. CD to the web-test directory.

    cd web-test/

3. Install the required packages.

    sudo pip install -r requirements.txt

4. To run the tests individually cd to the tests/ directory but DO NOT include the .py extension.
	
    python -m unittest <testname>

5. To run the entire suite of tests, cd to /tests and execute the runAll.py file.

    python runAll.py
