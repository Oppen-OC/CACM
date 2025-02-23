import java.util.Scanner;

public class Main {
    private static int cont = 0; 

    public static double fun(int i, int j, double p) {
        cont++; 

        // Base cases
        if (i == 0) { return 1.0;
        } else if (j == 0) {return 0.0;
        } else if (i < 0 || j < 0) { return -1.0;
        } else { return p * fun(i - 1, j, p) + (1 - p) * fun(i, j - 1, p);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long start = System.nanoTime();

        while (true) {
            String pNLine = scanner.nextLine().trim();
            if (pNLine.isEmpty()) { 
                continue;
            }

            String[] pN = pNLine.split(" ");
            double p = Double.parseDouble(pN[0]);
            int N = Integer.parseInt(pN[1]);

            if (N == 0) {
                break;
            }

            for (int k = 0; k < N; k++) {

                String ijLine = scanner.nextLine().trim();
                if (ijLine.isEmpty()) {
                    continue;
                }

                String[] ij = ijLine.split(" ");
                int i = Integer.parseInt(ij[0]);
                int j = Integer.parseInt(ij[1]);

                cont = 0;
                double result = fun(i, j, p);

                if (result == -1.0) {
                    System.out.printf("-1.00000%n");
                } else {
                    System.out.printf("%.5f%n", result);
                }

                System.out.println(cont - 1);
            }
            long time = System.nanoTime() - start; 
            System.out.printf("%d%n", time / 1000);
            System.out.println();
        }

        scanner.close();
    }
}