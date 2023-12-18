List of Sensors
===============

Continuous sensors
-------------------

================= ====== ====================== ================ ============ =====================
Group             Sensor Available in simulator Magnitude        Unit         Path
================= ====== ====================== ================ ============ =====================
Version Name      No     Yes                    \*               String       ``/version_name``
Accelerometer X   Yes    Yes                    Acceleration     G’s (m/s²)   ``/accelerometer/x``
Accelerometer Y   Yes    Yes                    Acceleration     G’s (m/s²)   ``/accelerometer/y``
Accelerometer Z   Yes    Yes                    Acceleration     G’s (m/s²)   ``/accelerometer/z``
Gyro X            Yes    Yes                    Angular Velocity rad/s        ``/gyro/x``
Gyro Y            Yes    Yes                    Angular Velocity rad/s        ``/gyro/y``
Gyro Z            Yes    Yes                    Angular Velocity rad/s        ``/gyro/z``
Nicla Temperature Yes    No                     Temperature      °C           ``/nicla_temp``
Gas Value         Yes    Yes                    \*               Integer      ``/gas_value``
Rotation X        Yes    Yes                    Degrees          °            ``/rotation/x``
Rotation Y        Yes    Yes                    Degrees          °            ``/rotation/y``
Rotation Z        Yes    Yes                    Degrees          °            ``/rotation/z``
Rotation W        Yes    Yes                    Degrees          °            ``/rotation/w``
Temperature #0    Yes    Yes                    Temperature      °C           ``/temperature/0``
Temperature #1    Yes    Yes                    Temperature      °C           ``/temperature/1``
Temperature #2    Yes    Yes                    Temperature      °C           ``/temperature/2``
Temperature #3    Yes    Yes                    Temperature      °C           ``/temperature/3``
Ultrasonic #0     Yes    Yes                    Distance         Meters       ``/srf/0``
Ultrasonic #1     Yes    Yes                    Distance         Meters       ``/srf/1``
Ultrasonic #2     Yes    Yes                    Distance         Meters       ``/srf/2``
Ultrasonic #3     Yes    Yes                    Distance         Meters       ``/srf/3``
Ultrasonic #4     Yes    Yes                    Distance         Meters       ``/srf/4``
Ultrasonic #5     Yes    Yes                    Distance         Meters       ``/srf/5``
Ultrasonic #6     Yes    Yes                    Distance         Meters       ``/srf/6``
Emergency button  Yes    No                     \*               Boolean      ``/emergency_button``
Chest button      Yes    No                     Time             Integer (ms) ``/chest_button``
Charger pad       Yes    No                     \*               Integer      ``/charger_pad``
Cart sensor #1    Yes    No                     \*               Integer      ``/cart_sensor/1``
Cart sensor #2    Yes    No                     \*               Integer      ``/cart_sensor/2``
================= ====== ====================== ================ ============ =====================


Sensors distribution in Gary
----------------------------


.. image:: ../../../_static/sensors.png
    :width: 1280
    :height: 964
    :alt: Gary sensors