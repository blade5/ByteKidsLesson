class LogicOperations {
    public static void main(String args[]) {
        int x = 39;

        boolean result = (x > 30) && (x < 50);
        System.out.println("" + x + "在30到50之间: " + result);

        boolean result1 = (x % 3 == 0) || (x % 2 == 0);
        System.out.println("" + x + "是3倍数或者是2的倍数: " + result1);

        boolean result2 = !(x > 10);
        System.out.println("" + x + "不大于10: " + result2); 
    }
}
