from jwt import encode, decode
from datetime import datetime, timedelta

class Authenticator:
    def __init__(self,jwtAlgorithm:str, jwtSecret:str):
        self.jwtAlgorithm = jwtAlgorithm
        self.jwtSecret = jwtSecret
    def createToken(self, payload):
        if len(payload) > 2: return False
        if 'expires_in' in list(payload.keys()):
            expr:timedelta = payload.pop('expires_in', None)
            payload.update({'exp':datetime.utcnow()+expr})
        self.jwtToken = encode(payload, self.jwtSecret, self.jwtAlgorithm)
        return self.jwtToken
    def isTokenValid(self, token):
        try: 
            self.payload = decode(token, self.jwtSecret, self.jwtAlgorithm)
            return True
        except: return False