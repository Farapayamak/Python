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
    SMART_ENDPOINT = 'https://api.payamak-panel.com/post/Smartsms.asmx?wsdl'

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

    def AddUser(self, productId, descriptions, mobileNumber, emailAddress, nationalCode, name, family, corporation, phone, fax, address, postalCode, certificateNumber):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'productId': productId, 'descriptions': descriptions, 'mobileNumber': mobileNumber, 'emailAddress': emailAddress, 'nationalCode': nationalCode, 'name': name, 'family': family, 'corporation': corporation, 'phone': phone, 'fax': fax, 'address': address, 'postalCode': postalCode, 'certificateNumber': certificateNumber})

    def AddUserWithLocation(self, productId, descriptions, mobileNumber, emailAddress, nationalCode, name, family, corporation, phone, fax, address, postalCode, certificateNumber, country, province, city):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'productId': productId, 'descriptions': descriptions, 'mobileNumber': mobileNumber, 'emailAddress': emailAddress, 'nationalCode': nationalCode, 'name': name, 'family': family, 'corporation': corporation, 'phone': phone, 'fax': fax, 'address': address, 'postalCode': postalCode, 'certificateNumber': certificateNumber, 'country': country, 'province': province, 'city': city})

    def AddUserWithMobileNumber(self, productId, mobileNumber, firstName, lastName, email):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'productId': productId, 'mobileNumber': mobileNumber, 'firstName': firstName, 'lastName': lastName, 'email': email})

    def AddUserWithMobileNumber2(self, productId, mobileNumber, firstName, lastName, email, userName):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'productId': productId, 'mobileNumber': mobileNumber, 'firstName': firstName, 'lastName': lastName, 'email': email, 'userName': userName})

    def AddUserWithUserNameAndPass(self, targetUserName, targetUserPassword, productId, descriptions, mobileNumber, emailAddress, nationalCode, name, family, corporation, phone, fax, address, postalCode, certificateNumber):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUserName': targetUserName, 'targetUserPassword': targetUserPassword, 'productId': productId, 'descriptions': descriptions, 'mobileNumber': mobileNumber, 'emailAddress': emailAddress, 'nationalCode': nationalCode, 'name': name, 'family': family, 'corporation': corporation, 'phone': phone, 'fax': fax, 'address': address, 'postalCode': postalCode, 'certificateNumber': certificateNumber})

    def AuthenticateUser(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def ChangeUserCredit(self, amount, description, targetUsername, GetTax):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'amount': amount, 'description': description, 'targetUsername': targetUsername, 'GetTax': GetTax})

    def DeductUserCredit(self, amount, description):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'amount': amount, 'description': description})

    def ForgotPassword(self, mobileNumber, emailAddress, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'mobileNumber': mobileNumber, 'emailAddress': emailAddress, 'targetUsername': targetUsername})

    def GetCities(self, provinceId):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'provinceId': provinceId})

    def GetEnExpireDate(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetExpireDate(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetProvinces(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetUserBasePrice(self, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername})

    def GetUserCredit(self, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername})

    def GetUserCredit2(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetUserDetails(self, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername})

    def GetUserIsExist(self, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername})

    def GetUserNumbers(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetUserTransactions(self, targetUsername, creditType, dateFrom, dateTo, keyword):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername, 'creditType': creditType, 'dateFrom': dateFrom, 'dateTo': dateTo, 'keyword': keyword})

    def GetUserWallet(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def GetUserWalletTransaction(self, dateFrom, dateTo, count, startIndex, payType, payLoc):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'dateFrom': dateFrom, 'dateTo': dateTo, 'count': count, 'startIndex': startIndex, 'payType': payType, 'payLoc': payLoc})

    def GetUsers(self):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {})

    def RemoveUser(self, targetUsername):
        return self.__exec(self.USER_ENDPOINT, inspect.stack()[0][3], {'targetUsername': targetUsername})


    # VOICE webservice

    def SendBulkSpeechText(self, title, body, receivers, DateToSend, repeatCount):
        return self.__exec(self.VOICE_ENDPOINT, inspect.stack()[0][3], {'title': title, 'body': body, 'receivers': receivers, 'DateToSend': DateToSend, 'repeatCount': repeatCount})

    def SendBulkVoiceSMS(self, title, voiceFileId, receivers, DateToSend, repeatCount):
        return self.__exec(self.VOICE_ENDPOINT, inspect.stack()[0][3], {'title': title, 'voiceFileId': voiceFileId, 'receivers': receivers, 'DateToSend': DateToSend, 'repeatCount': repeatCount})

    def UploadVoiceFile(self, title, base64StringFile):
        return self.__exec(self.VOICE_ENDPOINT, inspect.stack()[0][3], {'title': title, 'base64StringFile': base64StringFile})

    
    # CONTACT webservice

    def AddContact(self, groupIds, firstname, lastname, nickname, corporation, mobilenumber, phone, fax, birthdate, email, gender, province, city,  address, postalCode, additionaldate, additionaltext, descriptions):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'groupIds': groupIds, 'firstname': firstname, 'lastname': lastname, 'nickname': nickname, 'corporation': corporation, 'mobilenumber': mobilenumber, 'phone': phone, 'fax': fax, 'birthdate': birthdate, 'email': email, 'gender': gender, 'province': province, 'city': city, 'address': address, 'postalCode': postalCode, 'additionaldate': additionaldate, 'additionaltext': additionaltext, 'descriptions': descriptions})

    def AddContactEvents(self, contactId, eventName, eventType, eventDate):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'contactId': contactId, 'eventName': eventName, 'eventType': eventType, 'eventDate': eventDate})

    def AddGroup(self, groupName, Descriptions, showToChilds):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'groupName': groupName, 'Descriptions': Descriptions, 'showToChilds': showToChilds})

    def ChangeContact(self, contactId, mobilenumber, firstname, lastname, nickname, corporation, phone, fax, email, gender, province, city, address, postalCode, additionaltext, descriptions, contactStatus):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'contactId': contactId, 'mobilenumber': mobilenumber, 'firstname': firstname, 'lastname': lastname, 'nickname': nickname, 'corporation': corporation, 'phone': phone, 'fax': fax, 'email': email, 'gender': gender, 'province': province, 'city': city, 'address': address, 'postalCode': postalCode, 'additionaltext': additionaltext, 'descriptions': descriptions, 'contactStatus': contactStatus})

    def ChangeGroup(self, groupId, groupName, Descriptions, showToChilds, groupStatus):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'groupId': groupId, 'groupName': groupName, 'Descriptions': Descriptions, 'showToChilds': showToChilds, 'groupStatus': groupStatus})

    def CheckMobileExistInContact(self, mobileNumber):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'mobileNumber': mobileNumber})

    def GetContactEvents(self, contactId):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'contactId': contactId})

    def GetContacts(self, groupId, keyword, _from, count):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'groupId': groupId, 'keyword': keyword, 'from': _from, 'count': count})

    def GetContactsByID(self, contactId, status):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'contactId': contactId, 'status': status})

    def GetGroups(self):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {})

    def MergeGroups(self, originGroupId, destinationGroupId, deleteOriginGroup):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'originGroupId': originGroupId, 'destinationGroupId': destinationGroupId, 'deleteOriginGroup': deleteOriginGroup})

    def RemoveContact(self, mobilenumber):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'mobilenumber': mobilenumber})

    def RemoveContactByContactID(self, contactId):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'contactId': contactId})

    def RemoveGroup(self, groupId):
        return self.__exec(self.CONTACT_ENDPOINT, inspect.stack()[0][3], {'groupId': groupId})



    # SCHEDULE webservice

    def AddNewMultipleSchedule(self, to: list, _from, text: list, isflash, scheduleDateTime: list, period):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'scheduleDateTime': scheduleDateTime, 'period': period})

    def AddNewUsance(self, to, _from, text, isflash, scheduleStartDateTime, countrepeat, scheduleEndDateTime, periodType):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'scheduleStartDateTime': scheduleStartDateTime, 'countrepeat': countrepeat, 'scheduleEndDateTime': scheduleEndDateTime, 'periodType': periodType})

    def AddSchedule(self, to, _from, text, isflash, scheduleDateTime, period):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'to': to, 'from': _from, 'text': text, 'isflash': isflash, 'scheduleDateTime': scheduleDateTime, 'period': period})

    def GetScheduleDetails(self, scheduleId):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'scheduleId': scheduleId})

    def GetScheduleStatus(self, scheduleId):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'scheduleId': scheduleId})

    def RemoveSchedule(self, scheduleId):
        return self.__exec(self.SCHEDULE_ENDPOINT, inspect.stack()[0][3], {'scheduleId': scheduleId})


    # BULK webservice

    def AddNumberBulk(self, _from, title, message, receivers, DateToSend):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'from': _from, 'title': title, 'message': message, 'receivers': receivers, 'DateToSend': DateToSend})

    def BulkReception(self, bulkId, maximumRows, startRowIndex):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'bulkId': bulkId, 'maximumRows': maximumRows, 'startRowIndex': startRowIndex})

    def BulkReceptionCount(self, bulkId):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'bulkId': bulkId})

    def GetBulkDeliveries(self, recIds: list):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'recIds': recIds})

    def GetBulkDeliveries2(self, recId):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'recId': recId})

    def GetBulkDetails(self, bulkId):
        return self.__exec(self.BULK_ENDPOINT, inspect.stack()[0][3], {'bulkId': bulkId})
    


    # SMART webservice

    def SendSmartSMS(self, to, text, fromNumber, fromSupportOne, fromSupportTwo):
        return self.__exec(self.SMART_ENDPOINT, inspect.stack()[0][3], {'to': to, 'text': text, 'from': fromNumber, 'fromSupportOne': fromSupportOne, 'fromSupportTwo': fromSupportTwo})
    
    def SendMultipleSmartSMS(self, to, text, fromNumber, fromSupportOne, fromSupportTwo):
        return self.__exec(self.SMART_ENDPOINT, inspect.stack()[0][3], {'to': to, 'text': text, 'from': fromNumber, 'fromSupportOne': fromSupportOne, 'fromSupportTwo': fromSupportTwo})
    
    def GetSmartSMSDeliveries(self, ids):
        return self.__exec(self.SMART_ENDPOINT, inspect.stack()[0][3], {'Ids': ids})