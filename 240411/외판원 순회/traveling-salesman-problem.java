import java.util.*;
import java.io.*;
public class Main {        
    static int n;
    static int[][] graph;
    static boolean[] visited;
    static int answer = Integer.MAX_VALUE;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        graph = new int[n][n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                graph[i][j] = Integer.parseInt(line[j]);
            }
        }

        backtracking(0, new ArrayList<>());
        System.out.println(answer);
        

    }

    public static int getCost(List<Integer> lst) {
        int result = 0;
        if (graph[0][lst.get(0)] == 0 || graph[lst.get(lst.size() - 1)][0] == 0) {
            return -1;
        }
        result += graph[0][lst.get(0)];
        result += graph[lst.get(lst.size() - 1)][0];

        for (int i = 0; i < lst.size() - 1; i++) {
            if (graph[lst.get(i)][lst.get(i + 1)] == 0) {
                return -1;
            } else {
                result += graph[lst.get(i)][lst.get(i + 1)];
            }
        }
        return result;
    }

    public static void backtracking(int depth, List<Integer> cur) {
        if (cur.size() == n - 1) {
            int cost = getCost(cur);
            if (cost != -1) {
                answer = Math.min(answer, cost);
            }
            return;
        }

        for (int i = 1; i < n; i++) {
            if (visited[i]) continue;
            cur.add(i);
            visited[i] = true;
            backtracking(depth + 1, cur);
            cur.remove(cur.size() - 1);
            visited[i] = false;
        }
    }
}