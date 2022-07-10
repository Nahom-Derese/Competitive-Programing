import java.util.ArrayList;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;

public class Graph {
    protected boolean weighted;
    protected boolean directed;
    protected HashMap<String,int[]> nodes = new HashMap<String,int[]>();
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
        HashMap<String,int[]> Nodes = (HashMap<String,int[]>)nodes.clone();
        if (Nodes.keySet().contains(s) && Nodes.keySet().contains(e)) {
            Stack<String> ST = new Stack<>();
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.pop();
                System.out.println(temp);
                if (temp.equals(e)) break;
                if (!adjList.containsKey(temp)) continue;
                for (int i = 0; i < adjList.get(temp).size(); i++) {
                    if (Nodes.get(adjList.get(temp).get(i).get(0))[0] == 0) {
                        ST.add(adjList.get(temp).get(i).get(0));
                        int[] f = {0, Nodes.get(adjList.get(temp).get(i).get(0))[1]};
                        f[0] = 1;
                        Nodes.put(adjList.get(temp).get(i).get(0),f);
                    }
                }
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
        
    }
    
    public void print_bfs(String s, String e){
        HashMap<String,int[]> Nodes = (HashMap<String,int[]>)nodes.clone();
        if (Nodes.keySet().contains(s) && Nodes.keySet().contains(e)) {
            Queue<String> ST = new LinkedList<>();
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.remove();
                System.out.println(temp);
                if (temp.equals(e)) break;
                if (!adjList.containsKey(temp)) continue;
                for (int i = 0; i < adjList.get(temp).size(); i++) {
                    if (Nodes.get(adjList.get(temp).get(i).get(0))[0] == 0) {
                        ST.add(adjList.get(temp).get(i).get(0));
                        int[] f = {0, Nodes.get(adjList.get(temp).get(i).get(0))[1]};
                        f[0] = 1;
                        Nodes.put(adjList.get(temp).get(i).get(0),f);
                    }
                }
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
    }

    public int dijkstra(String s, String e){
        HashMap<String,int[]> Nodes = (HashMap<String,int[]>)nodes.clone();
        int ans = 0;
        ArrayList<String> finall = new ArrayList<>();
        String backtrack = "";
        if (Nodes.keySet().contains(s) && Nodes.keySet().contains(e)) {
            Stack<String> ST = new Stack<>();
            Nodes.get(s)[1] = 0;
            Nodes.get(s)[0] = 1;
            ST.add(s);
            while (!ST.isEmpty()) {
                String temp = ST.pop();
                if (!temp.equals(e)) finall.add(temp + " ==> ");
                if (temp.equals(e)){
                    for (int i = 0; i < finall.size(); i++) {
                        System.out.print(finall.get(i));
                    }
                    System.out.print(temp + "\n");
                    ans = Nodes.get(temp)[1];
                    break;
                }
                if (!adjList.containsKey(temp)) {
                    int o = finall.size()-1;
                    while (!finall.get(o).equals(backtrack)){
                        finall.remove(o);
                        o--;
                    };
                    backtrack = "";
                    continue;
                }

                for (int i = 0; i < adjList.get(temp).size(); i++) {
                    if (adjList.get(temp).size() > 1 && backtrack.equals("")) backtrack = temp + " ==> ";
                    int count = ST.size();
                    if (Nodes.get(adjList.get(temp).get(i).get(0))[0] == 0) {
                        ST.add(adjList.get(temp).get(i).get(0));
                        int[] f = {0, Nodes.get(adjList.get(temp).get(i).get(0))[1]};
                        f[0] = 1;
                        if (Integer.parseInt(adjList.get(temp).get(i).get(1)) < Nodes.get(adjList.get(temp).get(i).get(0))[1]) {
                            f[1] = Nodes.get(temp)[1] + Integer.parseInt(adjList.get(temp).get(i).get(1));
                            Nodes.put(adjList.get(temp).get(i).get(0), f);
                        }
                        else Nodes.put(adjList.get(temp).get(i).get(0),f);
                    }
                    if (i == adjList.get(temp).size()-1 && count == ST.size() && backtrack.equals("")) {
                        backtrack = temp + " ==> ";
                    }
                }
            }
        } else {
            System.out.println("Argument provided is not found in the Graph");
        }
        return ans;
    }
}
