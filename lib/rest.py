import inspect
import requests


class Rest_Client:

    __ENDPOINT = 'https://rest.payamak-panel.com/api/'

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def __post(self, method, args, path="SendSMS/"):
        self.__appendCred(args)
        return requests.post(self.__ENDPOINT + path + method, json=args).json()

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
    

    def SendSmartSMS(self, to, text, fromNumber, fromSupportOne, fromSupportTwo):
        args = {'to': to, 'text': text, 'from': fromNumber, 'fromSupportOne': fromSupportOne, 'fromSupportTwo': fromSupportTwo}
        return self.__post("Send", args, "SmartSMS/")
    
    def SendMultipleSmartSMS(self, to, text, fromNumber, fromSupportOne, fromSupportTwo):
        args = {'to': to, 'text': text, 'from': fromNumber, 'fromSupportOne': fromSupportOne, 'fromSupportTwo': fromSupportTwo}
        return self.__post("SendMultiple", args, "SmartSMS/")
    
    def GetSmartDeliveries2(self, id):
        args = {'Id': id}
        return self.__post("GetDeliveries2", args, "SmartSMS/")
    
    def GetSmartDeliveries(self, ids):
        args = {'Ids': ids}
        return self.__post("GetDeliveries", args, "SmartSMS/")
    