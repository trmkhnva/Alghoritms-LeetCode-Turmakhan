class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Запоминаем цвет, который был в самом начале
        old = image[sr][sc]
        
        # Если цвет уже такой, какой нужен, то просто выходим
        if old == color:
            return image
        
        def start(r, c):
            # Проверяем внутри ли картинки и тот ли самый цвет
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == old:
                # Красим клетку
                image[r][c] = color
                
                start(r + 1, c) # вниз
                start(r - 1, c) # вверх
                start(r, c + 1) # вправо
                start(r, c - 1) # влево
        
        # Запускаем
        start(sr, sc)
        
        # Возвращаем готовую картинку
        return image