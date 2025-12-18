import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        double maxScore = 0;
        double totalScore = 0d;
        double average;
        double[] scores = new double[n];

        for (int i = 0; i < n; i++) {
            double score = sc.nextDouble();
            scores[i] = score;

            if (maxScore < score) {
                maxScore = score;
            }
        }

        for (double score : scores) {
            totalScore += score / maxScore * 100;
        }

        average = totalScore / n;
        System.out.println(average);
    }
}
