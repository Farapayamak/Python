from lib.soap import Soap_Client


soapClient = Soap_Client('username', 'password')
# result = soapClient.SendSimpleSMS2('09123456789', '5000xxx', 'test sms')
# result = soapClient.SendSimpleSMS(['09123456789', '09123456789'], '5000xxx', 'test sms')
result = soapClient.SendMultipleSMS(['09123456789', '09123456789'], '5000xxx', ['test sms 1', 'test sms 2'], '')

print(result)