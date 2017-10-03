##########
# 424 * 512 = 217,088
##########



import socket
import time

host='127.0.0.1'
#host = '10.0.2.131'
port = 8889

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serversock.bind((host,port))
serversock.listen(1)
print ('Waiting for connections...')
clientsock, client_address = serversock.accept()
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

print ("end")
clientsock.close()
print (len(str(sendToHou)))





def convertData(data):
        valsStr = data.split(",")[0:-1]
        length = len(valsStr)
        print (length)
        valsInt = []
        for i in range(0, length):
            valsInt.append(float(valsStr[i]))

        return valsInt



node = hou.pwd()
geo = node.geometry()

valsInt = convertData(str(sendToHou))


count = 0
for pt in geo.points():
    pos = pt.position()
    pt.setPosition(hou.Vector3((pos.x(), valsInt[count], pos.z())))
    count += 1

print "fin"