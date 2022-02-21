// 169. Majority Element

class Solution {
public:
    int majorityElement(vector<int>& nums) {
        
        unordered_map<int, int> hash_map;
        int max_elem = 0;
        int max_count = 0;
        
        for(int i=0;i<nums.size();i++){
            
            hash_map[nums[i]]+=1;
            
            if(max_count<hash_map[nums[i]]){
                
                max_elem = nums[i];
                max_count = hash_map[nums[i]];
                
            }
        }
        
        return max_elem;
    }
    
};
