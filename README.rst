====================
Django IntenseDebate
====================

This project is a simple integration of the IntenseDebate comment widget for
quick implementation in Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#. Add the ``intensedebate`` directory to your Python path. Using ``pip``::

       pip install "git+https://bitbucket.org/raymondwanyoike/django-intensedebate.git#egg=django-intensedebate"

#. Add ``intensedebate`` to your ``INSTALLED_APPS`` setting::

       INSTALLED_APPS = (
           ...
           'intensedebate',
       )

Configuration
=============

#. TODO

Basic Usage
===========

#. TODO

Example
=======

::

    {% load intensedebate %}

    <html>
      <head>
        <title>Full Example</title>
        {% intensedebate_config post_id=object.id post_id_prefix='pid_' %}
        {% intensedebate_cw %}
      </head>
      <body>
        <div id="idc-container-parent"></div>
      </body>
    </html>
