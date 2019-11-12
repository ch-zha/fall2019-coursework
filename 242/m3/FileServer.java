import java.io.BufferedOutputStream;
import java.io.BufferedReader;
import java.io.PrintWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

// The tutorial can be found just here on the SSaurel's Blog : 
// https://www.ssaurel.com/blog/create-a-simple-http-web-server-in-java
// Each Client Connection will be managed in a dedicated Thread
public class FileServer {

	
//    static final File WEB_ROOT = new File(".");
    static final int PORT = 6666;
	
    // Client Connection via Socket Class
    private Socket clientSocket;


    public FileServer(Socket c) {
		clientSocket = c;
    }

    public static void main(String[] args) {
		try (ServerSocket serverConnect = new ServerSocket(PORT)) {
			System.out.println("cd ../Server started.\nListening for connections on port : " + PORT + " ...\n");

			// we listen until user halts server execution
			while (true) {
				FileServer myServer = new FileServer(serverConnect.accept());
				myServer.handleRequest();
			}

		} catch (IOException e) {
			System.err.println("Server Connection error : " + e.getMessage());
		}
    }

    public void handleRequest() {
		try (
				// ...
				PrintWriter out =
						new PrintWriter(clientSocket.getOutputStream(), true);
				BufferedReader in = new BufferedReader(
						new InputStreamReader(clientSocket.getInputStream()));
		) {
			// Initiate conversation with client
			FileProtocol fp = new FileProtocol();
			String input, output;

			while ((input = in.readLine()) != null) {
				output = fp.processInput(input);
				System.out.println("Client: " + input);
				System.out.println("Output: " + output);
				out.println(output);
				out.flush();
				if (input.equals("ready") || input.equals("index") || output.equals("error")) {
					break;
				}
			}
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			System.out.println("Connection closed");
		}
	}
	
}
