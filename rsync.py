import subprocess
import getpass
import os.path

class Rsync(object):
    def __init__(self,user=getpass.getuser(),host='127.0.0.1',port=22):
        self._host = host
        self._port = port
        self._user = user
        self._localRoot = ''
        self._remoteRoot = ''

    def setLocalRoot(self,root):
        self._localRoot = root

    def setRemoteRoot(self,root):
        self._remoteRoot = root

    def sync(self,source,dest):
        source = os.path.join(self._remoteRoot,source)
        dest = os.path.join(self._localRoot,dest)
        command = ['rsync','-P','-e','ssh -p{0!s}'.format(self._port),\
                '{0}@{1}:{2}'.format(self._user,self._host,source),dest]
        subprocess.Popen(command)

