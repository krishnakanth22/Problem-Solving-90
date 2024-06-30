import java.util.Scanner;

class Main {
    static int lcs(String s1, int m) {
        String s2 = new StringBuilder(s1).reverse().toString();
        
        int[][] dp = new int[m + 1][m + 1];
        
        for (int i = 0; i <= m; i++) {
            for (int j = 0; j <= m; j++) {
                if (i == 0 || j == 0) {
                    dp[i][j] = 0;
                } else if (s1.charAt(i - 1) == s2.charAt(j - 1)) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]);
                }
            }
        }
        return dp[m][m];
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String s1 = sc.nextLine();
        sc.close();
        
        int m = s1.length();
        System.out.println(lcs(s1, m));
    }
}
