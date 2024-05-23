Play Sound
==========

This function plays a sound from the data given in its arguments. This function is recommended to
play sound.

These 3 parameters are mutually exclusive `Name = Play a predefined sound by his name`,  `Path = Play a
file by his path`, `Data = Play an audio reading as a raw data`, an object of the
:doc:`SoundData <../handlers/sound_data_object>` type imported from SoundController must be created.

Arguments
---------

+------------------------+------------------------+------------------------+------------------------+
| Arguments              | Type                   | Default Value          | Description            |
+========================+========================+========================+========================+
| name                   | ``str``                | ``None``               | Predefined sound’s     |
|                        |                        |                        | name.                  |
+------------------------+------------------------+------------------------+------------------------+
| path                   | ``str``                | ``None``               | Play a sound from its  |
|                        |                        |                        | file path.             |
+------------------------+------------------------+------------------------+------------------------+
| data                   | ``any``                | ``None``               | Play a sound using raw |
|                        |                        |                        | audio data (SoundData  |
|                        |                        |                        | object).               |
+------------------------+------------------------+------------------------+------------------------+
| volume                 | ``int``                | 100                    | Volume from 1-100.     |
+------------------------+------------------------+------------------------+------------------------+
| callback_feedback      | ``callable``           | ``None``               | If you define a        |
|                        |                        |                        | feedback callback, it  |
|                        |                        |                        | will receive feedback  |
|                        |                        |                        | during the movement.   |
+------------------------+------------------------+------------------------+------------------------+
| callback_finish        | ``callable``           | ``None``               | If you define a finish |
|                        |                        |                        | callback, it will be   |
|                        |                        |                        | called when the        |
|                        |                        |                        | movement finishes or   |
|                        |                        |                        | is interrupted.        |
+------------------------+------------------------+------------------------+------------------------+
| wait                   | ``bool``               | ``True``               | If ``True``, the code  |
|                        |                        |                        | will be blocked until  |
|                        |                        |                        | the end of the sound.  |
+------------------------+------------------------+------------------------+------------------------+

Return
------

``None``

Exceptions
----------

-  ``RayaSoundWrongName``
-  ``RayaSoundWrongPath``
-  ``RayaSoundErrorPlayingAudiofile``
-  ``RayaSoundErrorPlayingAudio``
-  ``RayaSoundBufferNotFound``

See the :doc:`complete exceptions <../exceptions>`.

Usage example
-------------

.. code:: python

   self.log.warn(f'Recording for {self.duration} seconds...')
           record = await self.sound.record_sound(
                   duration=self.duration, 
                   wait=True
               )
           print(record)
           self.log.warn('Record Finish')

           self.log.warn(f'Playing recording')
           await self.sound.play_sound(
                   data=record, 
                   volume=self.volume,
               )

Load file (WAV, MP3, OGG, AAC, etc) and play it
-----------------------------------------------

.. code:: python

   from raya.controllers.sound_controller import SoundController, SoundData


   class RayaApplication(RayaApplicationBase):

       async def setup(self):
           self.sound: SoundController = await self.enable_controller('sound')
           
           
       async def loop(self):
           wav_file = SoundData(coding_format='mp3')
           with open('./test_sound.mp3', mode='rb') as file: # b is important -> binary
               wav_file.data = file.read()
           await self.sound.play_sound(
                   data=wav_file, 
                   volume=100,
               )
           self.finish_app()


       async def finish(self):
           self.log.info(f'Hello from finish()')

Create 5 seconds 1KHz tone and play it
--------------------------------------

.. code:: python

   import numpy as np
   from raya.controllers.sound_controller import SoundController, SoundData


   class RayaApplication(RayaApplicationBase):

       async def setup(self):
           self.sound: SoundController = await self.enable_controller('sound')
           
           
       async def loop(self):
           sample_rate = 44100
           signal_frequency = 1000
           duration = 5
           data_volume = 50 # 0 - 100
           signal_amplitude = min(max(0, data_volume)*127/100,100)
           samples = np.linspace(0, duration, int(sample_rate*duration), endpoint=False)
           signal = signal_amplitude*np.sin(2 * np.pi * signal_frequency * samples) + 127
           tone_data = SoundData(
               channels=1,
               sample_rate=sample_rate,
               sample_format=SoundData.SAMPLE_U8,
               coding_format='pcm')
           tone_data.data = np.uint8(signal)
           await self.sound.play_sound(
                   data=tone_data
               )
           self.finish_app()


       async def finish(self):
           self.log.info(f'Hello from finish()')
