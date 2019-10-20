import java.util.ArrayList;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main extends Thread {

    private int id;

    public void run() {
        while (true) {
            printMsg();
            try {
                this.sleep(2000);
            } catch (InterruptedException e) {
                return;
            }
        }
    }

    public void printMsg() {
        System.out.println("Hello World! I'm " + this.getName() + ". The current time is " + System.currentTimeMillis());
    }

    private static void printPrompt() {
        System.out.println("Here are your options: \na - Create a new thread \nb - Stop a given thread \nc - Stop all threads and exit this program");
    }

    public static void main(String[] args) throws InterruptedException {
        ArrayList<Main> threads = new ArrayList<>();
        Pattern threadno = Pattern.compile("[0-9]+");

        Scanner scanner = new Scanner(System.in);
        String input;
        printPrompt();
        do {
            input = scanner.nextLine();
            if (input.startsWith("b")) {
                Matcher threadname = threadno.matcher(input);
                if (threadname.find()) {
                    int thread = Integer.parseInt(threadname.group(0));
                    if (thread < threads.size()) {
                        threads.get(thread).interrupt();
                        System.out.println("Interrupted "+ threads.get(thread).getName());
                    } else {
                        System.out.println("That thread does not exist.");
                    }
                } else {
                    System.out.println("You did not enter a thread number.");
                }
            } else if (input.startsWith("a")) {
                threads.add(new Main());
                threads.get(threads.size() - 1).start();
                System.out.println("Created " + threads.get(threads.size() - 1).getName());
            } else if (input.startsWith("c")) {
                scanner.close();
                for (Main thread : threads) {
                    thread.interrupt();
                }
                return;
            }
            printPrompt();
        } while (true);
    }
}