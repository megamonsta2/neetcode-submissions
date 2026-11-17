const PATTERN = /^[a-zA-Z0-9]$/;

class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isPalindrome(s: string): boolean {
        const strip: string[] = [];
        for (const c of s) {
            if (this.isAlphanumeric(c)) {
                strip.push(c.toLowerCase());
            }
        }

        const half = Math.floor(strip.length / 2);
        let first: string[], end: string[];
        if (strip.length % 2 == 0) {
            first = strip.slice(0, half);
            end = strip.slice(half);
        } else {
            first = strip.slice(0, half);
            end = strip.slice(half + 1);
        }

        let [i, j] = [0, half - 1];
        while (i < half) {
            if (first[i] !== end[j]) return false;
            i += 1;
            j -= 1;
        }
        return true;
    }

    isAlphanumeric(str: string): boolean {
        return PATTERN.test(str);
    }
}
