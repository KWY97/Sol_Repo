import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int studentCount = 30;
        int checkHomework[] = new int[studentCount];

        for (int i = 1; i <= 28; i++) {
            int studentNum = sc.nextInt();
            studentNum -= 1;
            checkHomework[studentNum] = 1;
        }

        for (int i = 0; i < studentCount; i++) {
            if (checkHomework[i] == 0) {
                System.out.println(i+1);
            }
        }
    }
}