"""
DateTime: Since 2017/03/23 Start
Auth: Amy
Python Server Version: 1.0.1
Des: This is a Server written in Python
"""

import errno
import signal
import socket
import easygui as ui

import requests


from PythonServer.Svr.Config import *

name = 'PythonServer'

# httpheader = "b'["+ctime()+"] GET / HTTP/1.1\r\nHost: 127.0.0.1:20014\r\nConnection: keep-alive\r\nCache-Control: max-age=0\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nUpgrade-Insecure-Requests: 1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36\r\nAccept-Encoding: gzip, deflate, sdch\r\nAccept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.6'"

def sigIntHander(signo, frame):
    print('get signo# ', signo)
    global runflag
    runflag = False
    global lisfd
    lisfd.shutdown(socket.SHUT_RD)

lisfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
lisfd.bind((HOST, int(PORT)))
lisfd.listen(2)
signal.signal(signal.SIGINT, sigIntHander)
runflag = True


def Run():
    print('Python Server Start!')
    #ui.msgbox('启动成功！')
    while runflag:
        try:
            confd, addr = lisfd.accept()
        except socket.error as e:
            if e.errno == errno.EINTR:
                print('get a except EINTR')
            else:
                print(e.errno)
            continue

        if runflag == False:
            break

        print("connect by ", addr)

        # data = confd.recv(1024)
        try:
            data, addr = confd.recvfrom(4096)
        except socket.error as e:
            print(e.errno)
        if not data:
            break
        headerData = data.decode()
        headerList = headerData.split('\r\n') #.replace(':'+PORT, '')
        print(headerList)
        headerDict = {'Python Server Version': '1.0.0'}
        for header in headerList:
            # Colon and Space
            header = header.split(': ')
            if len(header) == 2:
                headerDict.setdefault(header[0], header[1])
        #print(1)
        #print(headerDict)
        referer = headerDict.get('Referer', 'null')

        # get page
        if referer == 'null':
            #print(2)
            tag = headerList[0].replace('GET /', '').replace(' HTTP/1.1', '')
        else:
            #print(3)
            tag = referer.replace(ROOT_PATH, '')


        #baseUrl = pageDir.get(tag, 'null')
        # use route to gen url
        baseUrl = routeUrl(tag, True, ROOT_PATH)

        if baseUrl == 'null':
            context = ErrorPage()
        else:
            s = requests.Session()
            context = s.get(baseUrl)

            if '404.0 - Not Found</title>' in context.text:
                context = ErrorPage()
            else:
                context = context.text.replace('string(0) \"\"', '').replace(' <!DOCTYPE html', '<!DOCTYPE html').replace('<title>', '<meta name="generator" content="该页面由Python服务器反向代理 IIS服务器进行处理">\n<title>')
            #print(context)
        # send page
        if 'charset=GBK' in context:
            confd.send(context.encode('GBK'))
        if 'charset=utf-8' in context:
            confd.send(context.encode('utf-8'))

        confd.close()
    else:
        print('runflag#', runflag)





