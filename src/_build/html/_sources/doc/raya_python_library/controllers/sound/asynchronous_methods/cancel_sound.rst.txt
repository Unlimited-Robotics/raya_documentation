============
Cancel Sound
============

Cancel current sound.

Arguments
=========

``None``

Return
======

``None``

Exceptions
==========

-  ``RayaCommandNotRunning``
-  ``RayaSoundErrorPlayingAudio``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

.. code:: python

           ...
           await self.sound.cancel_sound()
