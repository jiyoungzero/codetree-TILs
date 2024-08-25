import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 여기에 코드를 작성해주세요.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int[] arr = new int[26];
        Arrays.fill(arr, -1); 
        
        int ans = 0;
        int start = 0;

        for (int i=0; i<str.length(); i++) {
            int n = str.charAt(i) - 'a';
            if (arr[n] >= start) {
                start = arr[n];
            }
            arr[n] = i;
            ans = Math.max(ans, i - start);
        }

        System.out.println(ans); 
    }
}