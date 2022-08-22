import java.util.Scanner;

class Filip{
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        String inp = n.nextLine();
        String[] in = inp.split(" ");
        String a = new StringBuilder(in[0]).reverse().toString();
        String b = new StringBuilder(in[1]).reverse().toString();
        String ans = Integer.parseInt(a) > Integer.parseInt(b) ? a:b;
        n.close();
        System.out.println(ans);
    }
}