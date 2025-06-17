import java.util.HashMap;
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        int[] nums = {6, 6, 6, 7, 7};
        HashMap<Integer, Integer> elements = new HashMap<Integer, Integer>();

        for(int i=0; i<nums.length; i++){
            if(elements.get(nums[i]) == null){
                elements.put(nums[i], 1);
            }else {
                elements.put(nums[i], elements.get(nums[i]) + 1);
            }
        };
        Integer[] majorityElement = {null};
        int[] majorityElementCount = {0};

        elements.forEach((key, value) ->{
            if(value > majorityElementCount[0]){
                majorityElementCount[0] = value;
                majorityElement[0] = key;
            }
        });

        System.out.println(majorityElement[0]);


    }
}