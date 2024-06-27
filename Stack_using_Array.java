import java.util.*;
class Main
{
  static int[] Stack1 = new int[1000];
  static int[] Stack2 = new int[1000];
  static int top1=-1,top2=-1;
  public static boolean Isempty1(){
    if((top1==-1)){
      return true;
    }
    return false;
  }
  public static boolean Isempty2(){
    if((top2==-1)){
      return true;
    }
    return false;
  }
  public static void insert1(int a){//23
      Stack1[++top1] = a;//stack1[0]=23
  }
  public static void insert2(int b){
    Stack2[++top2] = b;
  }
  public static void pop1(){
    if(Isempty1()){
      System.out.println("Stack underflow. pop from stack 1 failed");
    }
    else{
      Stack1[top1]=0;
      top1--;
    }
  }
  public static void pop2(){
    if(Isempty2()){
      System.out.println("Stack underflow. pop from stack 1 failed");
    }
    else{
      Stack2[top2]=0;
      top2--;
    }
  }
  public static void print1(){
    System.out.println("Stack 1 Elements:");
    for(int i=top1;i>=0;i--){
      System.out.print(Stack1[i]+" ");
    }
    System.out.println();
  }
  public static void print2(){
    System.out.println("Stack 2 Elements:");
    for(int i=top2;i>=0;i--){
      System.out.print(Stack2[i]+" ");
    }
    System.out.println();
  }
  public static void main(String args[])
  {
    Scanner sc = new Scanner(System.in);
    int size1 = sc.nextInt();
    while(size1!=0){
      int a = sc.nextInt();//23
      insert1(a);//23
      size1--;
    }
    int size2 = sc.nextInt();
    while(size2!=0){
      int b = sc.nextInt();
      insert2(b);
      size2--;
    }
    print1();
    print2();
    int x,y;
    x = sc.nextInt();
    while(x!=0){
      pop1();
      x--;
    }
    y = sc.nextInt();
    while(y!=0){
      pop2();
      y--;
    }
    print1();
    print2();
  }
}
