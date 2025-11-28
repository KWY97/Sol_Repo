import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sleepTime = sc.nextInt();
        int wakeupTime = sc.nextInt();

        System.out.println((wakeupTime + 24 - sleepTime) % 24);
    }
}