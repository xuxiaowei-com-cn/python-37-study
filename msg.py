import ctypes

ctypes.windll.user32.MessageBoxA(0, "你好世界".encode('gbk'), "弹窗".encode('gbk'), 0x00)

# 0x10 到 0x16 为错误图标弹窗
# ctypes.windll.user32.MessageBoxA(0, "消息内容".encode('gbk'), "错误消息".encode('gbk'), 0x10)

# 0x20 到 0x26 为询问图标弹窗
# ctypes.windll.user32.MessageBoxA(0, "消息内容".encode('gbk'), "询问消息".encode('gbk'), 0x20)

# 0x30 到 0x36 为警告图标弹窗
# ctypes.windll.user32.MessageBoxA(0, "消息内容".encode('gbk'), "警告消息".encode('gbk'), 0x30)

# 0x40 到 0x46 为注意图标弹窗
# ctypes.windll.user32.MessageBoxA(0, "消息内容".encode('gbk'), "注意消息".encode('gbk'), 0x40)
