import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Long res = 1L, sum = 0L;
        for(int i = 1; i <= n; i++)
        {
            res *= i;
            sum += res;
        }
        System.out.println(sum);
    }
}
