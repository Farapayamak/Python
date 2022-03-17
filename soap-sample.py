from lib.soap import Soap_Client
# Use bellow lines to consume with a `pip install farapayamak`
# from farapayamak import soap
# Soap_Client = soap.Soap_Client

soapClient = Soap_Client('username', 'password')
# result = soapClient.SendSimpleSMS2('09123456789', '5000xxx', 'test sms')
result = soapClient.SendMultipleSMS(['09123456789', '09123456789'], '5000xxx', ['test sms 1', 'test sms 2'], '')

print(result)