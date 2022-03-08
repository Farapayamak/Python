from lib.rest import Rest_Client


restClient = Rest_Client('username', 'password')
restClient.SendSMS('09123456789', '5000xxx', 'test sms')
