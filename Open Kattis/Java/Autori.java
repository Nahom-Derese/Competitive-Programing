import java.util.Scanner;

public class Autori {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        String[] input = n.nextLine().split("-");
        for (int i = 0; i < input.length; i++) {
            char ans = input[i].charAt(0);
            System.out.print(ans);
        }
        System.out.print("\n");
        n.close();
    }
}