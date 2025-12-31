import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String[] croAlpha = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        String s = sc.nextLine();
        sc.close();

        for (int i = 0; i < croAlpha.length; i++) {
            if (s.contains(croAlpha[i])) {
                s = s.replace(croAlpha[i], "*");
            }
        }
        
        System.out.println(s.length());
    }
}
