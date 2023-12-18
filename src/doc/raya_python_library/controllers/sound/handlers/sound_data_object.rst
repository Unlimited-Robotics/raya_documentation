SoundData Object
=================

SoundData is a class that allows provide more information about the audio data that you want to play or that is recorded from the robot.

Attributes
----------
Data: Unsigned char array (0-255) containing the audio information.
Channels: number of data channels.
Sample rate: the number of samples taken per second.
Sample format: for raw, information about bytes configuration (see Constants).
Coding format: data format (MP3,WAV,PCM). PCM is used for raw.

Constants
---------
Raw format (PCM) allowed:

::
    
    SAMPLE_ALAW
    SAMPLE_F32BE
    SAMPLE_F32LE
    SAMPLE_F64BE
    SAMPLE_F64LE
    SAMPLE_MULAW
    SAMPLE_S16BE
    SAMPLE_S16LE
    SAMPLE_S24BE
    SAMPLE_S24LE
    SAMPLE_S32BE
    SAMPLE_S32LE
    SAMPLE_S8
    SAMPLE_U16BE
    SAMPLE_U16LE
    SAMPLE_U24BE
    SAMPLE_U24LE
    SAMPLE_U32BE
    SAMPLE_U32LE
    SAMPLE_U8
    SAMPLE_VIDC

Sample format by width (Used for PCM format)
With the number of bytes used to represent a sample, it's possible obtain the data format among the most common (SAMPLE_U8, SAMPLE_S16LE, SAMPLE_S24LE, SAMPLE_S32LE)

Example
-------
.. code-block:: python

    sample_format = SAMPLE_FORMAT_BY_WIDTH[2] # ( 2 bytes means 16 bits Signed little endian format )
    Sample width by format (Used for PCM format)
    With the format, it is possible to obtain the number of bits used to represent a sample

Example
-------
.. code-block:: python
    
    sample_width = SAMPLE_WIDTH_BY_FORMAT[SAMPLE_S32LE] # ( return 4 )

Class functions
---------------

clearData()
-----------

Clear stored values.

getSampleWidth()
----------------

``int`` Returns the sample width based on the format.
