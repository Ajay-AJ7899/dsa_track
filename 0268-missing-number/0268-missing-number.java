class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int m=nums.length-1;
        for(int i=0;i<nums.length;i++){
            if(nums[i]==i){

            }
            else{
                m=i;
                break;
            }
        }
        if(m<nums[nums.length-1]){
            return m;
        }
        else{
            return nums[nums.length-1]+1;
        }

    }
}