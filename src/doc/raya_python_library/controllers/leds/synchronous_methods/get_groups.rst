==========
Get groups
==========

Returns a List type string with all the leds groups name.

Reference
=========

Check the :doc:`LED's groups list <../../../../robots/gary/leds_colors>`.

Return
------

``List`` a list types string that containes all the avilable groups.

Exceptions
----------

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

Get all the groups of all led's:

.. code:: python

   self.log.info(self.leds.get_groups())

output:

.. code:: python

   ['head', 'sensors', 'skirt', 'chest']
