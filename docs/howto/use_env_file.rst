Use .env file to set module variables
#####################################

`.env` files are commonly used to store environment variables for your project, usually containing sensitive information such as API keys, database passwords, and so on. For Python, the `python-dotenv` library can be used to load this information from a `.env` file into the Python runtime environment.

Here are the steps to use a `.env` file with the `python-dotenv` module in a Python project:

#. **Install the python-dotenv library**

   You can install the `python-dotenv` library using pip, which is Python's package manager. In your terminal, navigate to your project folder and run the following command:

    .. code-block:: bash

        pip install python-dotenv

#. **Create the .env file**

   At the root of your project, create a new file called `.env`. This is the file where you'll store your environment variables. 
   
   Each line defines a new environment variable. The variable name is followed by an equals sign and the variable value.
   
   Here's an example of how you can set variables in the file:

    .. code-block:: bash

        BLIZZARD_API_CLIENT_ID=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
        BLIZZARD_API_CLIENT_SECRET=1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p

#. **Use the environment variables in your Python code**

   Now, in your Python code, you can load the environment variables from the `.env` file using the `python-dotenv` library. Here's an example of how you can do this:

   .. code:: python

    from dotenv import load_dotenv
    import os

    # Load the variables from the .env file
    load_dotenv()

    # Now you can access the variables directly from os.getenv
    client_id = os.getenv("BLIZZARD_API_CLIENT_ID")
    client_secret = os.getenv("BLIZZARD_API_CLIENT_SECRET")
    client_region = os.getenv("BLIZZARD_API_REGION")

    print(client_id, client_secret)

In this example, `os.getenv("client_id")` will return the string `"a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6"` (as set in the `.env` file), and so on for the other variables.

Finally, don't forget to add `.env` to your `.gitignore` file to prevent accidentally committing sensitive information to a public git repository.

**Note:** If you're using a virtual environment, you'll need to install the `python-dotenv` library inside the virtual environment. Otherwise, you'll get an error when you try to import the library.

By default, the `python-ndev-blizzardapi` library will look for the following environment variables:

* `BLIZZARD_API_CLIENT_ID` - Your Blizzard API client ID
* `BLIZZARD_API_CLIENT_SECRET` - Your Blizzard API client secret
* `BLIZZARD_API_REGION` - The region to use for API requests (defaults to `us`)
* `BLIZZARD_API_ACCESS_TOKEN` = The access token to use for API requests (optional)
* `BLIZZARD_API_LOCALE` - The locale to use for API requests (defaults is blank)
* `BLIZZARD_API_REALM_ID` - The realm ID to use for API requests (defaults is blank)
* `BLIZZARD_API_REALM_SLUG` - The realm slug to use for API requests (defaults is blank)
* `BLIZZARD_API_CHARACTER_ID` - The character ID to use for API requests (defaults is blank)
* `BLIZZARD_API_CHARACTER_NAME` - The character name to use for API requests (defaults is blank)
* `BLIZZARD_API_SEASON_ID` - The season ID to use for API requests (defaults is blank)

This means that you can set these variables in your `.env` file and the library will automatically load them for you.
You can also override these variables by passing them directly to the `BlizzardApi` constructor.

.. note:: 
    There is an example `.env` file available in the github repository called `.env_example`. Use it as a reference.
    Just remember to rename it to `.env` and fill in your own values.
