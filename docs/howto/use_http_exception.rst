Use mapped exceptions to handle common API errors
#####################################

The `mapped exceptions` feature allows you to handle common API errors in a more convenient way. You can define a mapping between the error codes returned by the API and the exceptions that should be thrown when these errors occur. This way, you can avoid writing boilerplate code to check the error codes and throw the appropriate exceptions.

How to get mapped exceptions:

.. code-block:: python

    from blizzardAPI.exceptions import HTTP400Error, HTTP401Error, HTTP403Error, HTTP404Error, HTTP429Error, HTTP500Error, HTTP503Error, HTTP504Error, HTTPUnknownError

    try:
        # Make a request that returns a 404 error
        api = BlizzardAPI()
        toy_index = api.wow.game.toy.get_toy(999999)
    except HTTP404Error as e:
        print(f"Error: {e}")

The `HTTP400Error`, `HTTP401Error`, `HTTP403Error`, `HTTP404Error`, `HTTP429Error`, `HTTP500Error`, `HTTP503Error`, `HTTP504Error`, and `HTTPUnknownError` exceptions are available for you to use. You can catch these exceptions in your code and handle them as needed.

Why even use mapped exceptions?
*******************************
The main advantage of using mapped exceptions is that they allow you to handle common API errors in a more convenient way. Instead of writing boilerplate code to check the error codes and throw the appropriate exceptions, you can simply catch the mapped exceptions and handle them as needed.

What are the reasons for each error?
*************************************
- `HTTP400Error`: The request was invalid or malformed.
- `HTTP401Error`: The request was unauthorized. This usually occurs when the Client ID, Client Secret, or access token is invalid.
- `HTTP403Error`: The request was forbidden. This usually occurs when the user does not have permission to access the requested resource. This can also happen if you try to access protected data without following the 'Authorization Code Flow' or the required scope has not been obtained.
- `HTTP404Error`: The requested resource was not found.
- `HTTP429Error`: The request was rate-limited. This usually occurs when you make too many requests in a short period of time.
- `HTTP500Error`: The server encountered an internal error while processing the request.
- `HTTP503Error`: The server is currently unavailable. This usually occurs when the server is down for maintenance or experiencing high traffic.
- `HTTP504Error`: The server took too long to respond to the request.
- `HTTPUnknownError`: An unknown error occurred. This usually occurs when the server returns an error code that is not handled by the other mapped exceptions.

.. note::
    The `HTTPUnknownError` exception is a catch-all exception that is raised when the server returns an error code that is not handled by the other mapped exceptions. You can use this exception to catch any unexpected errors that may occur.
    If you find that you are frequently encountering `HTTPUnknownError` exceptions, feel free to open an issue on the GitHub repository so that we can investigate and add support for the new error codes.