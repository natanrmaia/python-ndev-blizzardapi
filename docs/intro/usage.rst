Usage examples
###############

.. toctree::
   :caption: Table of Contents
   :maxdepth: 3

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

All requests return a dictionary containing the response from the Blizzard API. For more information on the structure of the response, see the `Blizzard API documentation <https://develop.battle.net/documentation/world-of-warcraft/game-data-apis>`_.