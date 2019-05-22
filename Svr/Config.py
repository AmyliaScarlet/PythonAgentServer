# there can read from server.config
print('__Config__')
import xml.dom.minidom as xmlDom
from xml.dom.minidom import Document
from PythonServer.Svr.Util import *


HOST = "127.0.0.1"
PORT = 20014
SSL = 'false'
schema = ''


ConfigPath = cur_file_dir()+'\server.config'
if os.path.exists(ConfigPath):
    dom = xmlDom.parse(ConfigPath)
    root = dom.documentElement
    HOST_E = root.getElementsByTagName('HOST')
    HOST = HOST_E[0].firstChild.data
    PORT_E = root.getElementsByTagName('PORT')
    PORT = PORT_E[0].firstChild.data
    SSL_E = root.getElementsByTagName('SSL')
    SSL = SSL_E[0].firstChild.data
else:
    doc = Document()  # 创建DOM文档对象
    config = doc.createElement('Config')

    HOST_E = doc.createElement('HOST')
    HOST_E_T = doc.createTextNode(HOST) #元素内容写入
    HOST_E.appendChild(HOST_E_T)
    config.appendChild(HOST_E)

    PORT_E = doc.createElement('PORT')
    PORT_E_T = doc.createTextNode(str(PORT)) #元素内容写入
    PORT_E.appendChild(PORT_E_T)
    config.appendChild(PORT_E)

    SSL_E = doc.createElement('SSL')
    SSL_E_T = doc.createTextNode('False') #元素内容写入
    SSL_E.appendChild(SSL_E_T)
    config.appendChild(SSL_E)


    doc.appendChild(config)
    f = open(ConfigPath, 'w')
    f.write(doc.toprettyxml(indent=''))
    f.close()

if SSL.lower() == 'true':
    schema = 'https'
elif SSL.lower() == 'false':
    schema = 'http'

ROOT_PATH = str(schema)+'://' + str(HOST) + ':' + str(PORT) + '/'




#pageDir = {
#    'index': 'http://yixiangdai.com/index.php?ctl=ItemHome',
#    'login': 'http://yixiangdai.com/index.php?ctl=AndroidUser&act=login',
#    'uc': 'http://yixiangdai.com/index.php?ctl=AndroidDeals',
#    'help': 'http://yixiangdai.com/index.php?ctl=guarantee',
#}



