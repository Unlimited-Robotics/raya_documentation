Overview
========

This section describes how to create a simple Ra-Ya app.

We are going to create an application that is going to be executed on a real robot, For now we are
going to test that everything is installed correctly with a Hello world example.

Download or update the simulator
--------------------------------

The Ra-Ya SDK have a command to download the necesary files to run the simulation, open a terminal
and execute:

.. code:: bash

   rayasdk update

The SDK will check if you have any version already on the system if not it will download it for you,
if the update was ok the output should be:

.. code:: bash

   SUCCESS: Raya_OS updated successfully
   SUCCESS: Everything is up to date

Open & activate the simulator
-----------------------------

Once the simulator is downloaded execute this command on a terminal:

.. code:: bash

   rayasdk simulator

This command will execute the Ra-Ya OS locally on your system and will open the simulator, if is the
first time that the simulator is being run it will ask you for a user, just follow the steps and log
in, **DO NOT CLOSE THE TERMINAL THAT IS RUNNING THE SIMULATION**, if you do you will have to kill
the Ra-Ya OS container and make sure that there is not a process running on the background.

Connecting to the simulation
----------------------------

Open a new terminal and execute this:

.. code:: bash

   rayasdk connect --simulator

The command can prompt you to do certain actions, Once that the connection is successfully you
should see

.. code:: bash

   You have successfully connected to the simulator

The connection is only necesary the first time, just make sure that the Ra-Ya OS is running on your
system.

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

The app will be sync to the Ra-Ya OS and is going to be launched, you should see on the output this

.. code:: bash

   Syncing the app on the simulation...
   Launching app...
   (INFO)<RayaApp.app.hello_world> Hello from setup()
   (INFO)<RayaApp.app.hello_world> Hello world
   (WARNING)<RayaApp.app.hello_world> Hello from finish()

Congratulations you just executed an app.
