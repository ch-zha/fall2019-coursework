import java.util.ArrayList;
import java.io.FileReader;
import java.io.FileNotFoundException;
import java.io.IOException;

public class LineCounter {

    public static void main(String[] args) {
    	if (args.length < 1) {
    		System.out.println("Please enter at least one file name.");
    		return;
		}

    	ArrayList<String> files = new ArrayList<>();
    	for (String arg : args) {
			files.add(arg);
		}

    	for (String file : files) {
    		int numlines = processFile(file);
    		if (numlines == -1) {
				System.out.println("Error processing " + file);
			}
			else {
				System.out.println("Lines in " + file + ": " + numlines);
			}
		}
    }

    private static int processFile(String file) {
    	int linecount = 0;
    	try (FileReader reader = new FileReader(file)) {
			int nextChar = 0;
			while ((nextChar = reader.read()) != -1) {
				if ((char) nextChar == "\n".charAt(0)) linecount++;
			}
		} catch (IOException e) {
    		e.printStackTrace();
    		return -1;
		}
    	return linecount + 1;
	}
}
