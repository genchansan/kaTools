import hou
import toolutils
import addExpression
from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtNetwork import *

import socket
import time

class pickerWidget(QtWidgets.QFrame):
    def __init__(self, parent = None):
        QtWidgets.QFrame.__init__(self, parent)

        receivedData = ""

        layout = QtWidgets.QVBoxLayout()

        # set up button
        buttonLayout = QtWidgets.QHBoxLayout()
        self.ConnectButton = QtWidgets.QPushButton("Connect")
        self.DisconnectButton = QtWidgets.QPushButton("Disconnect")
        buttonLayout.addWidget(self.ConnectButton)
        buttonLayout.addWidget(self.DisconnectButton)
        self.ConnectButton.clicked.connect(self.onConnectClicked)
        self.DisconnectButton.clicked.connect(self.onDisconnectClicked)
                
        #layout.addWidget(title)
        layout.addLayout(buttonLayout)
        self.setLayout(layout)



    def onConnectClicked(self):
        #self.serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #self.serversock.bind((host,port))
        #self.serversock.listen(1)

        self.recvThread = TcpThread(self, self.serversock)
        
        self.server = QtNetwork.QTcpServer(self)
        
        if not self.server.listen(QtNetwork.QHostAddress("127.0.0.1"), 8889):
            print("cannot connect")
            return

        self.server.newConnection.connect(self.onNewConnection)


    def onNewConnection(self):
        self.clientConnection = self.server.nextPendingConnection()
        self.clientConnection.disconnected.connect(self.clientConnection.deleteLater)
        self.clientConnection.readyRead.connect(self.onRead)
        #clientConnection.write(block)
        #clientConnection.disconnectFromHost()


    def onRead(self):


    def onDisconnectClicked(self):
        print "disconnect"

    def onCaptureDataClicked(self):
        dataVals = self.convertData(str(self.receivedData)


    def convertData(data):
        valsStr = data.split(",")[0:-1]
        length = len(valsStr)
        print (length)
        valsInt = []
        for i in range(0, length):
            valsInt.append(float(valsStr[i]))

        return valsInt



####################################################



    




####################################################





from threading import Thread

class TcpThread(Thread):
    def __init__(self, widget, sock):
        Thread.__init__(self)
        self.widget = widget
        self.sock = sock

        host='127.0.0.1'
        port = 8889

        
        self.setDaemon(True)
        self.start()

    def run(self):
        print ('Waiting for connections...')
        clientsock, client_address = self.serversock.accept()
        print ("accept")
        msg = bytearray()
        #sendToHou =''

        while True:
            
            data = clientsock.recv(4096)
            
            if not data:
                break
            #print str('Received -> %s' % (data))
            if "fin" in str(data):
                msg += data
                #print (str(data)),
                #sendToHou = msg
                self.widget.receivedData = msg
                msg = bytearray()
            else:
                msg += data
                pass

        try:
            self.socket.shutdown(socket.SHUT_RDWR)
        except:
            pass

        print ("end")
        clientsock.close()
        print (len(str(self.widget.receivedData)))




def createInterface():
    root = pickerWidget()
    return root