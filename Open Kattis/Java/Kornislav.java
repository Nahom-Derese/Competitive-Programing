import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

public class Kornislav {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input =  scanner.nextLine();
        String[] list = input.split(" ");
        ArrayList<Integer> sorted = new ArrayList<Integer>();

        for (String i:list) {
            sorted.add(Integer.valueOf(i));
        }
        sorted.sort(Comparator.naturalOrder());
        
        System.out.println(sorted.get(0) * sorted.get(2));

        scanner.close();
    }
}
