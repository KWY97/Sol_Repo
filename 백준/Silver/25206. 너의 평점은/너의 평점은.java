import java.util.Scanner;

public class Main {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        // 학점 × 과목평점
        double creditSubjectSum = 0;
        // 학점 총합
        double creditSum = 0;

        for (int i = 0; i < 20; i++) {
            String subject = sc.next();
            double credit = sc.nextDouble();
            String grade = sc.next();

            if (grade.equals("P")) {
                continue;
            }

            creditSum += credit;

            switch (grade) {
                case "A+":
                    creditSubjectSum += credit * 4.5;
                    break;
                case "A0":
                    creditSubjectSum += credit * 4;
                    break;
                case "B+":
                    creditSubjectSum += credit * 3.5;
                    break;
                case "B0":
                    creditSubjectSum += credit * 3;
                    break;
                case "C+":
                    creditSubjectSum += credit * 2.5;
                    break;
                case "C0":
                    creditSubjectSum += credit * 2;
                    break;
                case "D+":
                    creditSubjectSum += credit * 1.5;
                    break;
                case "D0":
                    creditSubjectSum += credit * 1;
                    break;
                case "F":
                    creditSubjectSum += credit * 0;
                    break;
            }
        }
        System.out.println(creditSubjectSum / creditSum);
    }
}
