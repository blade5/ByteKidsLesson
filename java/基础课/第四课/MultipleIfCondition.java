class MultipleIfCondition {
   public static void main(String args[]) {
       int score = 65;

       if(score >= 80) {
           System.out.println("优秀");
       } else if((score >= 60) && (score < 80)) {
           System.out.println("良好");
       } else {
           System.out.println("再接再厉");
       }
   }
}
