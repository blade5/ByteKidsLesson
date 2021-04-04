import java.util.Scanner;

class OddOrEven {
    public static void main(String[] args) {
        System.out.print("请输入一个整数：");
        int n = new Scanner(System.in).nextInt();

        if(n % 2 == 0) {
            System.out.println("该数是偶数");
        } else {
            System.out.println("该数是奇数");
        }
    }
}
