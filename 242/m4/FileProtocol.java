import javax.xml.crypto.Data;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.util.ArrayList;
import java.util.Arrays;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileProtocol {
	private String file =  "";
	private int PACKET_SIZE = 512;
	private InetAddress localAddr = null;
	private int destPort = 0;

	public FileProtocol(InetAddress address, int destPort) {
		this.localAddr = address;
		this.destPort = destPort;
	}

	public ArrayList<DatagramPacket> processInput(String input) {
		String[] inputs = input.split(" ");
		ArrayList<DatagramPacket> response = new ArrayList<>();
		switch (inputs[0]) {
			case "":
				response.add(prepareSingleDatagram("blank input"));
				return response;
			case "index":
				return stuffPackets(getFileNames());
			case "get":
				if (inputs.length != 2) {
					response.add(prepareSingleDatagram("error"));
					return response;
				}
				return prepareTextFile(inputs[1]);
			default:
				response.add(prepareSingleDatagram("default"));
				return response;
		}
	}

	private DatagramPacket prepareSingleDatagram(String contents) {
		byte[] buf = contents.getBytes();
		return new DatagramPacket(buf, buf.length, localAddr, destPort);
	}

	private String getFileNames() {
		String output = "";
		File dir = new File("./textfiles/");
		String[] files = dir.list();
		for (String filename : files) {
			output += filename;
			if (!filename.equals(files[files.length-1])) output += "\n";
		}
		return output;
	}

	private ArrayList<DatagramPacket> prepareTextFile(String filename) {
		ArrayList<DatagramPacket> packets = new ArrayList<>();
		String fileContents = getFileContents(filename);
		if (fileContents.equals("error")) {
			byte[] output = "error".getBytes();
			packets.add(new DatagramPacket(output, output.length, localAddr, destPort));
		} else {
			packets = stuffPackets(fileContents);
		}
		return packets;
	}

	private String getFileContents(String filename) {
		this.file = "./textfiles/" + filename;
		String output = "";
		try (FileReader reader = new FileReader(this.file)) {
			int nextChar = 0;
			while ((nextChar = reader.read()) != -1) {
				output += (char) nextChar;
			}
			return output;
		} catch (IOException e) {
			e.printStackTrace();
			return "error";
		}
	}

	private ArrayList<DatagramPacket> stuffPackets(String content) {
		ArrayList<DatagramPacket> packets = new ArrayList<>();
		byte[] contentAsBytes = content.getBytes();
		int index = 0;
		int packet = 1;
		int totalPackets = (int) Math.ceil((double) contentAsBytes.length/(double) PACKET_SIZE);
		do {
			// Create header
			byte[] header = (packet + "/" + totalPackets + "\n").getBytes();
			// Fill remaining packet with content
			byte[] buf = Arrays.copyOf(header, PACKET_SIZE);
			for (int i = header.length; index < contentAsBytes.length && i < PACKET_SIZE; index++, i++) {
				buf[i] = contentAsBytes[index];
			}
			packets.add(new DatagramPacket(buf, buf.length, localAddr, destPort));
			packet++;
		} while (index < contentAsBytes.length);
		return packets;
	}

	private int getPacketNumber (DatagramPacket packet) {
		String received = new String(packet.getData(), 0, packet.getLength());
		String header = received.split("\n")[0];
		return Integer.parseInt(header.split("/")[0]);
	}

	public int getTotalPackets (DatagramPacket packet) {
		String received = new String(packet.getData(), 0, packet.getLength());
		String header = received.split("\n")[0];
		int numPackets = Integer.parseInt(header.split("/")[1]);
		return numPackets;
	}

	public String readPackets(ArrayList<DatagramPacket> packets) {
		int numPackets = getTotalPackets(packets.get(0));
		String[] packetsInOrder = new String[numPackets];
		Arrays.fill(packetsInOrder, "");
		for (DatagramPacket packet : packets) {
			packetsInOrder[getPacketNumber(packet) - 1] = new String(packet.getData(), 0, packet.getLength());
		}
		String output = "";
		for (String contents : packetsInOrder) {
			String[] rawContents = contents.split("\n");
			for (int i = 1; i < rawContents.length; i++) {
				output += rawContents[i];
				if (i < rawContents.length-1) output += "\n";
			}
		}
		return output;
	}
}
