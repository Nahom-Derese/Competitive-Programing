import java.util.ArrayList;
import java.util.Scanner;

class knotKnowledge{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.nextLine();

        String required = sc.nextLine();
        String[] reqArray = required.split(" ");
        
        String alreadyLearned = sc.nextLine();
        String[] learnedArray = alreadyLearned.split(" ");
        
        ArrayList<String> learnedArrayList = new ArrayList<>();
        for (String i : learnedArray) {
            learnedArrayList.add(i);
        } 

        for (String i : reqArray) {
            if (!learnedArrayList.contains(i)) {
                System.out.println(i);
            }
        }

        sc.close();
    }
}