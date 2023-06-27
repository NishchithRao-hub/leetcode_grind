class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> result = new ArrayList<>();
        recursion(result, "", 0, 0, n);
        return result;
    }

    private void recursion(List<String> result, String current, int open, int close, int n) {
        if (current.length() == 2 * n) {
            result.add(current);
            return;
        }
        if (open < n) {
            recursion(result, current + '(', open + 1, close, n);
        }
        if (close < open) {
            recursion(result, current + ')', open, close + 1, n);
        }
    }
}
