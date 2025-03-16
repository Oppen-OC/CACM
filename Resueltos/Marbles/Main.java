import java.util.Scanner;

public class Main {
    
    public static int gcdExtended(int a, int b, int[] xy) {
        if (b == 0) {
            xy[0] = 1;
            xy[1] = 0;
            return a;
        }
        int[] tempXY = new int[2];
        int gcd = gcdExtended(b, a % b, tempXY);
        xy[0] = tempXY[1];
        xy[1] = tempXY[0] - (a / b) * tempXY[1];
        return gcd;
    }
    
    public static Object findMinCost(int n, int c1, int n1, int c2, int n2) {
        int[] xy = new int[2];
        int gcd = gcdExtended(n1, n2, xy);
        
        if (n % gcd != 0) return "failed";
        
        int x = xy[0] * (n / gcd);
        int y = xy[1] * (n / gcd);
        int step1 = n2 / gcd;
        int step2 = n1 / gcd;
        
        int lowerBound = (int) Math.ceil(-1.0 * x / step1);
        int upperBound = (int) Math.floor(1.0 * y / step2);
        
        if (lowerBound > upperBound) return "failed";
        
        int t = c1 * n2 > c2 * n1 ? upperBound : lowerBound;
        x += t * step1;
        y -= t * step2;
        
        return new int[]{x, y};
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while (true) {
            int n = Integer.parseInt(scanner.nextLine());
            if (n == 0) break;
            
            String[] line2 = scanner.nextLine().split(" ");
            String[] line3 = scanner.nextLine().split(" ");
            
            int c1 = Integer.parseInt(line2[0]);
            int n1 = Integer.parseInt(line2[1]);
            int c2 = Integer.parseInt(line3[0]);
            int n2 = Integer.parseInt(line3[1]);
            
            Object result = findMinCost(n, c1, n1, c2, n2);
            if (result instanceof int[]) {
                int[] arr = (int[]) result;
                System.out.println(arr[0] + " " + arr[1]);
            } else {
                System.out.println(result);
            }
        }
        scanner.close();
    }
}
