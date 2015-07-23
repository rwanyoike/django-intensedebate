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

#.  Create a container (see ``container_id``) in your html body to display the widget:

    .. code:: html

        <div id="intensedebate"></div>

#.  Load the widget:

    .. code:: html

        {% intensedebate_load %}

    You can pass these options as arguments:

    ========================= ========================= =========================
    Option                    Default                   Description
    ========================= ========================= =========================
    intensedebate_acct                                  Site *account number* (see configuration above).
    post_id *                 ``window.location.href;`` Unique identifier of the post. This is what keeps the comments set on this post different than comments set on another post. The default value is the URL of the page.
    post_id_prefix                                      ``post_id`` prefix.
    post_id_suffix                                      ``post_id`` suffix.
    post_url                  ``window.location.href;`` URL of the post. This is the URL IntenseDebate will link to in RSS feeds and on `intensedebate.com <http://intensedebate.com>`_.
    post_title                ``document.title;``       Title of the post. This is the title that will be displayed in RSS feeds and on `intensedebate.com <http://intensedebate.com>`_.
    container_id                                        The container to display the widget. **Warning:** If not defined, IntenseDebate will create a container ``id="idc-container-parent"`` above the ``intensedebate_load`` template tag.
    ========================= ========================= =========================

    - ``post_id`` ensures the correct comments are associated with the correct post. It should be unique, e.g ``object.id`` (to avoid conflict with other id's, use ``post_id_prefix`` and ``post_id_suffix``).

Example
=======

.. code:: html

    {% load intensedebate %}


    <!DOCTYPE HTML>

    <html>

    <head>
      <meta charset="utf-8">
      <title>django-intensedebate Example</title>
    </head>

    <body>
      <p>Well, the way they make shows is, they make one show. That show's
      called a pilot. Then they show that show to the people who make shows,
      and on the strength of that one show they decide if they're going to
      make more shows. Some pilots get picked and become television programs.
      Some don't, become nothing. She starred in one of the ones that became
      nothing.</p>

      <div id="intensedebate"></div>

      <!-- Placed at the end of the document so the page loads faster -->
      {% intensedebate_load post_id=object.id post_id_prefix='pid_' container_id='intensedebate' %}
    </body>

    </html>
