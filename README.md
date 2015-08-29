#README

- 将 `adb_connect_memu.py` 以及 `adb_connect_memu.bat` 文件复制到 Android SDK 的 **platform-tools** 文件夹内  
- 配置 `adb_connect_memu.py` 文件内的 **memu_adb_path** 属性  

```python
__memu_adb_path__ = '\"E:/Program Files (x86)/Microvirt/MEmu/adb.exe\"'
```  

- 运行 `adb_connect_memu.bat` 文件  