import java.util.Scanner;

public class Autori2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        String a = scanner.nextLine();

        String[] b = a.split("-");
        
        for (String i : b) {
            System.out.print(i.charAt(0));
        }

    }
}
