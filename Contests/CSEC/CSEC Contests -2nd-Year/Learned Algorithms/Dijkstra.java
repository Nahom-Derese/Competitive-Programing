public class Dijkstra {

    public static void main(String[] args) {
        Graph B = new Weighted_Graph();
        B.connect("a", "b", 4);
        B.connect("b", "c", 3);
        B.connect("b", "d", 1);
        B.connect("c", "d", 2);
        B.connect("c", "f", 1);
        B.connect("f", "h", 2);
        B.connect("a", "e", 5);
        B.connect("e", "f", 3);
        B.connect("d", "g", 3);
        B.connect("g", "h", 1);
        B.connect("d", "h", 4);

        B.print_dfs("a", "h");
        System.out.println("Cost ==> " + B.dijkstra("a", "c"));
    }
    
    
    
}