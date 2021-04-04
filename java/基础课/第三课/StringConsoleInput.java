import java.util.Scanner;

class StringConsoleInput {
    public static void main(String args[]) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("请输入一句话: ");
        String word = scanner.nextLine();
        System.out.println("你刚刚输入的是: " + word);
        scanner.close();
    }
}
