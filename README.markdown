###### RSA

`modularmath.py` contains a bunch of helper methods implementing efficient
modular operations, needed to implement encryption using RSA keys. Padding the
text is done in `padstring.py`. `librsa.py` uses these modules and does
encryption by hand, while decryption and keys generation is done by
**PyCrypto**.

###### Setup:

Scripts assume you've got your Python environment in `./env`. Get
[`virtualenv`](http://pypi.python.org/pypi/virtualenv) and do:

    $ cd path/to/project
    $ virtualenv env
    $ ./env/bin/pip install pycrypto bitarray

###### Testing:

    $ ./modularmath.py
    $ ./padstring.py
    $ ./librsa.py

###### Credits:

Most if not all methods in `modularmath.py` were copied from
[Wikibooks](http://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics).
