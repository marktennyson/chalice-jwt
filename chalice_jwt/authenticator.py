from jwt import encode, decode

class Authenticator:
    def __init__(self,jwtAlgorithm, jwtSecret):
        self.jwtAlgorithm = jwtAlgorithm
        self.jwtSecret = jwtSecret
    def createToken(self, payload):
        if len(payload) > 2: return False
        self.jwtToken = encode(payload, self.jwtSecret, self.jwtAlgorithm)
        return self.jwtToken
    def isTokenValid(self, token):
        try: 
            self.payload = decode(token, self.jwtSecret, self.jwtAlgorithm)
            return True
        except: return False