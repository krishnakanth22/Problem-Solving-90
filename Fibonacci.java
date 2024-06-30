import java.util.*;
class Fibonacci{
    static int fibonacci(int n){
        if (n<=1){
            return n;
        }
        return (fibonacci(n-1)+fibonacci(n-1));
    }
    
    public static void main(String[] args) {
    int n=10;
    System.out.print(fibonacci(n));
    }
}
