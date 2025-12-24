import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] arr = sc.nextLine().toUpperCase().toCharArray();

        Map<Character, Integer> eng = new HashMap<>();
        for (char c = 'A'; c <= 'Z'; c++) eng.put(c, 0);

        for (char c : arr) eng.put(c, eng.get(c) + 1);

        int max = 0;
        for (int v : eng.values()) {
            if (v > max) max = v;
        }

        int count = 0;
        char result = '?';
        for (Map.Entry<Character, Integer> e : eng.entrySet()) {
            if (e.getValue() == max) {
                result = e.getKey();
                count++;
            }
        }

        System.out.println(count == 1 ? result : '?');
    }
}
