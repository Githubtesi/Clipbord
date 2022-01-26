# -*- coding: utf-8 -*-
# Created by yoshiaki at 2022/01/27
import threading
import time

import win32clipboard

counter = 0

clips = ["", "", "", "", ""]


def process_input():
    while True:
        choice = int(input())
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardText(clips[choice], win32clipboard.CF_TEXT)
        win32clipboard.CloseClipboard()


threading.Thread(target=process_input).start()

while True:
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()
    if data not in clips:
        clips[counter] = data
        counter += 1
        counter %= 5
        print(clips)
    time.sleep(0.5)