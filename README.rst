====================
django-intensedebate
====================

A simple integration of the `IntenseDebate <http://intensedebate.com>`_ comment widget for Django projects.

Requirements
============

- Python 2.5+
- Django 1.4+

Installation
============

#.  Install the latest stable version using ``pip``:

    .. code:: shell

        pip install django-intensedebate

#.  Add ``intensedebate`` to your ``INSTALLED_APPS`` setting:

    .. code:: python

        INSTALLED_APPS = (
            ...
            'intensedebate',
        )

Configuration
=============

The ``intensedebate_config`` template tag requires a site *account number*. Either pass it as ``intensedebate_acct``, or set ``INTENSEDEBATE_ACCT`` in your settings:

  .. code:: python

      INTENSEDEBATE_ACCT = xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

The site *account number* can be found by visiting the `Site Key <http://intensedebate.com/sitekey>`_ page (**IntenseDebate site acct:**).

Basic Usage
===========

#.  Load the tag library:

    .. code:: html

        {% load intensedebate %}

#.  Set the config:

    .. code:: html

        {% intensedebate_config post_id=OBJECT_ID %}

    You can pass these options as arguments:

    ============================ ============================
    Option                       Default
    ============================ ============================
    intensedebate_acct           None (required or see configuration above)
    post_id                      None (required, should be unique)
    post_url                     None (inferred)
    post_id_prefix               ""
    post_id_suffix               ""
    ============================ ============================

#.  Create a container in your html body to be used by the intensedebate
    widget. It should have ``idc-container-parent`` as an id:

    .. code:: html

        <div id="idc-container-parent"></div>

#.  Load the widget:

    .. code:: html

        {% intensedebate_load %}


Example
=======

.. code:: html

    {% load intensedebate %}


    <!DOCTYPE HTML>

    <html>

    <head>
      <meta charset="utf-8">
      <title>django-intensedebate Example</title>

      {% intensedebate_config post_id=object.id post_id_prefix='pid_' %}
    </head>

    <body>
      <p>Well, the way they make shows is, they make one show. That show's
      called a pilot. Then they show that show to the people who make shows,
      and on the strength of that one show they decide if they're going to
      make more shows. Some pilots get picked and become television programs.
      Some don't, become nothing. She starred in one of the ones that became
      nothing.</p>

      <div id="idc-container-parent"></div>

      <!-- Placed at the end of the document so the pages load faster -->
      {% intensedebate_load %}
    </body>

    </html>
