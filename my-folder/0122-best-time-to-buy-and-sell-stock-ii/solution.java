class Solution {
    public int maxProfit(int[] prices) {
        int buy_or_not = -Integer.MAX_VALUE;
        int sell_or_not = 0;
        for ( int stock_price : prices){
            int prev_buy_or_not = buy_or_not;
            int prev_sell_or_not = sell_or_not;

            // case whether to wait or buy stock at todays price
            buy_or_not = Math.max(prev_buy_or_not, prev_sell_or_not - stock_price );

            // case whether to wait or sell stock at todays price
            sell_or_not = Math.max(prev_sell_or_not, prev_buy_or_not + stock_price);

        }
        //Profit
        return sell_or_not;
    }
}
