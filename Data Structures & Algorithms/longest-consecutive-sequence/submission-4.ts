class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        if (nums.length === 0) return 0;
        if (nums.length === 1) return 1;
        
        nums.sort((a, b) => a - b);
        let current = nums[0];
        let currentLongest = 1;
        let longest = 1;

        for (const n of nums) {
            if (n == current) {
                continue;
            } else if (n === current + 1) {
                current = n;
                currentLongest += 1;
                if (currentLongest > longest) longest = currentLongest;
            } else {
                current = n;
                currentLongest = 1;
            }
        }

        return longest;
    }
}
