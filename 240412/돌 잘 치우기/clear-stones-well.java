import java.util.*;

public class Main {
    public static final int DIR_NUM = 4;
    public static final int MAX_N = 100;

    public static int n, k, m;
    public static int[][] arr = new int[MAX_N][MAX_N];
    
    public static int answer;

    public static ArrayList<int[]> stonePos = new ArrayList<>();
    public static ArrayList<int[]> selected = new ArrayList<>();
    public static ArrayList<int[]> sPos = new ArrayList<>();

    // bfs함수를 위한 변수
    public static Queue<int[]> q = new LinkedList<>();
    public static boolean[][] visited = new boolean[MAX_N][MAX_N];

    public static boolean inRange(int x, int y){
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    public static void BFS(){
        while (!q.isEmpty()){
            int[] curPos = q.poll();
            int x = curPos[0], y = curPos[1];

            int[] dxs = new int[]{1,-1,0,0};
            int[] dys = new int[]{0,0,1,-1};

            for(int dir=0;dir<DIR_NUM;dir++){
                int nx = x +dxs[dir], ny = y+dys[dir];
                if (inRange(nx, ny) && !visited[nx][ny]  && arr[nx][ny] == 0){
                    visited[nx][ny] = true;
                    q.add(new int[]{nx, ny});
                }
            }
        }
    }



    public static int calc(){
        for(int i=0;i<m;i++){
            int x = selected.get(i)[0];
            int y = selected.get(i)[1];
            arr[x][y] = 0;
        }

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                visited[i][j] = false;
            }
        }

        for(int i=0;i<k;i++){
            q.add(sPos.get(i));
            visited[sPos.get(i)[0]][sPos.get(i)[1]] = true;
        }

        BFS();

        int cnt = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(visited[i][j]) cnt++;
            }
        }

        for(int i=0;i<m;i++){
            int x = selected.get(i)[0];
            int y = selected.get(i)[1];
            arr[x][y] = 1;
        }  

        return cnt;
        
    }


    public static void findMax(int depth, int cnt){
        if((int)stonePos.size() == depth){
            if(cnt == m){
                answer = Math.max(answer, calc());
            }
            return;
        }

        selected.add(stonePos.get(depth));
        findMax(depth+1, cnt+1);
        selected.remove(selected.size()-1);

        findMax(depth+1, cnt);
    }

    public static void main(String[] args) {
        // 여기에 코드를 작성해주세요.
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();
        m = sc.nextInt();

        for(int i = 0;i < n; i++){
            for(int j =0;j <n;j++){
                arr[i][j] = sc.nextInt();
                if(arr[i][j] == 1){
                    stonePos.add(new int[]{i,j});
                }
            }
        }

        for(int i =0;i<k;i++){
            int r = sc.nextInt();
            int c = sc.nextInt();
            r--;
            c--;
            sPos.add(new int[]{r, c});
        }

        findMax(0,0);

        System.out.println(answer);

    }
}