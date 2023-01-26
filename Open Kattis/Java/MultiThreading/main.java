
import java.util.*;

public class main {


    public static void main(String[] args){
       

        ArrayList<Integer> l1 =  new ArrayList<Integer>();
        ArrayList<Integer> l2 =  new ArrayList<Integer>();
        
        l1.addAll(Arrays.asList(1,2,3,4,5));
        l2.addAll(Arrays.asList(6,7,8,9,10));
        
        List<Integer> l3 = new ArrayList<Integer>(){{addAll(l1); addAll(l2);}};

        
        for (Integer integer : l3) {
            System.out.println(integer);
        }
        
    }

}
