import java.util.*;

public class Main {
    public static int n, m;
    public static ArrayList<Integer> combination = new ArrayList<>();

    // 방문한 원소들을 출력해줍니다.
    public static void printCombination() {
        for(int i = 0; i < combination.size(); i++)
            System.out.print(combination.get(i) + " ");
        System.out.println();
    }

    public static void findCombination(int cur, int cnt){
        if(cur == n+1){
            if(cnt == m)
                printCombination();
            return;
        }

        combination.add(cur);
        findCombination(cur+1, cnt+1);
        combination.remove(combination.size()-1);

        findCombination(cur+1, cnt);
    }


    public static void main(String[] args) {        
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        m = sc.nextInt();
        
        findCombination(1, 0);
    }
}