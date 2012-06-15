Django integration
==================

Usage
-----

Simply install natural and put it in your ``INSTALLED_APPS``:

.. code-block:: django

    INSTALLED_APPS += ('natural',)


Now you can use all features from the natural lib in your templates:

.. code-block:: html+django

    {% load naturalise %}
    CPU load is: {{ percent|percentage:1 }}
    Average load {{ load|sparkline }}
    ...


Alternatively, you may use ``naturalize`` if you feel it's more appropriate:

.. code-block:: html+django

    {% load naturalize %}
    ...


API
---

.. automodule:: natural.templatetags.naturalise
    :members:
    :undoc-members:
    :show-inheritance:

