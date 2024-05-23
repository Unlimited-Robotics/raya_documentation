=========
Animation
=========

A method that will play a specified animation on the specified group.

Reference
=========

Arguments
---------

================= ============ =================================================== ================================================================================================
Arguments         Type         Default value                                       Explanation
================= ============ =================================================== ================================================================================================
group             ``string``                                                       name of the predefined LED's group.
color             ``string``                                                       name of the predefined LED's color.
animation         ``string``                                                       name of the predefined LED's animation you want to play.
speed             ``int``      1                                                   sets the speed that the animation will play, 0 is not allowd.
repetitions       ``int``      1                                                   number of the times the animation will play. if set 0 - the animation will play forever.
execution_control ``enum``     :ref:`OVERRIDE <LEDS_EXECUTION_CONTROL.OVERRIDE>`   See :doc:`enumerations <../enumerations>` to set the animation to be overridden.  
callback_feedback ``callable`` ``None``                                            If you define a feedback callback, it will receive feedback during the movement.
callback_finish   ``callable`` ``None``                                            If you define a finish callback, it will be called when the movement finishes or is interrupted.
================= ============ =================================================== ================================================================================================



Return
------

``None``

Exceptions
----------

-  ``RayaLedsWrongGroup``
-  ``RayaLedsWrongColor``
-  ``RayaLedsWrongAnimationName``
-  ``RayaLedsWrongRepetitions``
-  ``RayaLedsWrongSpeed``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
=============

Give an order for UR robot to play an animation on the head led, with the color red, at the default
speed of 1, and do it once.

.. code:: python

   leds.animation(group = 'head', color= 'red', animation= 'waiting', speed=1, repetitions= 1)

Notice:
-------

If no speed was specified, the default speed would be 1. setting repetitions = 0 will make the robot
play the animation indefinitely
