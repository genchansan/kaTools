import hou
import toolutils
import socket
import time

##########
# 424 * 512 = 217,088
##########


class tcp():
    def __init__(self, geo, address, port):
        self.geo = geo
        self.address = address
        self.port = port


    def onConnectClicked(self):
        host=self.address
        port = self.port

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


####################################################


from threading import Thread

class TcpThread(Thread):

    sendToHou = ''

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
        #count = 0

        while True:
            
            data = clientsock.recv(4096)
            
            if not data:
                break
            #print str('Received -> %s' % (data))
            if "fin" in str(data):
                msg += data
                #print (str(data)),
                self.sendToHou += str(msg)

                self.applyData()


                msg = bytearray()
                
            else:
                msg += data
                pass

            #count+=1

        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except:
            pass

        print ("end")
        self.sock.close()
        #print (len(self.sendToHou))
        print ("done")


    def applyData(self):
        valsInt = self.convertData(self.sendToHou)
        if valsInt == None:
            return
        elif len(valsInt) !=  217088:
            print ("short length")
            return

        count = 0
        for pt in geo.points():
            pos = pt.position()
            pt.setPosition(hou.Vector3((pos.x(), valsInt[count], pos.z())))
            count += 1
        
        xformNode.cook(True)


    def convertData(self, data):
        split = data.split("fin")
        self.sendToHou = split[1]
        valsStr = split[0].split(",")
        length = len(valsStr)
        #print (length)
        valsInt = []
        for i in range(0, length-1):
            try:
                valsInt.append(float(valsStr[i]))
            except ex:
                print "error: to make array"
                return None

        return valsInt


####################################################
        
global geo
global xformNode


node = hou.pwd()
geo = node.geometry()
xformNode = hou.node("../null1")
address = node.parm("address").eval()
port = node.parm("port").eval()


if node.parm("enable_capture").eval() == 1:
    tcpsock = tcp(geo, address, port)
    tcpsock.onConnectClicked()


