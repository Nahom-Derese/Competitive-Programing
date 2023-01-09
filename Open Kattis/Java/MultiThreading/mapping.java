import java.util.*;

public class mapping {
    public static void main(String[] args) {
        Map<String, Double> m1 = new TreeMap<String, Double>();
        m1.put("Damtew", 60000.0);
        m1.put("Kefyalew", 30000.0);
        m1.put("Anella", 70000.0);
        Double total = 0.0;

        for (Double integer : m1.values()) {
            total += integer;
        }

        System.out.println(String.format("MAX = %s", Collections.max(m1.values())) );
        System.out.println(String.format("MIN = %s", Collections.min(m1.values())) );
        System.out.println(String.format("Total = %s", total ) );
        System.out.println(String.format("AVERAGE = %s", total/m1.values().size() ) );
        
        System.out.println();

        for (Map.Entry<String, Double> mEntry : m1.entrySet()) {
            System.out.println(String.format("%s => %s", mEntry.getKey() , mEntry.getValue()) );
        }
        


    }

}
