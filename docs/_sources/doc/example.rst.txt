This is a heading
==================

This is an introduction paragraph.

A subheading here
---------------------

I am *italic* and I am **bold**. I am an ``x,y = 2,3`` an inline code example.

An unordered list of items:

* item a
* item b
* item c

An ordered list of items:

#. first item
#. second item
#. third item

A code example::

    import sys
    import os
    print('Hello world')

.. image:: ../_static/logo.png

A list can be nested.

* fruits
* vegetables
  
  * broccoli
  * peas
* cereals (continuing first level list)

.. list-table:: Title
   :widths: 25 25 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
     - Heading row 1, column 3
   * - Row 1, column 1
     -
     - Row 1, column 3
   * - Row 2, column 1
     - Row 2, column 2
     - Row 2, column 3

Here is an external link to `Python <https://www.python.org/>`_.

.. rayadocumentationfunction:: /controllers/leds_controller.py get_groups
.. rayadocumentationfunction:: /controllers/leds_controller.py get_colors
.. rayadocumentationfunction:: /controllers/leds_controller.py get_animations
.. rayadocumentationfunction:: /controllers/leds_controller.py get_max_speed