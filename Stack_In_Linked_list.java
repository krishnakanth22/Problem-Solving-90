import java.util.*;
class Main
{
  static Node head = null;
  static class Node{
    int data;
    Node next;
    Node(int val){//20
      data = val;//20
      next = null;
    }
  }
  public static void insert(int val){
    Node newNode = new Node(val);//20
    if(head==null){//empty
      //newNode = head;
      head = newNode;
    }
    else{
      newNode.next = head;
      head = newNode;
    }
  }
  public static void display(){
    Node temp = head;
    while(temp!=null){
      System.out.print(temp.data+" ");
      temp = temp.next;
    }
  }
  public static void main(String args[])
  {
    Main ob = new Main();
    Scanner sc = new Scanner(System.in);
    int a = 1;
    while(a!=-1){
      a = sc.nextInt();
      if(a==-1) break;
      ob.insert(a);
    }
    ob.display();
  }
}
