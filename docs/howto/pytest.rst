Use PyTest to run tests
#######################

.. warning:: 

    The tests are not yet complete. Tests are being written as we add new functionality to the module. We hope this will be completed soon.  
    
    If you want to contribute to the project, please consider writing tests for the module in the github repository.

* All tests are written using PyTest. To run the tests, you need to install PyTest and run the tests using the ``pytest`` command.
* All tests are located in the ``tests`` folder. The ``tests`` folder contains a ``conftest.py`` file that contains fixtures that are used by the tests.
* If you are using PyCharm, you can run the tests by right-clicking on the ``tests`` folder and selecting ``Run 'pytest in tests'``.
* All tests are written using the ``assert`` statement. If the assertion fails, the test fails.
* The tests use same structure of the module. For example, the tests for the ``blizzardAPI.world_of_warcraft.game_data`` module are located in the ``blizzardAPI\tests\world_of_warcraft\game_data`` folder.


Run all tests
*************

.. note:: 

    By default, the tests are setted up to use .env file to load the environment variables. If you not have a .env file, you can use the arguments to pass the environment variables to the tests. Read :doc:`here </howto/use_env_file>` for more information.

Using ``.env`` file
===================
To run all tests, run the following command from the root of the project folder where ``.env`` file is located with the following content:

.. code-block:: bash

    pytest blizzardAPI

Using specific keys
===================
To run all tests, run the following command from the root of the project folder:

.. code-block:: bash

    pytest blizzardAPI --client YOUR_CLIENT_ID --secret YOUR_SECRET --region YOUR_REGION

Run specific tests
******************

.. note:: 

    By default, the tests are setted up to use .env file to load the environment variables. If you not have a .env file, you can use the arguments to pass the environment variables to the tests. Read :doc:`here </howto/use_env_file>` for more information.

Using ``.env`` file
===================
To run all tests, run the following command from the root of the project folder where ``.env`` file is located with the following content:

.. code-block:: bash

    pytest blizzardAPI\tests\world_of_warcraft\game_data\test_reputation.py

.. code-block:: bash

    pytest blizzardAPI -k test_reputation

Using specific keys
===================
To run specific tests, run the following command from the root of the project folder:

.. code-block:: bash

    pytest blizzardAPI\tests\world_of_warcraft\game_data\test_reputation.py -client YOUR_CLIENT_ID --secret YOUR_SECRET --region YOUR_REGION

.. code-block:: bash

    pytest blizzardAPI -k test_reputation -client YOUR_CLIENT_ID --secret YOUR_SECRET --region YOUR_REGION