class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        answer = Integer.parseInt(Integer.toString(a) + Integer.toString(b));
        answer = Math.max(answer, Integer.parseInt(Integer.toString(b) + Integer.toString(a)));
        return answer;
    }
}