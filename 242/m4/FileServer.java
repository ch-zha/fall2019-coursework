import javax.xml.crypto.Data;
import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.DatagramSocket;
import java.net.InetAddress;
import java.net.Socket;
import java.util.ArrayList;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileServer {

    static final int DESTINATION = 6969;

    public static void main(String[] args) {
		try (DatagramSocket socket = new DatagramSocket(6666)) {

			System.out.println("Receiving data........ ");
			while (true) {
				byte[] buf = new byte[512];
				// get msg
				DatagramPacket packet = new DatagramPacket(buf, buf.length);
				socket.receive(packet);
				// display msg
				String received = new String(packet.getData(), 0, packet.getLength());
				System.out.println(received);

				// prepare response
				FileProtocol fp = new FileProtocol(InetAddress.getLocalHost(), DESTINATION);
				ArrayList<DatagramPacket> response = fp.processInput(received);
				// send response
				for (DatagramPacket responsePacket : response) socket.send(responsePacket);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
	
}
