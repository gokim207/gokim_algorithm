class Solution {
    public int solution(String number) {
        int answer = 0;
        for(int i = 0; i < number.length(); i++) {
            int x = number.charAt(i);
            answer += Character.getNumericValue(x);
        }
        return answer%9;
    }
}