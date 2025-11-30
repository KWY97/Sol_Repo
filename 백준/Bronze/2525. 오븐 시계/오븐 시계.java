import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();
        int cook = sc.nextInt();

        int totalMinute = 0;

        if (hour == 0) {
            totalMinute = (24 * 60) + minute + cook;
        } else {
            totalMinute = (hour * 60) + minute + cook;
        }

        hour = (totalMinute / 60) % 24;
        minute = totalMinute % 60;

        System.out.println(hour + " " + minute);
    }
}