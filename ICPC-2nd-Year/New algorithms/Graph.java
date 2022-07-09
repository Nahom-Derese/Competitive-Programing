import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Graph {
    protected boolean weighted;
    protected boolean directed;
    protected HashMap<String,Boolean> nodes = new HashMap<String,Boolean>();
    protected HashMap<String, ArrayList<ArrayList<String>>> adjList = new HashMap<>();

    public boolean isweighted(){
        return weighted;
    }

    public void connect(String a, String b){};
    public void connect(String a, String b, int c){};

    public boolean isdirected(){
        return directed;
    }

    public void print_dfs(String s, String e){
        if (nodes.keySet().contains(s) && nodes.keySet().contains(e)) {
            Stack<String> ST = new Stack<>();
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.pop();
                System.out.println(temp);
                if (temp == e) break;
                if (!adjList.containsKey(temp)) continue;
                for (int i = 0; i < adjList.get(temp).size(); i++) {
                    if (!nodes.get(adjList.get(temp).get(i).get(0))) {
                        ST.add(adjList.get(temp).get(i).get(0));
                        nodes.put(adjList.get(temp).get(i).get(0), true);
                    }
                }
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
        
    }
    
    public void print_bfs(String s, String e){
        if (nodes.keySet().contains(s) && nodes.keySet().contains(e)) {
            Queue<String> ST = new LinkedList<>();
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.remove();
                System.out.println(temp);
                for (int i = 0; i < adjList.get(temp).size(); i++) {
                    ST.add(adjList.get(temp).get(i).get(0));
                }
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
    }
}
