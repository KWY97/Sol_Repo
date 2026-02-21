import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        StringBuilder sb = new StringBuilder();

        while (sc.hasNextLine()) {
            String s = sc.nextLine();
            if (s.isEmpty()) break;

            for (char c : s.toCharArray()) {
                if (c == 'e') sb.append('i');
                else if (c == 'i') sb.append('e');
                else if (c == 'E') sb.append('I');
                else if (c == 'I') sb.append('E');
                else sb.append(c);
            }
            sb.append('\n');
        }

        System.out.print(sb.toString());
        sc.close();
    }
}