==============
Turn off group
==============

This function sets a particular group to a color (see list of colors with get_colors).

Reference
=========

Arguments
---------

========= ========== ===================================
Arguments Type       Explanation
========= ========== ===================================
group     ``string`` Name of the predefined LED's group.
color     ``string`` Name of the predefined LED's color.
========= ========== ===================================

Return
------

``None``

Exceptions
----------

-  ``RayaLedsWrongGroup``
-  ``RayaLedsWrongColor``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

Sets the ``head`` group of leds off. Code:

.. code:: python

   self.leds.turn_off_group(group = 'head')
