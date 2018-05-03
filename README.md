# Password Strength Calculator

This script allows to calculate a password strength with a score from 1 (very poor password) to 10 (very strong password).

# Quickstart

For script launch need to install Python 3.5 and then install all dependencies:

```

$ pip install -r requirements.txt

```

Usage:

```

$ python3 password_strength.py -h
usage: password_strength.py [-h] password

positional arguments:
  password    a password for analysis

optional arguments:
  -h, --help  show this help message and exit

```

Examples of script launch on Linux:

```

$ python3 password_strength.py 123456789
------------------------------------
Score of password strength:  1 of 10
------------------------------------

$ python3 password_strength.py password1
------------------------------------
Score of password strength:  2 of 10
------------------------------------

$ python3 password_strength.py PaSsWoRd1
------------------------------------
Score of password strength:  4 of 10
------------------------------------

$ python3 password_strength.py r4Bh34Aq1
------------------------------------
Score of password strength:  9 of 10
------------------------------------

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
