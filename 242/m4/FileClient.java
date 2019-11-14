import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.InetAddress;
import java.net.*;
import java.io.InputStreamReader;
import java.io.OutputStream;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileClient {

    public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Please enter at least one argument.");
			System.exit(1);
		}

		int portNumber = 6969;
		try (DatagramSocket socket = new DatagramSocket(portNumber)) {
			// send request
			String input = args[0];
			if (args.length == 2) input += " " + args[1];
			byte[] buf = input.getBytes();
			DatagramPacket packet = new DatagramPacket(buf, buf.length, InetAddress.getLocalHost(), 6666);
			socket.send(packet);

			// get response
			while (true) {
				buf = new byte[512];
				packet = new DatagramPacket(buf, buf.length);
				socket.receive(packet);

				// display response
				String received = new String(packet.getData(), 0, packet.getLength());
				System.out.println("Packet: " + received);
			}
		} catch (IOException e) {
			e.printStackTrace();
		}

    }

}
