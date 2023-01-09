import java.util.LinkedList;
import java.util.ListIterator;


public class Adama {
    public static void main(String[] args) {
        
    LinkedList<String> staff = new LinkedList<String>();
    ListIterator<String> iterator = staff.listIterator();
    iterator.add("Addis");
    
    iterator.add("Adama");
    
    iterator.add("Awasa");
    
    iterator = staff.listIterator();
    
    iterator.next();
    
    iterator.next();
    
    iterator.add("Bishoftu");
    
    iterator.next();
    
    iterator.add("Diredawa");
    
    iterator = staff.listIterator();
    
    iterator.next();
    
    iterator.remove();
    while (iterator.hasNext()) { System.out.println(iterator.next()); 
    }
    }
}
