import java.util.ArrayList;

public class Weighted_Graph extends Graph {
    Weighted_Graph(){
        weighted = true;
    }
    public void connect(String a, String b, int c) {
        nodes.put(a, false);
        nodes.put(b, false);
        ArrayList<String> e = new ArrayList<>();
        e.add(b);
        e.add(String.valueOf(c));
        if(adjList.containsKey(a)) adjList.get(a).add(e);
        else {
            ArrayList<ArrayList<String>> r = new ArrayList<ArrayList<String>>();
            r.add(e);
            adjList.put(a, r);
        }
    }
}
