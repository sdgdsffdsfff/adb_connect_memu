__author__ = 'nekocode'
import os

__memu_adb_path__ = '\"E:/Program Files (x86)/Microvirt/MEmu/adb.exe\"'
__sdk_adb_path__ = 'adb'

if __name__ == '__main__':
    rlt = os.popen(__memu_adb_path__ + " devices")
    line = rlt.readlines()[1].strip('\r\n')
    start_index = line.find("device")
    if start_index != -1:
        port = line[10:start_index].strip('\t ')
        os.system(__sdk_adb_path__ + ' connect 127.0.0.1:' + port)
