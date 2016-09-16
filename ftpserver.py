#coding=utf-8

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
import socket
import optparse

parser = optparse.OptionParser()

parser.add_option("-u","--user",dest="username",help="login username")
parser.add_option("-p","--password",dest="password",help="login password")
parser.add_option("-d","--dir",dest="homedir",help="ftp homedir")
parser.add_option("-l","--port",dest="port",help="ftp listen port")

(options,args) = parser.parse_args()

default_username = "admin"
default_password = "123456"
default_homedir = "."
default_port = 21 

#print options

if options.username:
	default_username=options.username

if options.password:
	default_password=options.password

if options.homedir:
	default_homedir = options.homedir

if options.port:
	default_port=options.port


print "---------------------------------------------------------"
print "[+] Please login with (%s:%s) && ftp_port is (%s)"%(default_username,default_password,default_port)
print "---------------------------------------------------------"

authorizer = DummyAuthorizer()
authorizer.add_user(default_username, default_password, default_homedir,'elradfmwM')
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0",default_port), handler)
server.serve_forever()



