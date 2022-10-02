import java.util.Scanner;

public class ColdPuterScience {
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        int in = Integer.parseInt(n.nextLine());
        String[] input = n.nextLine().split(" ");
        int count = 0;
        for (int i = 0; i < in; i++) {
            if (Integer.parseInt(input[i]) < 0) {
                count++;
            }
        }
        System.out.println(count);
        n.close();
    }
}
