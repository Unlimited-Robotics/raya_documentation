Sound exceptions
================

+-------------------------------------------------+-------------------------------------------------+
| Exception                                       | Condition                                       |
+=================================================+=================================================+
| RayaSoundErrorRecording                         | Problem when trying to record from the robot.   |
+-------------------------------------------------+-------------------------------------------------+
| RayaNeedCallback                                | No callback specified (sync or async).          |
+-------------------------------------------------+-------------------------------------------------+
| RayaApplicationException                        | Command was not accepted properly: Of path,     |
|                                                 | data, and name, one and only one can be used.   |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundWrongName                              | Wrong predfined sound name.                     |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundWrongPath                              | Wrong path file.                                |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundErrorPlayingAudiofile                  | File corrupted or device problem processing     |
|                                                 | data in the robot.                              |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundErrorPlayingAudio                      | Data sent to robot could not be played.         |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundBufferNotFound                         | Buffer not found.                               |
+-------------------------------------------------+-------------------------------------------------+
| RayaCommandNotRunning                           | Command not running                             |
+-------------------------------------------------+-------------------------------------------------+
| RayaSoundErrorPlayingAudio                      | No sound currently playing.                     |
+-------------------------------------------------+-------------------------------------------------+