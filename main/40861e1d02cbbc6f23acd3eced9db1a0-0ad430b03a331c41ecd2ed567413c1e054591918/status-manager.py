#!/usr/bin/python3
import socket
import struct
import json
import time
import win32api
import os




def kill_exe(exe_name):
    """
    杀死exe进程
    :param exe_name:进程名字
    :return:无
    """
    os.system('taskkill /f /t /im '+exe_name)#MESMTPC.exe程序名字
    print("杀死进程{}".format(exe_name))

class StatusPing:
    """ Get the ping status for the Minecraft server """

    def __init__(self, host='locatehost', port=10021, timeout=60):
        """ Init the hostname and the port """
        self._host = host
        self._port = port
        self._timeout = timeout

    def _unpack_varint(self, sock):
        """ Unpack the varint """
        data = 0
        for i in range(5):
            ordinal = sock.recv(1)

            if len(ordinal) == 0:
                break

            byte = ord(ordinal)
            data |= (byte & 0x7F) << 7 * i

            if not byte & 0x80:
                break

        return data

    def _pack_varint(self, data):
        """ Pack the var int """
        ordinal = b''

        while True:
            byte = data & 0x7F
            data >>= 7
            ordinal += struct.pack('B', byte | (0x80 if data > 0 else 0))

            if data == 0:
                break

        return ordinal

    def _pack_data(self, data):
        """ Page the data """
        if type(data) is str:
            data = data.encode('utf8')
            return self._pack_varint(len(data)) + data
        elif type(data) is int:
            return struct.pack('H', data)
        elif type(data) is float:
            return struct.pack('Q', int(data))
        else:
            return data

    def _send_data(self, connection, *args):
        """ Send the data on the connection """
        data = b''

        for arg in args:
            data += self._pack_data(arg)

        connection.send(self._pack_varint(len(data)) + data)

    def _read_fully(self, connection, extra_varint=False):
        """ Read the connection and return the bytes """
        packet_length = self._unpack_varint(connection)
        packet_id = self._unpack_varint(connection)
        byte = b''

        if extra_varint:
            # Packet contained netty header offset for this
            if packet_id > packet_length:
                self._unpack_varint(connection)

            extra_length = self._unpack_varint(connection)

            while len(byte) < extra_length:
                byte += connection.recv(extra_length)

        else:
            byte = connection.recv(packet_length)

        return byte

    def get_status(self):
        """ Get the status response """
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connection:
            connection.settimeout(self._timeout)
            connection.connect((self._host, self._port))

            # Send handshake + status request
            self._send_data(connection, b'\x00\x00', self._host, self._port, b'\x01')
            self._send_data(connection, b'\x00')

            # Read response, offset for string length
            data = self._read_fully(connection, extra_varint=True)

            # Send and read unix time
            self._send_data(connection, b'\x01', time.time() * 1000)
            unix = self._read_fully(connection)

        # Load json and return
        response = json.loads(data.decode('utf8'))
        response['ping'] = int(time.time() * 1000) - struct.unpack('Q', unix)[0]

        return response

while 1:
    time_ping_start =time.perf_counter()
    try:
        f = open('data.txt','a',encoding='utf-8')
        status_ping = StatusPing('play.zamcraft.net')
        ping_result = str(status_ping.get_status())
        #print(status_ping.get_status())
        f.write('\n')
        f.write(time.strftime("%Y-%m-%d--%H:%M:%S", time.localtime()) +"--"+ str(int(time.time())) + ping_result)
        if "Last_ID" in ping_result:
            print('yep!')
        else:
            kill_exe('MinecraftClient.exe')
            time.sleep(1.5)
            win32api.ShellExecute(0, 'open', r'C:\Minecraft-PATH\MinecraftClient\MinecraftClient.exe', "C:\Minecraft-PATH\MinecraftClient\MinecraftClient.ini",'',1)
    except IOError as e:
        print("ping exception: %s: %s" %(e.errno, e.strerror))
    else:
        print("Success!")
    finally:
        print("Close the file.")
        f.close()
        time_ping_end = time.perf_counter()
        print('Running time: %s (sec)'%(time_ping_end-time_ping_start))
        print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) +' [Done!]')
    time.sleep(120)

