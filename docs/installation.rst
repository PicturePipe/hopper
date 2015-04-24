************
Installation
************

Development Setup
=================

Install the packages for development::

    $ make develop

Before creating the database install PostgreSQL extension hstore::

    $ psql -d template1 -c 'create extension hstore;'

Then create the new PostgreSQL user and database::

    $ make create-db

Now create the database tables::

    $ make migrate

And start the development webserver::

    $ make runserver

To see the other targets available in the ``Makefile`` simply run::

    $ make
