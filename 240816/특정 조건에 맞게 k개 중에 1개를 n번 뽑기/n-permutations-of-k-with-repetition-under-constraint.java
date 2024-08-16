import java.util.Scanner;
import java.util.ArrayList;

public class Main {
    public static int k, n;
    public static ArrayList<Integer> selected = new ArrayList<>();

    public static void findPermutations(int cnt){
        if(cnt == n){
            for(int i = 0;i<cnt;i++){
                System.out.print(selected.get(i) + " ");
            }
            System.out.println();
            return;
        }

        for(int i = 1; i <= k;i++){
            if(cnt >= 2 && i == selected.get(selected.size()-1) && i == selected.get(selected.size()-2)){
                continue;
            }
            selected.add(i);
            findPermutations(cnt+1);
            selected.remove(selected.size()-1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        k = sc.nextInt();
        n = sc.nextInt();

        findPermutations(0);
        
        
    }
}