from .authenticator import Authenticator
from datetime import datetime, timedelta
from .utils import _jsonify
from functools import wraps
from jwt import decode

class JWTManager:
    def __init__(self, jwtAlgorithm='HS256', jwtSecret=str(),app=None):
        self.jwtAlgorithm = jwtAlgorithm
        self.jwtSecret = jwtSecret
        self.authenticator = Authenticator(self.jwtAlgorithm, self.jwtSecret)
        if app is not None: self.init_app(app)
    
    def init_app(self, app): self.app = app
    
    def create_access_token(self, identity, expires_in=None):
        self.identity = list(identity.keys())[0]
        self.payload = identity.copy()
        if expires_in is not None: self.payload.update({'exp':datetime.utcnow()+expires_in})
        self.access_token = self.authenticator.createToken(self.payload)
        try: return self.access_token.decode('utf-8')
        except: return self.access_token
    
    def jwt_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            argData = self.app.current_request.headers.get('authorization')
            if not argData or not " " in argData: return _jsonify(message='missing authentication token')
            jwtToken = argData.split(" ")[1]
            if not self.authenticator.isTokenValid(jwtToken):return _jsonify(message='invalid/expired authentication token')
            return f(*args, **kwargs)
        return decorated_function

    def get_jwt_identity(self):
        argData = self.app.current_request.headers.get('authorization')
        if not argData or not " " in argData: return _jsonify(message='missing authentication token')
        jwtToken = argData.split(" ")[1]
        return decode(jwtToken, self.jwtSecret, algorithms=[self.jwtAlgorithm]).get(self.identity)