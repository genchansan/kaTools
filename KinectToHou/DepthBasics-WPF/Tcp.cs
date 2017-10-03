using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Net.Sockets;
using System.Net;

namespace Microsoft.Samples.Kinect.DepthBasics
{
    class Tcp
    {
        private string serverHost = "127.0.0.1";
        private int serverPort = 8889;

        //private IPEndPoint ipEndPoint;
        private System.Text.Encoding encutf = System.Text.Encoding.UTF8;
        private StringBuilder smsg;
        TcpClient tcp;
        Socket socket;
        //NetworkStream stream;
        MainWindow main;

        public Tcp(MainWindow main, int size)
        {
            this.main = main;
            this.smsg = new StringBuilder(size);
            //this.ipEndPoint = new IPEndPoint(IPAddress.Loopback, this.serverPort);
        }

        public StringBuilder sMsg { set { this.smsg = value; } get { return this.smsg; } }

        public string ServerHost
        {
            set { this.serverHost = value; }
            get { return this.serverHost; }
        }

        public int SreverPort
        {
            set { this.serverPort = value; }
            get { return this.serverPort; }
        }


        public void TcpConnect()
        {
            try
            {
                this.tcp = new TcpClient(this.serverHost, this.serverPort);
                //this.stream = tcp.GetStream();
                this.socket = this.tcp.Client;
                
            }
            catch (Exception ex)
            {
                //Console.WriteLine("socket error : " + ex.ToString());
            }
            //Console.WriteLine(this.stream);
        }

        public void TcpSend()
        {
            byte[] sendBytes = this.encutf.GetBytes(this.sMsg.ToString() + "fin"); 
            //Console.WriteLine(sendBytes.Length);
            if (this.tcp != null && this.tcp.Connected)
            {
                try
                {
                    //this.stream.Write(sendBytes, 0, sendBytes.Length);
                    this.socket.Send(sendBytes);
                }
                catch (Exception ex)
                {
                    Console.WriteLine("error:" + ex.ToString());
                    this.TcpClose();
                    if (this.tcp == null)
                    { 
                        this.TcpConnect();
                    }
                }
            }
            else
            {
                if (this.tcp == null)
                {
                    this.TcpConnect();
                }
            }
        }

        public void TcpClose()
        {
            if (this.tcp != null && this.tcp.Connected)
            {
                //this.stream.Close();
                this.tcp.Close();

                //this.stream = null;
                this.tcp = null;
            }
        }
    }
}
