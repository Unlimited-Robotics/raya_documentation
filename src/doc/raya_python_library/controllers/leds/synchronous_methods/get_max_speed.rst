=============
Get max speed
=============

Each groups of leds can play the animation in different speeds. This function allows you to get the
maximum available speed for the specified group.

Reference
=========

Arguments
---------

========= ========== ============= ==================================
Arguments Type       Default value Explenation
========= ========== ============= ==================================
group     ``string`` ``None``      Name of the predefined LED's group
========= ========== ============= ==================================

Return
------

``int`` The maximum speed allowed.

Exceptions
----------

-  ``RayaLedsWrongGroup``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

Print the maximum speed allowed to play an animation of the ``head`` group

.. code:: python

   self.log.info(leds.get_max_speed(group = 'head'))

Console output:

.. code:: python

   17
