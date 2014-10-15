#!/usr/bin/python
#
# by Fabien Royer, Bertrand Le Roy
#
# Copyright (C) 2013 Nwazet http://nwazet.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
#
# Full license and additional terms are specified in the license.txt file
# that accompanies this program.
#
from subprocess import call
import SimpleHTTPServer
import SocketServer
import threading
import time
import os
 
Port = 8080
WorkingDirectory = "/home"
PictureSettingsPath = "/home/snapshot.txt"
DefaultPictureSettings = "raspistill -w 1920 -h 1080 -q 100 -o /home/latest.jpg -e jpg -awb auto -n"
 
 
def ReadPictureSettings(settingsPath):
    try:
        with open(settingsPath, 'r') as f:
            cmd = f.readline().strip()
    except Exception as e:
        print("Oops: " + e.__str__())
        cmd = DefaultPictureSettings
    return cmd.split(' ')
 
 
def TakeSnapShot(interval):
    while True:
        call(ReadPictureSettings(PictureSettingsPath))
        print "Snap!"
        time.sleep(interval)
 
os.chdir(WorkingDirectory)
 
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
Httpd = SocketServer.TCPServer(("0.0.0.0", Port), Handler)
t = threading.Thread(target=TakeSnapShot, args=(5,))
 
print "SimpleHTTPServer listening on port", Port
 
t.start()
Httpd.serve_forever()