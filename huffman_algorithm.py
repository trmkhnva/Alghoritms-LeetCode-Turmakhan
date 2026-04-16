import heapq
import time
from collections import Counter

# Элемент нашего будущего дерева
class Node:
    def __init__(self, bukva, chastota):
        self.bukva = bukva      # Сама буква
        self.chastota = chastota  # Как часто встречается
        self.left = None
        self.right = None
    
    # как сравнивать буквы 
    def __lt__(self, other):
        return self.chastota < other.chastota

# Функция для кодирования 
def kodirovanie(text):
    if not text:
        return "", {}
    
    # Считаем, сколько раз каждая буква попалась в тексте
    povtory = Counter(text)
    
    # Создаем список из всех букв (очередь)
    spisok_uzlov = [Node(b, c) for b, c in povtory.items()]
    heapq.heapify(spisok_uzlov)
    
    # Собираем дерево: берем по две самые редкие буквы и объединяем
    while len(spisok_uzlov) > 1:
        levo = heapq.heappop(spisok_uzlov)
        pravo = heapq.heappop(spisok_uzlov)
        
        # Создаем общую ветку
        obshiy_uzel = Node(None, levo.chastota + pravo.chastota)
        obshiy_uzel.left = levo
        obshiy_uzel.right = pravo
        
        heapq.heappush(spisok_uzlov, obshiy_uzel)
    
    # Теперь проходим по дереву и раздаем каждой букве код
    tablica_kodov = {}
    def sbor_kodov(uzel, tekushiy_kod):
        if uzel.bukva is not None:
            tablica_kodov[uzel.bukva] = tekushiy_kod
            return
        sbor_kodov(uzel.left, tekushiy_kod + "0")
        sbor_kodov(uzel.right, tekushiy_kod + "1")
    
    koren = spisok_uzlov[0]
    sbor_kodov(koren, "")
    
    # Собираем сжатую строку из нулей и единиц
    szhataya_stroka = "".join([tablica_kodov[simvol] for simvol in text])
    return szhataya_stroka, tablica_kodov

#Функция для декодирования 
def dekodirovanie(binarnaya_stroka, tablica):
    if not binarnaya_stroka:
        return ""
    
    # Переворачиваем таблицу, чтобы искать букву по коду
    obratnaya_tablica = {v: k for k, v in tablica.items()}
    
    itog = ""
    kusok_koda = ""
    for bit in binarnaya_stroka:
        kusok_koda += bit
        if kusok_koda in obratnaya_tablica:
            itog += obratnaya_tablica[kusok_koda]
            kusok_koda = ""
            
    return itog

if __name__ == "__main__":
    proba_text = "Пример текста для лабораторной работы" * 10
    
    print("Проверка")
    
    # Засекаем время и делаем 5 кругов
    start = time.time()
    for i in range(5):
        szhatie, kody = kodirovanie(proba_text)
        original = dekodirovanie(szhatie, kody)
        assert proba_text == original
    
    finis = time.time()
    
    print("Результат: текст совпадает")
    print(f"Среднее время (из 5 попыток): {(finis - start) / 5:.6f} сек")