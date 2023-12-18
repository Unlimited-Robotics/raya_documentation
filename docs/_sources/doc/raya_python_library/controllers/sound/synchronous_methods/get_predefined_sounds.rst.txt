Get predefined sounds
=====================

Returns a list with all the prederfined sounds that can be played.

Arguments
---------

``None``

Return
------

======== ================================
Type     Description
======== ================================
``List`` List of predefined sounds names.
======== ================================

Usage example
-------------

Code:

.. code:: python

   from raya.application_base import RayaApplicationBase

   class RayaApplication(RayaApplicationBase):
       async def setup(self):
           self.sound = await self.enable_controller('sound')

       async def loop(self):
                   self.sounds =  self.sound.get_predefined_sounds()
           print(self.sounds)
           self.finish_app()

       async def finish(self):
           self.log.info(f'Hello from finish()')

Console output:

.. code:: python

   ['happy', 'finish_task', 'on_the_go']
