import hou
import toolutils

import socket
import time

##########
# 424 * 512 = 217,088
##########


class tcp():
    def __init__(self, geo):
        self.geo = geo
        pass

    def onConnectClicked(self):
        host='127.0.0.1'
        port = 8889

        self.receivedData = []

        self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serversock.bind((host,port))
        self.serversock.listen(1)

        self.recvThread = TcpThread(self, self.serversock, self.geo)


    def onDisconnectClicked(self):
        print "disconnect"
        self.serversock.close()

    def onCaptureDataClicked(self):
        self.receivedData


    def convertData(data):
        valsStr = data.split(",")[0:-1]
        valsInt = []
        length = len(valsStr)
        for i in range(0,length - 1):
            valsInt[i] = int(valsStr[i])

        return valsInt





from threading import Thread

class TcpThread(Thread):
    def __init__(self, parent, sock, geo):
        Thread.__init__(self)
        self.sock =sock
        self.parent = parent
        self.geo = geo

        self.setDaemon(True)
        self.start()

    def run(self):
        print ('Waiting for connections...')
        clientsock, client_address = self.sock.accept()
        print ("accept")
        msg = bytearray()
        sendToHou =''

        while True:
            
            data = clientsock.recv(4096)
            
            if not data:
                break
            #print str('Received -> %s' % (data))
            if "fin" in str(data):
                msg += data
                #print (str(data)),
                sendToHou = msg
                msg = bytearray()
            else:
                msg += data
                pass

        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except:
            pass

        print ("end")
        self.sock.close()
        #print (len(str(sendToHou)))
        valsInt = self.convertData(str(sendToHou))
        print "aa"
        self.parent.receivedData = valsInt
        print ("bb %d", len(self.geo.points()))
        count = 0
        for pt in self.geo.points():
            pos = pt.position()
            pt.setPosition(hou.Vector3((pos.x(), valsInt[count], pos.z())))
            #if valsInt[count] != 0:
                #print valsInt[count]
            count += 1
        print ("done %d", count)


    def convertData(self, data):
        valsStr = data.split(",")[0:-1]
        length = len(valsStr)
        print (length)
        valsInt = []
        for i in range(0, length):
            valsInt.append(float(valsStr[i]))

        return valsInt




node = hou.pwd()
geo = node.geometry()

tcp = tcp(geo)
tcp.onConnectClicked()


