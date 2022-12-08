#!/usr/bin/env python3

import websocket

# websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://192.168.1.109:81")
ws.send(' { "brightness": 0.0, "save": false } ')
ws.recv()
ws.close()
ws1 = websocket.WebSocket()
ws1.connect("ws://192.168.1.106:81")
ws1.send(' { "brightness": 0.0, "save": false } ')
# ws1.recv()
ws1.close()
