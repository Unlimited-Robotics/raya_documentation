================
LED's Controller
================

Overview
========

This controller allows you to manipulate all the leds groups that exist in the robotic device. For example, Gary has leds in the head area, around the button, next to the sensors and in the bottom of the skirt.

Please notice that if you set animation repetition to zero, it will continue to play indefinitely.

Main arguments:
===============

========= =========================================================================================================================================================================================================================
Name      Description
========= =========================================================================================================================================================================================================================
Group     groups represent the area of leds that you want to manipulate. For example, “head” group will be used to play a led interaction in the head area.
Color     the LEDS can be displayed in different colors. In order to see the entire list of possible colors, please visit :doc:`this <../../../robots/gary/leds_colors>`.
Animation For each group area, there are several animations that can be used in order to interact with the end-users. For example, “waiting” animation for head group will display a line moving from left to the right of the head
========= =========================================================================================================================================================================================================================

Using the Controller
====================

.. code:: python

   from raya.application_base import RayaApplicationBase

   class RayaApplication(RayaApplicationBase):
       async def setup(self):
       ...
           self.leds = await self.enable_controller('leds')
        ...

Each method page includes standalone examples of their use.

Example
=======

-  `LEDS usage example <https://github.com/Unlimited-Robotics/pyraya_examples/blob/main/leds/src/app.py>`__


Leds controller methods
=======================

.. toctree::
   :maxdepth: 2

   Asynchronous methods <asynchronous_methods/index>
   Synchronous methods <synchronous_methods/index>
   Exceptions <exceptions>
   Feedbacks <feedbacks>
   Enumerations <enumerations>