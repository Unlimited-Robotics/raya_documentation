=========
Set color
=========

This function sets a particular group to a color (see Check the :doc:`list <../../../../robots/gary/leds_colors>` of colors with get_colors).

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

Sets the ``head`` group of leds to the color ``red`` (see hex values with :doc:`get_colors() <../../../../robots/gary/leds_colors>`). Code:

.. code:: python

   self.leds.set_color(group = 'head', color = 'red')
