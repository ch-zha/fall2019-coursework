import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.net.DatagramPacket;
import java.net.InetAddress;
import java.util.ArrayList;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileProtocol {
	private String file =  "";
	private int PACKET_SIZE = 512;
	private InetAddress localAddr;

	public FileProtocol(InetAddress address) {
		this.localAddr = address;
	}

	public String processInput(String input) {
		String[] inputs = input.split(" ");
		switch (inputs[0]) {
			case "":
				return "Blank input";
			case "index":
				return getFileNames();
			case "get":
				if (inputs.length != 2) return "error";
				return getFileContents(inputs[1]);
			default:
				return "default";
		}
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

	private String getFileContents(String filename) {
		this.file = "./textfiles/" + filename;
		String output = "ok\n"; //TODO make the OK its own packet
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
		return packets;
	}

	private String readPackets(ArrayList<DatagramPacket> packets) {
		return "";
	}
}
