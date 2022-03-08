import inspect
import requests


class Rest_Client:

    __ENDPOINT = 'https://rest.payamak-panel.com/api/SendSMS/'

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def __post(self, method, args):
        self.__appendCred(args)
        requests.post(self.__ENDPOINT + method, args)

    def __appendCred(self, args):
        args['username'] = self.__username
        args['password'] = self.__password        

    def SendSMS(self, to, _from, text, isFlash=False):
        args = {'to': to, 'from': _from, 'text': text, 'isFlash': isFlash}
        return self.__post(inspect.stack()[0][3], args)

        
