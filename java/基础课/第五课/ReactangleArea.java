import java.util.Scanner;

class ReactangleArea {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("请输入矩形的长（米）：");
        int length = input.nextInt();
        System.out.print("请输入矩形的宽（米）：");
        int width = input.nextInt();

        int size = length * width;

        if(length == width) {
            System.out.println("正方形的面积是（平方米）: " + size);
        } else {
            System.out.println("长方形的面积是（平方米）: " + size);
        }

        input.close();
    }
}
