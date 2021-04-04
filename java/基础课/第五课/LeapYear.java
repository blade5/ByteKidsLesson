import java.util.Scanner;

class LeapYear {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("请输入一个年份：");
        int year = scanner.nextInt();

        if (year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
            System.out.println(year + "年是闰年！");
        } else {
            System.out.println(year + "年是平年！");
        }

        scanner.close();
    }
}
