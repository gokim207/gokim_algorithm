import java.util.*;

class Solution {
    public List solution(int n) {
        ArrayList<Integer> answer = new ArrayList<>();
        while(n != 1) {
            answer.add(n);
            if(n%2 == 0) {
                n /= 2;
            }else {
                n = n*3+1;
            }
        }
        answer.add(n);
        
        return answer;
    }
}