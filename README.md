# ISIC OAuth Example

An application demonstrating authentication with the ISIC Archive from a server side Flask application.

## Usage
* Create a client application https://api.isic-archive.com/oauth/applications/register/ with the following options

``` text
    Client type: Confidential
    Authorization grant type: Authorization Code
    Redirect uris: http://127.0.0.1:5000/authorize
```

* Define the necessary environment variables
  ```bash
    export OAUTH_CLIENT_ID="<client-id>"
    export OAUTH_CLIENT_SECRET="<client-secret>"
    export OAUTH_BASE_URL="https://api.isic-archive.com/oauth"
    export OAUTH_REDIRECT_URL="http://127.0.0.1:5000"
    export API_BASE_URL="https://api.isic-archive.com/api/v2"
    export SECRET_KEY="<secret-key>" # change to a long random value in production
  ```

* Run the test application

```bash
    FLASK_ENV=development flask run
```

* Navigate to http://127.0.0.1:5000 and login.
