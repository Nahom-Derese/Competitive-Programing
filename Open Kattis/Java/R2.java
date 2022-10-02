import java.util.Scanner;

public class R2 {
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        String m = n.nextLine();
        String[] u = m.split(" ");
        System.out.println(2*Long.parseLong(u[1]) - Long.parseLong(u[0]));
        n.close();
    }
}
