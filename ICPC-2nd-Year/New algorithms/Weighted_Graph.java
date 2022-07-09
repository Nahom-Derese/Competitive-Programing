import java.util.ArrayList;

public class Weighted_Graph extends Graph {
    public void connect(String a, String b, int c) {
        nodes.add(a);
        nodes.add(b);
        ArrayList<String> e = new ArrayList<>();
        e.add(b);
        e.add(String.valueOf(c));
        if(adjList.containsKey(a)) adjList.get(a).add(e);
    }
}
