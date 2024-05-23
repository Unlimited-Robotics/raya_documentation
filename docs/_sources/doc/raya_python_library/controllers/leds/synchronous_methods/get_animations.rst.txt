==============
Get animations
==============

Returns a list with all the available animations for a specified group.

Reference
=========

Arguments
---------

========= ========== ============= ===================================
Arguments Type       Default value Explanation
========= ========== ============= ===================================
group     ``string`` ``None``      Name of the predefined LED's group.
========= ========== ============= ===================================

Return
------

``list`` A list with all the available animations for a specified group.

Exceptions
----------

-  ``RayaLedsWrongGroup``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

Print a list of all available animations for the chest leds. Code:

.. code:: python

   self.log.info(self.leds.get_animations('chest'))

Console output:

.. code:: python

   ['standby', 'waiting', 'loading', 'searching']
