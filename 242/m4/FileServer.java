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

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileServer {

    static final int PORT = 6666;

    public static void main(String[] args) {
		try (DatagramSocket socket = new DatagramSocket(PORT)) {
			System.out.println("Receiving data........ ");
			byte[] buf = new byte[512];
			// get msg
			DatagramPacket packet = new DatagramPacket(buf, buf.length);
			socket.receive(packet);
			// display msg
			String received = new String(packet.getData(), 0, packet.getLength());
			System.out.println(received);

			// prepare response
			FileProtocol fp = new FileProtocol(InetAddress.getLocalHost());
			String response = fp.processInput(received);

			// send response
			buf = response.getBytes(); //TODO chop into bite sized pieces
			packet = new DatagramPacket(buf, buf.length, InetAddress.getLocalHost(), 6969);
			socket.send(packet);
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
	
}
