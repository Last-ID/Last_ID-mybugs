import os
import time
import win32api


def kill_exe(exe_name):
    """
    杀死exe进程
    :param exe_name:进程名字
    :return:无
    """
    os.system('taskkill /f /t /im '+exe_name)#MESMTPC.exe程序名字
    print("杀死进程{}".format(exe_name))


kill_exe('MinecraftClient.exe')
time.sleep(3)
win32api.ShellExecute(0, 'open', r'C:\Minecraft-PATH\MinecraftClient\MinecraftClient.exe', 'C:\Minecraft-PATH\MinecraftClient','',1)