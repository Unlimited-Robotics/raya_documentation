================
Sound Controller
================

Overview
========

Sounds controller allows playing predefined and custom sounds in the robot. It also allows recording to a file or variable.

List of pre-defined sounds
==========================

You can find a list of predefined sounds, including suggested use cases for each of them under :doc:`this section <../sound/synchronous_methods/get_predefined_sounds>`.

Using the controller
====================

Creating the controller in your app:

.. code:: python

   from raya.application_base import RayaApplicationBase

   class RayaApplication(RayaApplicationBase):
       async def setup(self):
           ...
           self.sound = await self.enable_controller('sound')
           ...

Example
=======

-  `Sound play custom <https://github.com/Unlimited-Robotics/pyraya_examples/blob/main/sound_play_custom/src/app.py>`__
-  `Sound play predefined <https://github.com/Unlimited-Robotics/pyraya_examples/blob/main/sound_play_predefined/src/app.py>`__
-  `Sound record and play <https://github.com/Unlimited-Robotics/pyraya_examples/tree/main/sound_record_and_play>`__
-  `Sound record and save <https://github.com/Unlimited-Robotics/pyraya_examples/tree/main/sound_record_save>`__


Sound controller methods
========================

.. toctree::
   :maxdepth: 2

   Asynchronous methods <asynchronous_methods/index>
   Synchronous methods <synchronous_methods/index>
   Handlers <handlers/index>
   Exceptions <exceptions>
   Feedbacks <feedbacks>
