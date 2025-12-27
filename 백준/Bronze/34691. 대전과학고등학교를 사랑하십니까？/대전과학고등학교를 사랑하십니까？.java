import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (true) {
            String s = sc.nextLine();

            if (s.equals("end")) {
                break;
            } else if (s.equals("animal")) {
                System.out.println("Panthera tigris");
            } else if (s.equals("flower")) {
                System.out.println("Forsythia koreana");
            } else if (s.equals("tree")) {
                System.out.println("Pinus densiflora");
            }
        }

        sc.close();
    }
}
