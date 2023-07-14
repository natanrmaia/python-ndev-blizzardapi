# Python - NDEV Blizzard API

Integration developed in Python to connect the Blizzard API.


## Author

- [@natanrmaia](https://github.com/natanrmaia)


## Support / Feedback

For support / feedback, send email for contato@natanael.dev.br.


## Reference

 - [Battle.Net Developer Portal](https://develop.battle.net/documentation)


## API Documentation

#### Settings

| Parameter   | Type       | Description                           |
| :---------- | :--------- | :---------------------------------- |
| `client_id` | `string` | **Required**. Check Blizzard's documentation for more information. |
| `client_secret` | `string` | **Required**. Check Blizzard's documentation for more information. |

## Instalation
```python
  pip install python-ndev-blizzardapi
```

## Usage Example
```python
  from blizzardAPI import BlizzardAPI
  
  api = BlizzardAPI(client_id, client_secret)
  api.bnet.oauth.get_user_info("us","imagine_token_here")
```

## Blizzard APIs Supported

| API                     | Items           | Obs                   |
| :---------------------- | :-------------- | :-------------------- |
| **Battle.Net**          | OAuth API       | All Regions supported |
| **World Of Warcraft**   | Game Data API   | _Profile Data API in development_ |


## Tests using PyTest
To perform the tests using PyTest, I recommend using the dotenv module. Read more in the documentation provided below.
```cmd
pytest blizzardAPI
```

## Documentation

[Read the Docs](https://python-ndev-blizzardapi.readthedocs.io/)