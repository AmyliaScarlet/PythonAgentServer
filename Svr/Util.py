import os
import sys
import re
from time import sleep
from time import ctime


def cur_file_dir():
    #获取脚本路径
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def HttpResponseGen(header, fn):
    f = open(fn)
    contxtlist = f.readlines()
    context = ''.join(contxtlist)
    response = "%s\n\n%s\n\n" % (header, context)
    return response


def routeUrl(tag,isRoute = False,ROOT_PATH=''):
    if tag != 'null':
        if isRoute:
            ROOT_PATH = ROOT_PATH.replace('20014', '80')
        else:
            import PythonServer.Svr.Config.ROOT_PATH as C_ROOT_PATH
            ROOT_PATH = C_ROOT_PATH
        r = str(ROOT_PATH+tag)
    else:
        r = 'null'
    return r


def ErrorPage():
    page = 'error.html'
    f = open(page, 'r', encoding='utf-8')
    contxtlist = f.readlines()
    context = ''.join(contxtlist)
    return context

