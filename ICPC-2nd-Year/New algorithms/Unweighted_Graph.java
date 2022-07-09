import java.util.ArrayList;

public class Unweighted_Graph extends Graph{
    Unweighted_Graph(){
        weighted = false;
    }
    public void connect(String a, String b) {
        nodes.put(a, false);
        nodes.put(b, false);
        ArrayList<String> e = new ArrayList<>();
        e.add(b);
        e.add(String.valueOf(0));
        if(adjList.containsKey(a)) adjList.get(a).add(e);
        else {
            ArrayList<ArrayList<String>> r = new ArrayList<ArrayList<String>>();
            r.add(e);
            adjList.put(a, r);
        }
    }
}   
