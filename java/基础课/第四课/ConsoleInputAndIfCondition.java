import java.util.Scanner;

class ConsoleInputAndIfCondition {
    public static void main(String args[]) {
       Scanner scanner = new Scanner(System.in);

       System.out.print("请输入你的考试分数：");
       int score = scanner.nextInt();

       if(score >= 80) {
           System.out.println("优秀");
       } else if((score >= 60) && (score < 80)) {
           System.out.println("良好");
       } else {
           System.out.println("再接再厉");
       }
    }
}
