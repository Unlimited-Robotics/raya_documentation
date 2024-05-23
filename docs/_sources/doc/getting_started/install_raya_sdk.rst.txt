Install Ra-Ya SDK
=================

The Ra-Ya SDK is a python package that allows to execute various commands from the CLI, this tool helps you to create apps, debug code and executing it in a real robot

Operating Systems
-----------------

The Ra-Ya SDK is currently compatible with the following operating systems:

+---------+--------------------------------------------+
| **OS**  | **Version (tested)**                       |
+=========+============================================+
| Linux   | Ubuntu 18.04, Ubuntu 20.04, and derivated. |
+---------+--------------------------------------------+
| macOS   | Ventura                                    |
+---------+--------------------------------------------+
| Windows | 10, 11                                     |
+---------+--------------------------------------------+


.. note::
    
    * Linux compilation of Ra-Ya SDK is a completely static build, so it should work with most of the recent Linux distributions over anaconda virtual environments.

Requirements
------------

Python
^^^^^^

You need an installed version of Python 3.8.10.

Docker
Install Docker and verify that you can execute commands without sudo:

* `Ubuntu 18.04 (steps 1 + 2) <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04>`_
* `Ubuntu 20.04 (steps 1 + 2) <https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04>`_
* `Other distros <https://docs.docker.com/engine/install/>`_
* `Windows <https://docs.docker.com/desktop/windows/install/>`_

Install
-------

The packages are hosted using PyPi

* `Ra-Ya SDK package <https://pypi.org/project/rayasdk/>`_
* `Ra-Ya Python library package <https://pypi.org/project/raya/>`_

In order to install it execute:

.. code-block:: bash

    python3 -m pip install rayasdk raya

``raya`` is a requirement of ``rayasdk``, but it always tries to download the last “release” version, to install a \
“pre-release” version, you must explicitly define the version, to check if the installation was correct open a new terminal and run:

.. code-block:: python

    rayasdk

This should output:

.. code-block:: bash

    usage: rayasdk [-h] [-v | -q]
               {init,scan,connect,run,simulator,kill,update} ...
    rayasdk: error: the following arguments are required: command

Well done! the environment is ready and we can start creating your first robotics app!