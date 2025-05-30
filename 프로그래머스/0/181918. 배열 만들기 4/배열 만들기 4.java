import java.util.*;

class Solution {
    public List solution(int[] arr) {
        ArrayList<Integer> stk = new ArrayList<>();
        int i = 0;
        while(i < arr.length) {
            if(stk.size() == 0) {
                stk.add(arr[i]);
                i += 1;
                continue;
            }else if(stk.get(stk.size()-1) < arr[i]) {
                stk.add(arr[i]);
                i += 1;
            } else {
                stk.remove(stk.size()-1);
            }
        }
        return stk;
    }
}