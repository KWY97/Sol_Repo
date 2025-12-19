import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        char[] arr = s.toCharArray();

        char[] english = new char[26];
        for (int i = 0; i < 26; i++) {
            english[i] = (char) (i + 'a');
        }

        int[] count = new int[26];
        for (int i = 0; i < 26; i++) {
            count[i] = -1;
        }

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < english.length; j++) {
                if ((arr[i] == english[j]) && (count[j] == -1)) {
                    count[j] = i;
                }
            }
        }

        for (int i = 0; i < count.length; i++) {
            if (i > 0) {
                System.out.print(" ");
            }
            System.out.print(count[i]);
        }
    }
}