import java.util.Scanner;

class NumberConsoleInput {
   public static void main(String args[]) {
       Scanner scanner = new Scanner(System.in);
       System.out.print("请输入一个整数: ");
       int number = scanner.nextInt();
       int square = number * number;
       System.out.println("" + number + "的平方是：" + square);
       scanner.close();
   }
}
