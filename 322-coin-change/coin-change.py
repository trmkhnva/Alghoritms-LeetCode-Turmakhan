class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Заполняем таблицу значениями, которые больше возможной суммы
        min_coins = [amount + 1] * (amount + 1)
        
        # Для суммы 0 нужно 0 монет
        min_coins[0] = 0
        
        # Перебираем все суммы от 1 до нужной нам
        for i in range(1, amount + 1):
            # Пробуем каждую монету
            for c in coins:
                if i - c >= 0:
                    min_coins[i] = min(min_coins[i], 1 + min_coins[i - c])
        
        # Если значение не изменилось, значит сумму собрать нельзя
        if min_coins[amount] > amount:
            return -1
        else:
            return min_coins[amount]