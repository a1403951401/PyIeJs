name = "PyIeJs"

import clr
from os.path import dirname, abspath

clr.AddReference(dirname(abspath(__file__)) + "/dll/Martin")
import Martin

ie = Martin.IE()

def IE_RunJS(JS, hwnd = 0):
    return ie.IERunJS(hwnd, JS)

# 获取指定句柄的 IE浏览器 标题
def IE_GetTitle(hwnd = 0):
    return ie.IEGetTitle(hwnd)

# 获取指定句柄的 IE浏览器 链接
def IE_GetUrl(hwnd = 0):
    return ie.IEGetUrl(hwnd)

# 启用一个新的 IE浏览器
def IE_Browser(url = None):
    return ie.NewIE(url)

# 根据句柄获取 获取 HTML 页面的内容
def IE_Html(hwnd = 0):
    return ie.IEHtml(hwnd)

# 根据句柄获取 获取 HTML 页面的 BODY 内容
def IE_Body(hwnd = 0):
    return ie.IEBody(hwnd)

# 操作当前 IE浏览器 返回
def IE_GoBack(hwnd = 0):
    return ie.IEGoBack(hwnd)

# 操作当前 IE浏览器 前进
def IE_GoForward(hwnd = 0):
    return ie.IEGoForward(hwnd)

# 操作当前 IE浏览器 刷新
def IE_Refresh(hwnd = 0):
    return ie.IERefresh(hwnd)

# 获取 IE浏览器 当前状态    如果页面正在加载 则返回 true          该方法不会检测JS的加载
def IE_Busy(hwnd = 0):
    return ie.IEBusy(hwnd)

# 等待页面加载完成，未完成前不会返回！！，返回等待时间            该方法不会检测JS的加载
def IE_Wate(hwnd=0):
    return ie.IEWate(hwnd)