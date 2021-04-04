import java.util.Scanner;

class QuarterInYearSwitchCondition {
    public static void main(String args[]) {
    System.out.print("请输入一个月份：");
    int month = new Scanner(System.in).nextInt();

    int mod = month / 4;

    switch(mod) {
        case 0:
            System.out.println("第一季度");
            break;
        case 1:
            System.out.println("第二季度");
            break;
        case 2:
            System.out.println("第三季度");
            break;
        case 3:
            System.out.println("第四季度");
            break;
        default:
            System.out.println("未知月份");
            break;
        }
    }
}
