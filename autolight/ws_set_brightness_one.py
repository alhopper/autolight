#!/usr/bin/env python3

import websocket

# websocket.enableTrace(True)
ws = websocket.WebSocket()
ws.connect("ws://192.168.1.109:81")
ws.send(' { "brightness": 1.0, "save": false } ')
ws.recv()
ws.close()
ws = websocket.WebSocket()
ws.connect("ws://192.168.1.106:81")
ws.send(' { "brightness": 1.0, "save": false } ')
# ws.recv()
ws.close()
