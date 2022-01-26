# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/27
import time

import win32clipboard

old = ""

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if old != data:
        with open("clip_history.txt", "+a") as f:
            f.write(data + "\n")
            old = data
    time.sleep(0.5)
