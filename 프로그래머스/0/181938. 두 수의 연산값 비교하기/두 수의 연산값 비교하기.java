class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        answer = Math.max(2*a*b, Integer.parseInt(Integer.toString(a) + Integer.toString(b)));

    
        return answer;           
    }
    }
