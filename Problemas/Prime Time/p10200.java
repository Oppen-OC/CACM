import java.util.*;

public class p10200 {

    // Maximum value of n^2 + n + 41 for n <= 10000
    private static final int MAX = 10000 * 10000 + 10000 + 41;

    // Sieve of Eratosthenes to precompute primes
    private static boolean[] sieve;

    static {
        sieve = new boolean[MAX + 1];
        Arrays.fill(sieve, true);
        sieve[0] = sieve[1] = false;

        for (int i = 2; i * i <= MAX; i++) {
            if (sieve[i]) {
                for (int j = i * i; j <= MAX; j += i) {
                    sieve[j] = false;
                }
            }
        }
    }

    // Function to calculate n^2 + n + 41
    private static int formula(int n) {
        return n * n + n + 41;
    }

    // Function to count primes in the interval [a, b]
    private static double countPrimes(int a, int b) {
        int primeCount = 0;
        for (int n = a; n <= b; n++) {
            int value = formula(n);
            if (sieve[value]) {
                primeCount++;
            }
        }
        return (double) primeCount / (b - a + 1) * 100;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (scanner.hasNextInt()) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            long start = System.nanoTime();

            double percentage = countPrimes(a, b);
            System.out.printf("%.2f%n", percentage);
            long time = System.nanoTime() - start; 
            System.out.printf("%d%n", time / 1000);
        }

        scanner.close();
    }
}