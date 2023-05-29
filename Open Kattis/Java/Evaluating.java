import java.util.Scanner;

public class Evaluating {
    public static void main(String[] args) {
        String input;
        Scanner scanner = new Scanner(System.in);

        input = scanner.nextLine();

        int currentNo = 0;
        int summation = 0;

        for (int i = 0; i < input.length(); i++) {
            Character j = input.charAt(i);
            if(j.equals('O')){
                currentNo++;
                summation = summation + currentNo;
            }
            else{
                currentNo = 0;
            }
        }

        System.out.println(summation);
        scanner.close();
    }
}
