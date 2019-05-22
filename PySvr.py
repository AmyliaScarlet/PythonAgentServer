import easygui as ui

command = ui.buttonbox(msg='是否启动Python服务器？', title='Python服务器', choices=('启动', '退出'))
print(command)
if command == '启动':
    import PythonServer.Svr
elif command == '退出':
    pass
