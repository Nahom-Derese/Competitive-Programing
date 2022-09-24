import java.util.Scanner;

public class Greater {

    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        String m = n.nextLine();
        String[] u = m.split(" ");
        if (Integer.parseInt(u[0]) > Integer.parseInt(u[1])) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        n.close();
    }

}