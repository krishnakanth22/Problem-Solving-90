import java.util.*;

class Main {
 
  static int lis(int arr[], int n) {
    int lis[] = new int[n];
    int i, j, max = 1; // Initialize max to 1
   
    for (i = 0; i < n; i++) {
      lis[i] = 1;
    }
   
    for (i = 1; i < n; i++) {
      for (j = 0; j < i; j++) {
        if (arr[i] > arr[j] && lis[i] < lis[j] + 1) {
          lis[i] = lis[j] + 1;
        }
      }
    }
    int lds[] = new int[n];
    int i, j, max = 1;
   
    for (i = 0; i < n; i++) {
      lds[i] = 1;
    }
   
    for (i = 1; i < n; i++) {
      for (j = 0; j < i; j++) {
        if (arr[i] < arr[j] && lds[i] < lds[j] + 1) {
          lds[i] = lds[j] + 1;
        }
      }
    }
    for(int i=0;i<n;i++){
        if(max<(lis[i]+lds[i]-1)){
            max = (lis[i]+lds[i]-1);
        }        
    }
 
  }
 
  public static void main(String args[]) {
    Scanner sc = new Scanner(System.in);
    int t = sc.nextInt();
   
    while (t > 0) {
      int n = sc.nextInt();
      int arr[] = new int[n];
     
      for (int i = 0; i < n; i++) {
        arr[i] = sc.nextInt();
      }
      int lisLength = lis(arr, n);
      int Length = lisLength + ldsLength - 1;
     
      System.out.println(Length);
      t=t-1;
    }
  }
}
