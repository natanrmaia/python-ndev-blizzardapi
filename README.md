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

### Battle.Net API

| Python      | API URL    | API Name                                    |
| :---------- | :--------- | :------------------------------------------ |
| `api.bnet.oauth.get_user_info(region, access_token)`      | `/oauth/userinfo` | User Info (param) |
| `api.bnet.oauth.get_token_validation(region, access_token)`      | `/oauth/check_token` | Token Validation (GET) |


## Documentation

[Read the Docs](https://python-blizzardapi.natanael.dev.br/)