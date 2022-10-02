import java.io.*;
import java.util.*;

class TornToPeices{
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out = new PrintWriter(new BufferedWriter(new OutputStreamWriter(System.out)));

        int n = Integer.parseInt(in.readLine());
        Map<String,HashSet<String>> AdjList = new HashMap<String, HashSet<String>>();
        for (int i = 0; i < n; i++) {
            String input = in.readLine();
            String[] splited = input.split(" ");
            HashSet<String> split = new HashSet<>();
            Collections.addAll(split, Arrays.copyOfRange(splited, 1, splited.length));
            AdjList.put(splited[0], split);
        }
        Graph g = new Graph(AdjList);
        String s[] = in.readLine().split(" ");
        List<String> res = g.bfs(s[0], s[1]);
        out.println(res.size() > 1 ? res.toString().replace("[", "").replace("]", "").replace(",", "") : "no route found");
        in.close();
        out.close();
    }
}

class Graph{

    Map<String,HashSet<String>> AdjList = new HashMap<String,HashSet<String>>();
    Deque<String> queue = new LinkedList<String>();
    Map<String,Boolean> traversed = new HashMap<>();
    
    Graph(Map<String,HashSet<String>> AdjList){
        this.AdjList = AdjList;
        Object[] set = AdjList.keySet().toArray();
        for (int i = 0; i < set.length; i++) {
            traversed.put(set[i].toString(), false);
            for (String j : AdjList.get(set[i].toString())) {
                traversed.put(j, false);
                if(AdjList.containsKey(j)){
                    AdjList.get(j).add(set[i].toString());
                }
                else{
                    HashSet<String> b = new HashSet<String>();
                    b.add(set[i].toString());
                    AdjList.put(j, b);
                }
            }
        }
    }



    List<String> bfs(String start, String end){
        traversed.put(start, true);
        queue.add(start);
        Map<String,String> backwards = new LinkedHashMap<String, String>();
        while (!queue.isEmpty()) {
            String q = queue.remove();
            
            if (q.equals(end)) 
                break;
            
            else{
                for (String us : AdjList.get(q)) {
                    if (!traversed.get(us)) {
                        queue.add(us);
                        traversed.put(us,true);
                        backwards.put(us, q);
                    }
                }
            }
        } 
        List<String> answer = new LinkedList<>();

        for (String i = end; i != null; i = backwards.get(i))
            answer.add(i);
        
        Collections.reverse(answer);
        return answer;
    }
}

