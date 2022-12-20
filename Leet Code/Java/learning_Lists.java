import java.util.*;

public class learning_Lists {
    public static void main(String[] args) {

        TreeMap<String,Integer> m1 = new TreeMap<String, Integer>();

        m1.put("CSE",1000);
        m1.put("SE",2000);
        m1.put("EPCE",3000);
        m1.put("ECE",4000);

        int min = Integer.MAX_VALUE;
        int max = 0;
        int total = 0;


        // Total 
        for(Map.Entry<String, Integer> m:m1.entrySet()){
            int a = Integer.valueOf((m.getValue().toString()));
            if (a  >= max) {
                max = a;
            }
            if (a  <= min) {
                min = a;
            }
            total += a;
        }
        
        System.out.println();
        System.out.println("EMPLOYEES SORTED BY ALPHABET \n ");
        
        for(Map.Entry<String, Integer> m:m1.entrySet()){
            System.out.println(m.getKey() );
        }
        
        System.out.println();
        System.out.println("MIN AND MAX SALARY EMP \n ");

        for(Map.Entry<String, Integer> m:m1.entrySet()){
            int a = Integer.valueOf((m.getValue().toString()));
            if (a  == max) {
                System.out.println("MAX = " + m.getKey());
            }
            if (a  == min) {
                System.out.println("MIN  = " + m.getKey());
            }
            if (a  == total / 2) {
                System.out.println("AVE =" + m.getKey());
            }
        }
        
        
        System.out.println();
        System.out.println("MIN MAX AND TOTAL SALARIES \n");
        
        System.out.println("MIN : " + min);
        System.out.println("MAX : " + max);
        System.out.println("TOTAL : " + total);
        System.out.println();

    }
}
