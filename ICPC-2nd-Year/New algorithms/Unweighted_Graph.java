import java.util.ArrayList;

public class Unweighted_Graph extends Graph{
    public void connect(String a, String b) {
        nodes.add(a);
        nodes.add(b);
        ArrayList<String> e = new ArrayList<>();
        e.add(b);
        e.add(String.valueOf(0));
        if(adjList.containsKey(a)) adjList.get(a).add(e);
    }
}   
