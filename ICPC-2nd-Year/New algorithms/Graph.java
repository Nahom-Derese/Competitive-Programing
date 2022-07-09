import java.util.ArrayList;
import java.util.HashMap;
import java.util.Queue;
import java.util.Set;
import java.util.Stack;

import javax.swing.text.StyledEditorKit.BoldAction;
import javax.xml.stream.events.StartDocument;

public class Graph {
    private boolean weighted;
    private boolean directed;
    protected Set<String> nodes;
    protected HashMap<String, ArrayList<ArrayList<String>>> adjList = new HashMap<>();

    public boolean isweighted(){
        return weighted;
    }

    public boolean isdirected(){
        return directed;
    }

    public void print_dfs(String s, String e){
        if (nodes.contains(s) && nodes.contains(e)) {
            Stack<String> ST = new Stack<>();
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.pop();
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
        
    }
    public void print_bfs(){
        Queue<String> Qu;

    }
}
