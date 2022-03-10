import inspect
import requests


class Rest_Client:

    __ENDPOINT = 'https://rest.payamak-panel.com/api/SendSMS/'

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def __post(self, method, args):
        self.__appendCred(args)
        return requests.post(self.__ENDPOINT + method, args).json()

    def __appendCred(self, args):
        args['username'] = self.__username
        args['password'] = self.__password



    def SendSMS(self, to, _from, text, isFlash=False):
        args = {'to': to, 'from': _from, 'text': text, 'isFlash': isFlash}
        return self.__post(inspect.stack()[0][3], args)

    def GetDeliveries2(self, recID):
        args = {'recID': recID}
        return self.__post(inspect.stack()[0][3], args)

    def GetMessages(self, location, _from, index, count):
        args = {'location': location, 'from': _from, 'index': index, 'count': count}
        return self.__post(inspect.stack()[0][3], args)

    def GetCredit(self):
        return self.__post(inspect.stack()[0][3], {})

    def GetBasePrice(self):
        return self.__post(inspect.stack()[0][3], {})

    def GetUserNumbers(self):
        return self.__post(inspect.stack()[0][3], {})

    def BaseServiceNumber(self, text, to, bodyId):
        args = {'text': text, 'to': to, 'bodyId': bodyId}
        return self.__post(inspect.stack()[0][3], args)