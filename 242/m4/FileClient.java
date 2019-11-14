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
import java.util.ArrayList;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileClient {

    public static void main(String[] args) {
		if (args.length < 1) {
			System.out.println("Please enter at least one argument.");
			System.exit(1);
		}

		int DESTINATION = 6666;
		try (DatagramSocket socket = new DatagramSocket(6969)) {
			socket.setSoTimeout(10000);
			// send request
			String input = args[0];
			if (args.length == 2) input += " " + args[1];
			byte[] buf = input.getBytes();
			DatagramPacket packet = new DatagramPacket(buf, buf.length, InetAddress.getLocalHost(), DESTINATION);
			socket.send(packet);

			// get response
			FileProtocol fp = new FileProtocol(InetAddress.getLocalHost(), DESTINATION);
			ArrayList<DatagramPacket> received = new ArrayList<>();
			try {
				//receive first packet
				buf = new byte[512];
				packet = new DatagramPacket(buf, buf.length);
				socket.receive(packet);

				if (new String(packet.getData(), 0, packet.getLength()).equals("error")) {
					System.out.println("Error getting file. Check file name and try again.");
					System.exit(1);
				}

				int receivedPackets = 1;
				int numPackets = fp.getTotalPackets(packet);
				received.add(packet);

				while (receivedPackets < numPackets) {
					buf = new byte[512];
					packet = new DatagramPacket(buf, buf.length);
					socket.receive(packet);
					received.add(packet);
					receivedPackets ++;
				}
			} catch (SocketTimeoutException e) {
				System.out.println("Timed out before receiving full file. Please try again.");
			}
			// display response
			System.out.println(fp.readPackets(received));

		} catch (IOException e) {
			e.printStackTrace();
		}

    }

}
