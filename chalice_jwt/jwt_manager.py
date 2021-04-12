from .authenticator import Authenticator
from .utils import _jsonify
from functools import wraps
from jwt import decode

class JWTManager:
    def __init__(self, jwtAlgorithm:str='HS256', jwtSecret:str=str(),app=None):
        self.jwtAlgorithm:str = jwtAlgorithm
        self.jwtSecret:str = jwtSecret
        self.authenticator:Authenticator = Authenticator(self.jwtAlgorithm, self.jwtSecret)
        if app is not None: self.init_app(app)
    
    def init_app(self, app): self.app = app
    
    def create_access_token(self, **kwargs):
        # self.identity = kwargs.
        self.access_token = self.authenticator.createToken(kwargs)
        try: return self.access_token.decode('utf-8')
        except: return self.access_token
    
    def jwt_required(self, f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            argData = self.app.current_request.headers.get('authorization')
            if not argData or not " " in argData: return _jsonify(message='missing authentication token')
            jwtToken = argData.split(" ")[1]
            if not self.authenticator.isTokenValid(jwtToken):return _jsonify(message='invalid authentication token')
            return f(*args, **kwargs)
        return decorated_function

    def get_jwt_identity(self):
        argData = self.app.current_request.headers.get('authorization')
        if not argData or not " " in argData: return _jsonify(message='missing authentication token')
        jwtToken = argData.split(" ")[1]
        try: 
            payload:dict = decode(jwtToken, self.jwtSecret, algorithms=[self.jwtAlgorithm])
            return payload
        except: return False