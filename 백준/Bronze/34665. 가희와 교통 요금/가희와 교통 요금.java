import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String firstStation = sc.nextLine();
        String secondStation = sc.nextLine();

        if (firstStation.equals(secondStation)) System.out.println(0);
        else System.out.println(1550);
    }
}
