import java.util.Scanner;

class QuarterInYear {
    public static void main(String args[]) {
        System.out.print("请输入一个月份：");
        int month = new Scanner(System.in).nextInt();

        int mod = month / 4;

        if(mod == 0) {
            System.out.println("第一季度");
        } else if(mod == 1) {
            System.out.println("第二季度");
        } else if(mod == 2) {
            System.out.println("第三季度");
        } else if(mod == 3) {
            System.out.println("第四季度");
        } else {
            System.out.println("未知月份");
        }
    }
}
