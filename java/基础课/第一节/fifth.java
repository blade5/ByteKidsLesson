import java.util.Scanner;

class fifth {
    public static double circumArea(double radius) {
        return Math.PI * Math.pow(radius, 2);
    }
    
    public static double circumference(double radius) {
        return 2 * Math.PI * radius;
    }

    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("请输入圆的半径（单位：米）： ");
        double radius = scanner.nextDouble();
        
        System.out.printf("周长：%.3f 米\n", circumArea(radius));
        System.out.printf("面积：%.3f 平方米\n", circumference(radius));
    }

}
