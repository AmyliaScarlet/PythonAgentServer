from PythonServer.Svr import Svr
import easygui as ui

print('__ini__')

while 1:
    try:
        Svr.Run()
    except Exception as e:
        # 如果服务器异常停止捕捉错误并停止  正常停止则输出Done并重启(404,500等基本的请求错误都会导致正常停止)
        print('Python Server Error!')
        print(e)
        #ui.msgbox('Python Server Error!\n'+str(e))
        break
    finally:
        print('Python Server Done!')
        #ui.msgbox('Python Server Done!')

