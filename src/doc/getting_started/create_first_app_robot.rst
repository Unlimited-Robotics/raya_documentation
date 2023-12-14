Overview
========

This section describes how to create a simple Ra-Ya app.

We are going to create an application that is going to be executed on a real robot, For now we are
going to test that everything is installed correctly with a Hello world example.

Connecting to the robot
-----------------------

Let's start verifying that the robot is connected to the network, with the SDK installed open a new
terminal and run

.. code:: bash

   rayasdk scan

This will output a table with the available robots on the network, the output should look like this

.. code:: bash

   Press enter to exit...

   Robot ID              Serial                IP Address
   --------------------  --------------------  --------------
   JETSON_ORIN_BOGOTA    JETSON_ORIN_BOGOTA    172.xxx.xxx.xxx
   JETSON_XAVIER_BOGOTA  JETSON_XAVIER_BOGOTA  192.168.xxx.xxx
   GARYV2_OFFICE_08      SN-08                 172.xxx.xxx.xxx

Once that you see that the robot that you want to connect is present on the list, execute this

.. code:: bash

   rayasdk connect --robot-id GARYV2_OFFICE_08

In case that the robot appears multiple times you will have to define the IP that should be use on
the connection with

.. code:: bash

   rayasdk connect --robot-ip 192.168.xxx.xxx

The command can prompt you to do certain actions, Once that the connection is successfully you
should see

.. code:: bash

   You have successfully connected to GARYV2_OFFICE_08

The connection is only necesary the first time, or each time that you want to run the application on
a different robot, **In case that the connection failed make sure that the robot is running Ra-Ya OS
and is connected to your network.**

Creating the app
----------------

An Ra-Ya app need a structure in order to execute, The SDK will help you with this, open a terminal
and execute:

.. code:: bash

   mkdir hello_world
   cd hello_world
   rayasdk init

Now you should see that the folder contains files and directories, open with any editor the file
``app.py`` inside the ``src`` directory, replace the content with the following code:

.. code:: python

   from raya.application_base import RayaApplicationBase

   class RayaApplication(RayaApplicationBase):

       async def setup(self):
           # Create local attributes and variables
           self.log.info(f'Hello from setup()')

       async def loop(self):
           # Loop
           self.log.info('Hello world')
           self.finish_app()

       async def finish(self):
           # Finishing instructions
           self.log.warn(f'Hello from finish()')

Run your app
------------

You just wrote your first Ra-Ya app. It’s time to run it!

Open a terminal and go to the project folder, and execute:

.. code:: bash

   rayasdk run

The app will be sent to the robot and is going to be launched, you should see on the output this

.. code:: bash

   Syncing the app on the host 'rayadevel@172.xxx.xxx.xxx'...
   Launching app...
   (INFO)<RayaApp.app.hello_world> Hello from setup()
   (INFO)<RayaApp.app.hello_world> Hello world
   (WARNING)<RayaApp.app.hello_world> Hello from finish()

Congratulations you just executed an app.
