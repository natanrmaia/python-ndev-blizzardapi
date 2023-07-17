Usage examples
###############

.. toctree::
   :caption: Table of Contents
   :maxdepth: 3

.. note:: 
    The examples below assume that you have already installed the package. For more information on how to install the package, see the :doc:`installation` section.


How to locale the specific api in the module
********************************************

The Blizzard API is divided into several sections, each of which is represented by a module in the package. For example, the World of Warcraft API is represented by the ``world_of_warcraft`` module. Each module contains a number of classes, each of which represents a specific API endpoint. For example, the ``world_of_warcraft.game_data.toy.get_toy_index`` class represents the ``/data/wow/toy/index`` endpoint. 

Ever call function starting with ``get_``. For example, ``get_toy_index``. The function name is the same as the endpoint name, but without the ``/data/wow`` part. More examples:

* ``/data/wow/toy/index`` -> ``get_toy_index``
* ``/data/wow/toy/{toyId}`` -> ``get_toy`` (with ``toyId`` as a parameter)

Using keys in .env file (default option)
**********************************************

By default, the package will look for the API key and secret key in a .env file in the root directory of your project. The .env file should contain the following:

.. code:: python

    BLIZZARD_API_KEY=YOUR_CLIENT_ID
    BLIZZARD_API_SECRET=YOUR_CLIENT_SECRET

Read more about the .env file :doc:`here </howto/use_env_file>`.

To use the package, import it into your project:

.. code:: python

    from blizzardAPI import BlizzardAPI

To create an instance of the BlizzardAPI class, you need to provide an API key and a secret key:

.. code:: python

    api = BlizzardAPI()

You can then use the instance to make requests to the Blizzard API. For example, to get the toy index for World of Warcraft:

.. code:: python

    from blizzardAPI import BlizzardAPI

    api = BlizzardAPI()
    toy_index = api.wow.game.toy.get_toy_index()

    print(toy_index)

Determining the keys when calling the function
**********************************************

To use the package, import it into your project:

.. code:: python

    from blizzardAPI import BlizzardAPI

To create an instance of the BlizzardAPI class, you need to provide an API key and a secret key:

.. code:: python

    api = BlizzardAPI('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')

You can then use the instance to make requests to the Blizzard API. For example, to get the toy index for World of Warcraft:

.. code:: python

    from blizzardAPI import BlizzardAPI

    api = BlizzardAPI('YOUR_CLIENT_ID', 'YOUR_CLIENT_SECRET')
    toy_index = api.wow.game.toy.get_toy_index()

    print(toy_index)


.. note:: 
    All requests return a dictionary containing the response from the Blizzard API. For more information on the structure of the response, see the `Blizzard API documentation <https://develop.battle.net/documentation/world-of-warcraft/game-data-apis>`_.