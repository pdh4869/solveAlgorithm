import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> stack = new ArrayList();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < n; i++) {
            String a[] = br.readLine().split(" ");

            switch (Integer.parseInt(a[0])) {
                case 1:
                    stack.add(Integer.parseInt(a[1]));
                    break;
                case 2:
                    if (stack.size() >= 1)
                        sb.append(stack.remove(stack.size() - 1)).append("\n");
                    else
                        sb.append(-1).append("\n");
                    break;
                case 3:
                    sb.append(stack.size()).append("\n");
                    break;
                case 4:
                    if (stack.size() == 0) {
                        sb.append(1).append("\n");
                    } else {
                        sb.append(0).append("\n");
                    }
                    break;
                case 5:
                    if (stack.size() > 0) {
                        sb.append(stack.get(stack.size() - 1)).append("\n");
                    } else {
                        sb.append(-1).append("\n");
                    }
            }  
        }
        br.close();
        System.out.println(sb);
    }
}
