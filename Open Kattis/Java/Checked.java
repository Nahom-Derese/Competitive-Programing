import java.util.*;

public class Checked
{ public static void main(String args[]) 
{ // Create and initialize linked list
LinkedList ll = new LinkedList();
ll.add(-8);
ll.add(20);
ll.add(-20);
ll.add(8);
// Create a reverse order comparator
Comparator r = Collections.reverseOrder();
// Sort list by using the comparator
Collections.sort(ll, r);
// Get iterator
Iterator li = ll.iterator();
System.out.print("List sorted in reverse: ");
while(li.hasNext()){
System.out.print(li.next() + " ");}
System.out.println();
Collections.shuffle(ll);
// display randomized list
li = ll.iterator();
System.out.print("List shuffled: ");
while(li.hasNext()){
System.out.print(li.next() + " ");
}
System.out.println();
System.out.println("Minimum: " + 
Collections.min(ll));
System.out.println("Maximum: " + 
Collections.max(ll));

LinkedList ml = new LinkedList<>();

Collections.copy(ml, ll);

System.out.print("List Coppied: ");
Iterator m = ml.iterator();
while(m.hasNext()){
    System.out.print(m.next() + " ");
}
}
}

