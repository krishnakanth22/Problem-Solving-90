import java.util.*;
class Main
{
  static int lis(int arr[], int n){
    int i,j,max=0;
    int list[]=new int[n];
    for(i=0;i<n;i++){
      list[i]=1;
    }
    for (i=1;i<n;i++){
      for (j=0;j<i;j++){
        if(arr[i]>arr[j] && list[i] < list[j]+1){
          list[i]=list[j]+1;
        }
      }
    }
    for (i=0;i<n;i++){
      if(max<list[i]){
        max=list[i];
      }
    }
    return max;
  } 
  public static void main(String args[])
  {
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int arr[]=new int[n];
    for(int i=0;i<n;i++){
      arr[i]=sc.nextInt();
    }
    System.out.print(lis(arr,n));
  }
}
