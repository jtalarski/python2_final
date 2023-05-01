"""
Name: Jim Talarski
Course: CIS289 23227
Assignment: FINAL PROJECT
"""

** READ  ME **

NOTE: This application was built using Python version 3.12. Backwards compatibility was
not tested and is not guaranteed.These instructions assumes reader has working knowledge
of Python its basic libraries, and Django framework. If you do not have a working
knowledge the internet is your friend.


REQUIRED SOFTWARE INSTALLATION:
- Python programming libraries - Assumed most users will already have this
installed on their machine. Web search will provide installation instructions

- Python pip installer program. Use terminal, command prompt, or Powershell. To install
	- Linux/macOS: python get-pip.py
	- Windows: py get-pip.py

- Python virtual environment management application. Use terminal, command prompt,
or Powershell. To install
	- Linux/macOS: python3 -m pip install --user virtualenv
	- Windows: py -m pip install --user virtualenv

- Activate provided virtual environment contained in directory where you extracted
files from the zipped archive.
	- Linux/macOS: source env/bin/activate
	- Windows: .\env\Scripts\activate

- You can confirm you’re in the virtual environment by checking the location of your
Python interpreter. It should be in the env directory of the applications base directory
to which you extracted the zipped archive files
	- Linux/macOS: which python
	- Windows: where python

- Use pip to install required Python packages/libraries/modules using the provided file
requirements.
	- Linux/macOS: python3 -m pip install -r requirements.txt
	- Windows: py -m pip install -r requirements.txt


RUNNING THE PROGRAM:
- From the applications base directory to which you extracted the zipped archive files
	- python3 manage.py runserver
	- Open browser to provided link http://127.0.0.1:8000//
	- Interact with the Django web application and have fun


API ACCESS - Assumes reader has working knowledge of making API requests
- Basic API directory  http://127.0.0.1:8000/pizza_pi2/
	- To use the curl terminal program enter this command on one line without quotations
		- "curl -H 'Accept: application/json; indent=4' -u
		guest_chef:guest1234 http://127.0.0.1:8000/pizza_pi2/"
	- Sample JSON object (dictionary) that is returned
		  {
        "title": "New York Pepperoni",
        "description": "Make dough, form pizza, add sauce, add pepperoni, add cheese",
        "directions": "",
        "current_rating": 0,
        "author": 1
    	}


