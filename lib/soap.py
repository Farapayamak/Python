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
                # elif isinstance(args[key][0], int):
                #     array_of_long_type = client.get_element("ns0:ArrayOfLong")
                #     args[key] = array_of_long_type(args[key])
        return getattr(client.service, method)(**args)


    # SEND webservice
    def GetCredit(self):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {})

    def SendSimpleSMS2(self, to, _from, text, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash})
    
    def SendSimpleSMS(self, to: list, _from, text, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash})

    def SendMultipleSMS(self, to: list, _from, text, udh, isflash = False):
        return self.__exec(self.SEND_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'udh': udh})