import java.util.*;

public class Check {

    public static void main(String[] args){
        List<Integer> a = List.of(3, 4,5,8 , 3);
        Set<Integer> b = Set.of(3, 11,5,12, 10 );
        Collection c;

        //          List 
        ArrayList<Integer> arrayList = new ArrayList<Integer>(a);
        LinkedList<Integer> linkedList = new LinkedList<Integer>(a);
        Vector<Integer> vector = new Vector<Integer>(a);
        Stack<Integer> stack = new Stack<Integer>();

        //         Set
        HashSet<Integer> hashSet = new HashSet<Integer>(b);
        LinkedHashSet<Integer> linkedHashSet = new LinkedHashSet<Integer>(b);
        TreeSet<Integer> treeSet = new TreeSet<Integer>(b);
        
        //         Qeuee
        PriorityQueue<String> priorityQeuee = new PriorityQueue<String>();
        ArrayDeque<String> arrayDeQueue = new ArrayDeque<String>();

        //         Map
        HashMap<Integer, String> hashMap = new HashMap<Integer, String>(){{put(1, "One"); put(2, "Two");}};
        LinkedHashMap<Integer, String> linkedHashMap = new LinkedHashMap<Integer, String>(){{put(1, "One"); put(2, "Two");}};
        TreeMap<Integer, String> treeMap = new TreeMap<Integer, String>(){{put(1, "One"); put(2, "Two");put(4, "Four"); put(3, "Three");}};


        // Looping through List
        System.out.println("\n Looping through List \n "); 
        Iterator<Integer> listItr = stack.iterator();
        while(listItr.hasNext()) {
            System.out.println(listItr.next());
        }

         // Looping through Set
         System.out.println("\n Looping through Set \n");
         Iterator<Integer> setItr = treeSet.iterator();
         while(setItr.hasNext()) {
             System.out.println(setItr.next());
         }

         // Looping through Map
         System.out.println("\n Looping through Set \n");
         for (Map.Entry<Integer, String> mEntry : treeMap.entrySet()) {
            System.out.println(String.format("%s   =>   %s", mEntry.getKey() , mEntry.getValue()));
         }


         // Looping through Queue
         System.out.println("\n Looping through Queue \n");
         arrayDeQueue.add("String");
         arrayDeQueue.add("Check");
         arrayDeQueue.add("Loop");
         Iterator<String> queueItr = arrayDeQueue.iterator();
        while(queueItr.hasNext()) {
            System.out.println(queueItr.next());
        }

        class TestGenericsMethod {
            public static <E>void printArray(E[] elements){
            for(E element : elements){
            System.out.println(element);
            }
            System.out.println();
            } 
        }

        Integer[] intArray = {10,20,30,40,50};
            Character[]charArray={'C','S','E','-','A','S','T','U'};
            System.out.println("Printing Integer Array");
            TestGenericsMethod.printArray(intArray);
            System.out.println("Printing Character Array");
            TestGenericsMethod.printArray(charArray);
    }
}
