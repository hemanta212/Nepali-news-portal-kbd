### Setting up a Virtual Environment
Venv is provided with the default installation of python since python 3.4 and above.

* Make a virtual environment:
```
python -m venv venv
```

* Activate it

- For Windows:
```
venv\Scripts\activate
```

- For Linux/Mac/(other Unix):
```
source venv/bin/activate
```

Once activated you can use regular python and pip commands and it will operate under your local project.

You can verify this by running 
```
$ where python # for Windows
$ which pip python # for others
```

NOTE: This applies to not only pip and python but also other python scripts like black, pylint, etc 

After finishing your work you can simply use the ```deactivate``` command to deactivate your virtual environment and use the system's version of pip and python.

Similarly closing the current terminal window also deactivates it.


