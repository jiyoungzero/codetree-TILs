import java.util.*;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] arr = new int[n];
        int[] dp = new int[n];
        int answer = 0;

        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
            dp[i] = 1;
        } 

        for(int i = 0; i< n;i++){
            for(int j = 0;j < i;j++){
                if(arr[i] > arr[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    answer = Math.max(answer, dp[i]);
                }
            }
        }

        System.out.println(answer);

    }
}