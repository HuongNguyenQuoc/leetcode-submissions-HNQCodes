class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        hold, sold, reset = prices[0] * -1, 0, 0
        #Important: reset -> không giữ stock và cũng không bán, tức là không làm gì cả cooldown
        
        for i in range(1, len(prices)):
            price = prices[i]

            prev_hold, prev_sold, prev_reset = hold, sold, reset
            
            hold = max(prev_hold, prev_reset - price)
            # Để giữ stock trong ngày hôm nay thì sẽ có 2 case valid:
            # 1. Giữ tiếp stock của ngày hôm qua đã mua
            # 2. Nếu hôm qua không transactions gì cả thì hôm nay được phép mua

            sold = prev_hold + price
            # Nếu bán thì sold = tiền giữ stock của ngày hôm trước + giá bán hôm nay

            reset = max(prev_reset, prev_sold)
            '''
            Nếu ngày hôm nay muốn không làm gì
            thì phải tiếp tục reset từ hôm qua or số tiền hôm qua đã bán được
            -> Tức là nếu bán thì buộc nay phải nghỉ hoặc tiếp tục nghỉ tiếp của ngày hôm qua
            '''
        
        return max(sold, reset)


