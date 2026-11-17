class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const alisha: string[] = [];
        for (const c of s) {
            const last = alisha.at(-1);
            if (c === ")") {
                if (last === "(") alisha.pop();
                else return false;
            } else if (c === "}") {
                if (last === "{") alisha.pop();
                else return false;
            } else if (c === "]") {
                if (last === "[") alisha.pop();
                else return false;
            } else alisha.push(c);
        }

        return alisha.length === 0;
    }
}
