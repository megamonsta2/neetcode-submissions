class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board: string[][]): boolean {
        const rows = Array.from({ length: 9 }, () => new Set<string>());
        const columns = Array.from({ length: 9 }, () => new Set<string>());
        const subboxes = Array.from({ length: 9 }, () => new Set<string>());

        for (let y = 0; y < board.length; y++) {
            for (let x = 0; x < board[y].length; x++) {
                const item = board[y][x];
                if (item == ".") continue;

                const row = rows[y];
                const column = columns[x];
                const subbox = subboxes[Math.floor(y/3)*3  + Math.floor(x/3)];

                if (row.has(item)) return false;
                if (column.has(item)) return false;
                if (subbox.has(item)) return false;
                row.add(item);
                column.add(item);
                subbox.add(item);
            }
        }
        return true;
    }
}
