from chalice import Chalice
from chalice_jwt import JWTManager
from datetime import timedelta

app = Chalice(app_name='test-jwt')

jwt = JWTManager(jwtSecret="secret", app=app)


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