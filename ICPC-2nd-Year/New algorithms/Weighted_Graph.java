import java.util.ArrayList;

public class Weighted_Graph extends Graph {
    Weighted_Graph(){
        weighted = true;
    }
    public void connect(String a, String b, int c) {
        int[] f = {0,Integer.MAX_VALUE};
        nodes.put(a, f);
        nodes.put(b, f);
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
