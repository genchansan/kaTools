using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Microsoft.Samples.Kinect.DepthBasics
{
    using System;
    using System.Collections.Generic;
    //using System.Linq;
    using System.Text;
    using System.Net;
    using System.Net.Sockets;
    using System.Threading;
    using System.Windows;
    using System.Windows.Controls;
    using System.Windows.Controls.Primitives;

    //public delegate void SenseEnabledHandler(object sender, /*EventArgs*/int e);


    public class Udp
    {
        #region defines

        public string sendMsg;
        private int rcvmsgint = 0;
        public System.Net.Sockets.UdpClient udp;
        private string remoteHost = "127.0.0.1";//"192.168.100.111";//"10.0.2.15";//"172.20.10.6";//
        private string localHost = "127.0.0.1";//"192.168.100.200";//"127.0.0.1";//"172.20.10.7";//
        private int remotePort = 8889;
        private int localPort = 8891;
        //public int recvPort = 8891;
        private System.Text.Encoding encutf = System.Text.Encoding.UTF8;
        private StringBuilder smsg = new StringBuilder(200);
        MainWindow main;
        //CheckBox checkbox;
        //ComboBox combobox;
        //Button[] button;

        //public event SenseEnabledHandler SenseEnabled;

        public Udp(MainWindow main) { this.main = main;}

        public StringBuilder sMsg { set { this.smsg = value; } get { return this.smsg; } }

        public string RemoteHost
        {
            set { this.remoteHost = value; }
            get { return this.remoteHost; }
        }

        public string LocalHost
        {
            set { this.localHost = value; }
            get { return this.localHost; }
        }

        public int RemotePort
        {
            set { this.remotePort = value; }
            get { return this.remotePort; }
        }

        public int LocalPort
        {
            set { this.localPort = value; }
            get { return this.localPort; }
        }


        #endregion


        public void UDPConnect(int connectPort, int sendPort, string sendIP, string type)
        {
            try
            {
                this.udp = new System.Net.Sockets.UdpClient(connectPort);
                this.udp.Client.SetSocketOption(SocketOptionLevel.Socket, SocketOptionName.ReuseAddress, true);
                this.udp.DontFragment = true;
                this.udp.EnableBroadcast = true;
                if (type == "send")
                {
                    this.udp.Connect(sendIP, sendPort);
                }
                else if (type == "recv")
                {
                    //this.udp.BeginReceive(this.UDPReceive, this.udp);
                }
            }
            catch (Exception ex)
            {
                Console.WriteLine("ここが" + ex);
            }
        }


        public void UDPSend()
        {
            //byte[] sendBytes = this.encutf.GetBytes(this.sendMsg);
            byte[] sendBytes = this.encutf.GetBytes(this.sMsg.ToString());
            if (this.udp != null)
            {
                try
                {
                    this.udp.Send(sendBytes, sendBytes.Length);
                    //                    Console.WriteLine(this.sendMsg);
                    //                    Console.WriteLine(BitConverter.ToString(sendBytes));
                    //                    Console.WriteLine(sendBytes.Length);
                }
                catch (Exception ex)
                {
                    this.udp.Close();
                    this.udp = null;
                    Console.WriteLine("ここのエラーは{0}", ex);
                }
            }
        }
/*
        public void UDPReceive(IAsyncResult AR)
        {
            System.Net.IPEndPoint remoteEP = new System.Net.IPEndPoint(System.Net.IPAddress.Any, 0);
            if (this.udp != null)
            {
                //byte[] rcvBytes = this.udp.Receive(ref remoteEP);
                byte[] rcvBytes = this.udp.EndReceive(AR, ref remoteEP);
                string rcvMsg = this.encutf.GetString(rcvBytes);
                try
                {
                    this.RcvMsgInt = int.Parse(rcvMsg);
                }
                catch (Exception ex)
                {
                    Console.WriteLine(ex);
                }
                Console.WriteLine("rcvmsg is : " + this.rcvmsgint.ToString());
                //Console.WriteLine("送信元アドレス:{0}/ポート番号:{1}", remoteEP.Address, remoteEP.Port);

                //try
                //{
                //    //main.SensToggleChange();
                //    Console.WriteLine(AR.AsyncState);
                //}
                //catch (Exception ex)
                //{
                //    Console.WriteLine(ex);
                //}
                this.udp.BeginReceive(this.UDPReceive, this.udp);

            }
        }
*/
        public void UDPClose()
        {
            if (this.udp != null)
            {
                this.udp.Close();
                this.udp = null;
            }
        }
    }
}
