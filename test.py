import PyIeJs
from time import sleep

PyIeJs.IE_Browser()
sleep(1)
PyIeJs.IE_RunJS('window.location.href="https://www.python.org/";')
PyIeJs.IE_Wate()
print(PyIeJs.IE_Html())