from zeep import Client
import inspect



class Soap_Client:

    SEND_ENDPOINT = 'http://api.payamak-panel.com/post/send.asmx?wsdl'
    RECEIVE_ENDPOINT = 'http://api.payamak-panel.com/post/receive.asmx?wsdl'
    USER_ENDPOINT = 'http://api.payamak-panel.com/post/users.asmx?wsdl'
    VOICE_ENDPOINT = 'http://api.payamak-panel.com/post/voice.asmx?wsdl'
    CONTACT_ENDPOINT = 'http://api.payamak-panel.com/post/contacts.asmx?wsdl'
    SCHEDULE_ENDPOINT = 'http://api.payamak-panel.com/post/schedule.asmx?wsdl'
    BULK_ENDPOINT = 'http://api.payamak-panel.com/post/newbulks.asmx?wsdl'

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def __appendCred(self, args):
        args['username'] = self.__username
        args['password'] = self.__password

    def __exec(self, endpoint, method, args):
        client = Client(endpoint)
        self.__appendCred(args)
        # organize lists by type (int, long, string)
        # zeep doesn't know how to send array of types (only first item works)
        for key in args:
            if isinstance(args[key], list):
                if isinstance(args[key][0], str):
                    array_of_string_type = client.get_element("ns0:ArrayOfString")
                    args[key] = array_of_string_type(args[key])
        return getattr(client.service, method)(**args)


    # SEND webservice
    def GetCredit(self):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {})

    def GetDeliveries(self, recIds: list):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'recIds': recIds})

    def GetDeliveries3(self, recId: list):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'recId': recId})

    def GetSmsPrice(self, irancellCount, mtnCount, _from, text):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'irancellCount': irancellCount, 'mtnCount': mtnCount, 'from': _from, 'text': text})

    def SendByBaseNumber(self, text: list, to, bodyId):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'text': text, 'to': to, 'bodyId': bodyId})

    def SendByBaseNumber2(self, text, to, bodyId):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'text': text, 'to': to, 'bodyId': bodyId})

    def SendByBaseNumber3(self, text, to):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'text': text, 'to': to})

    def SendSimpleSMS(self, to: list, _from, text, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash})
        
    def SendSimpleSMS2(self, to, _from, text, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash})
    
    def SendSms(self, to: list, _from, text, udh, recId: list, status, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'udh': udh, 'recId': recId, 'status': status})

    def SendSms2(self, to: list, _from, text, udh, recId: list, status, filterId, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'udh': udh, 'recId': recId, 'status': status, 'filterId': filterId})

    def SendMultipleSMS(self, to: list, _from, text: list, udh, recId: list, status, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'udh': udh, 'recId': recId, 'status': status})

    def SendMultipleSMS(self, to: list, _from: list, text: list, udh, recId: list, status, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'udh': udh, 'recId': recId, 'status': status})
    

    #RECEIVE webservice

    def ChangeMessageIsRead(self, msgIds):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'msgIds': msgIds})

    def GetInboxCount(self, isRead: bool):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'isRead': isRead})

    def GetLatestReceiveMsg(self, sender, receiver):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'sender': sender, 'receiver': receiver})

    def GetMessages(self, location, _from, index, count):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'location': location, 'from': _from, 'index': index, 'count': count})

    def GetMessagesAfterID(self, location, _from, count, msgId):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'location': location, 'from': _from, 'count': count, 'msgId': msgId})

    def GetMessagesFilterByDate(self, location, _from, index, count, dateFrom, dateTo, isRead: bool):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'location': location, 'from': _from, 'index': index, 'count': count, 'dateFrom': dateFrom, 'dateTo': dateTo, 'isRead': isRead})

    def GetMessagesReceptions(self, msgId, fromRows):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'msgId': msgId, 'fromRows': fromRows})

    def GetMessagesWithChangeIsRead(self, location, _from, index, count, isRead, changeIsRead):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'location': location, 'from': _from, 'index': index, 'count': count, 'isRead': isRead, 'changeIsRead': changeIsRead})

    def GetOutBoxCount(self):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {})

    def RemoveMessages(self, location, msgIds):
        return self.__exec(self.RECEIVE_ENDPOINT, inspect.stack()[0][3], {'location': location, 'msgIds': msgIds})


    # USER webservice

    