import java.util.Scanner;
import java.util.stream.Stream;

public class QualityLife {
    public static void main(String[] args) {
        Scanner n = new Scanner(System.in);
        int a = Integer.parseInt(n.nextLine());
        double b = 0.0;
        for (int i = 0; i < a; i++) {
            double[] v = Stream.of(n.nextLine().split(" "))
                    .mapToDouble(Double::parseDouble)
                    .toArray();
            b += v[0] * v[1];
        }

        System.out.println(String.format("%.3f", b));

        n.close();
    }
}
