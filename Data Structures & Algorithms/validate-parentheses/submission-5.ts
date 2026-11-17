class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const alisha: string[] = [];
        const map = {
            "]": "[",
            "}": "{",
            ")": "(",
        };

        for (const c of s) {
            const last = alisha.at(-1);
            const open = map[c];
            if (open) {
                if (last === open) alisha.pop();
                else return false;
            } else alisha.push(c);
        }

        return alisha.length === 0;
    }
}
