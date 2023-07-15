Best practices for using client_id and client_secret
####################################################

.. toctree::
   :caption: Table of Contents
   :maxdepth: 3
   
This module requires you to have a client_id and client_secret to access the Blizzard API. This requires a set of best practices to keep these pieces of information secure. Here are some tips:

* **Don't include these values directly in the code**: Always avoid including the `client_id` and `client_secret` directly in the source code. This can lead to the leakage of sensitive information if the source code is shared or becomes public.

* **Use environment variables**: A good practice is to store the `client_id` and `client_secret` as environment variables on the server or local machine where your application is running. This way, these pieces of information will not be present in the source code and will only be accessible when the environment is running. 

* **Use separate configuration files**: Another practice is to place the `client_id` and `client_secret` in a separate configuration file that is loaded at runtime. This configuration file should be excluded from the version control system (e.g., included in the .gitignore if you are using Git). Check the article :doc:`how to use .env file </howto/use_env_file>` for more information on how to set environment variables for this module.

* **Encryption**: When storing these values, whether in environment variables or a configuration file, consider using some form of encryption. Thus, even if someone gains access to these values, they won't be immediately useful without the decryption key.

* **Limited access permissions**: If you're using a configuration file, ensure that only authorized users can read that file. In Unix systems, this can be done using `chmod` commands to change the file permissions.

* **Periodic regeneration**: Depending on the sensitivity of your application, you may consider periodically regenerating the `client_id` and `client_secret`. This can help mitigate any issues if your keys have been compromised.

* **Monitoring**: Monitor the use of your `client_id` and `client_secret`. If you notice suspicious activities, such as an unusual number of requests from an unknown location, it may be a sign that your keys have been compromised.

* **Use secure networks**: When using these keys for authentication, make sure you are on a secure network. Avoid using these keys on public networks without adequate security.

Remember, the security of your client keys is crucial for the security of your application. Follow these best practices to ensure you are adequately protecting this sensitive information.