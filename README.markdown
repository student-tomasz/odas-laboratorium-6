###### Running:

This is a primitive, unfeasibly sluggish and memory devouring implementation of
RSA. Without any text padding, so it's not even semantically secure. Don't
bother using it with keys longer than `32` bits, you'll only regret it.

    $ ./my_rsa.py [key_length]

###### Setup:

Scripts assume you've got your Python environment in `./env`. Get
[`virtualenv`](http://pypi.python.org/pypi/virtualenv) and do:

    $ cd path/to/project
    $ virtualenv env
    $ ./env/bin/pip install pycrypto bitarray
