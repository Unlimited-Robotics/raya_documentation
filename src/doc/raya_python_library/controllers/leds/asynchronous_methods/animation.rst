=========
Animation
=========

.. rayadocumentationfunction:: /controllers/leds_controller.py animation
See the :doc:`complete exceptions <../exceptions>`.

Usage example
-------------

Give an order for UR robot to play an animation on the head led, with the color red, at the default
speed of 1, and do it once.

.. code:: python

   leds.animation(group = 'head', color= 'red', animation= 'waiting', speed=1, repetitions= 1)

Notice
------

If no speed was specified, the default speed would be 1. setting repetitions = 0 will make the robot
play the animation indefinitely
