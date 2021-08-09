<h1>Json Web Token based authentication for Python Chalice</h1>
# Maintainers wanted
<!-- [Apply within](https://github.com/github-tools/github/issues/539) -->

# Chalice-JWT

# Downloads
[![Downloads](https://pepy.tech/badge/chalice-jwt)](https://pepy.tech/project/chalice-jwt) [![Downloads](https://pepy.tech/badge/chalice-jwt/month)](https://pepy.tech/project/chalice-jwt/month) [![Downloads](https://pepy.tech/badge/chalice-jwt/week)](https://pepy.tech/project/chalice-jwt/week)
<br>

`chalice-jwt` provides a simple interface for jwt based authentication with AWS Chalice microframework(serverless).
source code available at: <a href="https://github.com/marktennyson/chalice-jwt">https://github.com/marktennyson/chalice-jwt</a>

## Usage

```python
from chalice import Chalice
from chalice_jwt import JWTManager
from datetime import timedelta

app = Chalice(app_name='test-jwt')

jwt = JWTManager(jwtSecret="top-secret-key", app=app)


@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/get-token')
def token():
    Identity:dict = {"email":"aniketsarkar@yahoo.com"}
    return {'token': jwt.create_access_token(identity=Identity, expires_in=timedelta(seconds=60)),}

@app.route('/get-identity')
@jwt.its_required
def login():
    return jwt.get_jwt_identity()
```

## Installation
`chalice-jwt` is available from `pypi`.
#### install using pip
```shell
pip install chalice-jwt
```
#### install from source code
```shell
git clone https://github.com/marktennyson/chalice-jwt && cd chalice-jwt
python setup.py install --user
```

## Compatibility
`chalice-jwt` is compatiable with all python3 versions.
Not available for Python version 2.


## Contributing

We welcome contributions of all types!
