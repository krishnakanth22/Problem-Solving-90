import java.util.*;

class Fibonacci {
    
    static long[] fibonacciCache;
    
    static long fibonacci(int n) {
        if (n <= 1) {
            return n;
        }
        if (fibonacciCache != null && fibonacciCache[n] != 0) { 
            return fibonacciCache[n];
        }
        long nthNumber = fibonacci(n-1) + fibonacci(n-2); 
        fibonacciCache[n] = nthNumber; 
        return nthNumber; 
    }
    
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        fibonacciCache = new long[n + 1]; 
        
        System.out.print(fibonacci(n));
    }
}
