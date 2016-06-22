#!/usr/bin/python
#

import time,hashlib,subprocess,socket,os,json

dir = os.path.dirname(os.path.realpath(__file__))
cfg = None

with open(dir + "/tunnel.json") as file:
    cfg = json.load(file)
    file.close()

if cfg is not None:
    hbBase = "HEARTBEAT TUNNEL " + cfg["local"] + " sender " + str(int(time.time()))
    hbToSend = hbBase + " " + hashlib.md5(hbBase + " " + cfg["password"]).hexdigest()
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(hbToSend, (cfg["remote"], 3740))
    sock.close()