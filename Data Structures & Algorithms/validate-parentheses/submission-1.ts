class Solution {
    /**
     * @param {string} s
     * @return {boolean}
     */
    isValid(s: string): boolean {
        const alisha: string[] = [];
        for (const c of s) {
            if (c === "(" || c === "{" || c === "[") alisha.push(c);
            else if (c === ")") {
                if (alisha.at(-1) === "(") alisha.pop();
                else return false;
            } else if (c === "}") {
                if (alisha.at(-1) === "{") alisha.pop();
                else return false;
            } else if (c === "]") {
                if (alisha.at(-1) === "[") alisha.pop();
                else return false;
            }
        }

        const last = alisha.at(-1);
        if (last === "(" || last === "{" || last === "[") return false;
        return true;
    }
}
