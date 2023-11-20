| Number |Message |Description|
| --- | --- |---|
| 1  | Custom command feedback | Indicates that the feedback from a custom command is being received |

| Exception |  Condition |
| --- | --- |
| `RayaLedsException` |Command was not accepted properly. |
| `RayaLedsWrongGroup` |Invalid group name (the group name doesn't exist).|
| `RayaLedsWrongColor` |Invalid color name (the color name doesn't exist).|
| `RayaLedsWrongAnimationName` |Invalid animation name (the animation doesn't exist).|
| `RayaLedsWrongRepetitions` |Invalid repetitions (incorrect repetitions number).|
| `RayaLedsWrongSpeed` |Invalid speed number (incorrect speed number).|

### LEDS_EXECUTION_CONTROL
Enumeration to set the animation to be overriden.

* `LEDS_EXECUTION_CONTROL.OVERRIDE`: Overide current animation
* `LEDS_EXECUTION_CONTROL.ADD_TO_QUEUE` : Insert animation to serial queue
* `LEDS_EXECUTION_CONTROL.AFTER_CURRENT` : Run animation at the end of current animation