class Solution {
    /**
     * @param {number[]} nums
     * @return {number}
     */
    longestConsecutive(nums: number[]): number {
        nums.sort((a, b) => a - b);
        let currentLongest = 0;
        let longest = 0;
        let current: number;

        for (const n of nums) {
            if (current === undefined) {
                current = n;
                currentLongest += 1;
                longest = currentLongest;
                continue;
            }

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
