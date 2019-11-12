import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.net.UnknownHostException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.Socket;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileClient {

    public static void main(String[] args) {
//		if (args.length != 2) {
//			//error msg
//			System.exit(1);
//		}

		String hostName = "localhost"; //args[0];
		int portNumber = 6666; //Integer.parseInt(args[1]);

		try (
				Socket socket = new Socket(hostName, portNumber);
				PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
				BufferedReader in = new BufferedReader(
						new InputStreamReader(socket.getInputStream()));
		) {
			String fromUser = "";
			if (args[0].equals("index")) fromUser = args[0];
			else if (args[0].equals("get")) {
				if (args.length != 2) {
					System.out.println("Error reading file name.");
					System.exit(10);
				}
				fromUser = args[0] + " " + args[1];
			} else {
				System.out.println("Please use the command \'index\' or \'get\' followed by a file name.");
				System.exit(10);
			}
			System.out.println("Client: " + fromUser);
			out.println(fromUser);
			out.flush();

			String fromServer;
			while ((fromServer = in.readLine()) != null) {
				System.out.println(fromServer);
				if (fromServer.equals("ok")) {
					out.println("ready");
				}
			}
		} catch (UnknownHostException e) {
			System.err.println("Don't know about host " + hostName);
			System.exit(1);
		} catch (IOException e) {
			System.err.println("Couldn't get I/O for the connection to " +
					hostName);
			System.exit(1);
		}
    }

}
