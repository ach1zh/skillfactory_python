# M7-L6 Итоговое задание 5.6.1 (HW-02)
# Игра Крестики-нолики
# Чижов А.С.

import random, sys

GameBoard = [ 
    [' ','1','2','3'],
    ['1','-','-','-'],
    ['2','-','-','-'],
    ['3','-','-','-'] 
    ]

'''
#Тестовое игровое поле
GameBoard = [ 
    [' ','1','2','3'],
    ['1','m1','m2','m3'],
    ['2','m4','m5','m6'],
    ['3','m7','m8','m9'] 
    ]
'''
#Все возможные ходы
possibleTurns = [11, 12, 13, 21, 22, 23, 31, 32, 33]

#Чем играет игрок. 'x' или '0'
userToken = 'u'
compToken = 'c'

#Вывод на экран правил. Определение чем играет пользователь.
def gameInitialization():
    global userToken
    global compToken
    print("\n- По правилам игры первый ход делает игрок, ставящий крестики.")
    if(random.randint(0,1) == 0):
        userToken = '0'
        compToken = 'x'
        print(f"- Random определил, что сегодня Вы играете ноликами ({userToken})")
    else:
        userToken = 'x'
        compToken = '0'
        print(f"- Random определил, что сегодня вы играете крестиками ({userToken})")    
    print("- Ход игрока осуществляется вводом двух цифр. Первая означает ось X, вторая ось Y. Например, что бы занять центр нужно ввести '22'\n")    
    print(">>> Запуск игры \n")

# Вывод в консоль текущего игрового поля
def printGameBoard():
    global GameBoard
    print("\n>>> Обновление игрового поля:\n")
    for i in GameBoard:
        print(f"{i[0]}  {i[1]}  {i[2]}  {i[3]}")
    print("\n")

# Ход пользователя. Считывается из консоли. Принимается только корректный ввод.
def getUserTurn() -> int:
    global possibleTurns    
    global GameBoard
    errText = "\nНекорректный ввод! Ход игрока осуществляется вводом двух цифр. Первая означает ось X, вторая ось Y.\n"
    
    #Проверка: не занято ли уже выбранное игровое поле
    def fieldIsFree(field:int):
        if (GameBoard[int(str(field)[0])][int(str(field)[1])] == '-'):
            return True
        else:
            return False

    userInputIsCorrect = False
    while not userInputIsCorrect:
        try:
            userInput = int(input(">>> Сделайте свой ход\n"))
            if userInput not in possibleTurns:
                print(errText)                
            else:
                if fieldIsFree(userInput):
                    userInputIsCorrect = True                    
                    #print("\n")
                    return userInput
                else:
                    print(f"\n>>> Игровое поле {userInput} уже занято\n")                    
        except ValueError:            
            print(errText)

# Запись хода на игровое поле
def changeGameBoard(newTurn:int,Token:str):
    global GameBoard 
    global possibleTurns
    if newTurn in possibleTurns:        
        GameBoard[int(str(newTurn)[0])][int(str(newTurn)[1])] = Token
    else:
        # На всякий случай
        sys.exit("Error:  newTurn NOT in possibleTurns:")    

#Ход компьютера
def getComputerTurn() -> int:
    global GameBoard
    
    #V1 Самый простой. Поле для хода выбирается рандомно.

    #Собираем все свободные поля
    freeFields = []
    for elem in GameBoard:
        freeFields.append([index for index in range(len(elem)) if elem[index] =='-'])

    #Выбираем непустые массивы.
    not_empty_str = [index for index in range(len(freeFields)) if freeFields[index]]    
    #Из непустых выбираем случайный
    rnd_str = not_empty_str[random.randint(0,len(not_empty_str) -1)]
        
    #Выбираем случайный элемент из ненулевого массива
    not_empty_elem =  random.choice([ index for index in range(len(freeFields[rnd_str])) if freeFields[rnd_str][index] ])
    
    rnd_elem = freeFields[rnd_str][not_empty_elem]
    
    result = int(f"{rnd_str}{rnd_elem}")
    print(f">>> Компьютер ходит: {result}")
    return result
    
    #V2. Если бы было больше времени, можно было бы реализовать какой-нибудь осмысленный алгоритм ходов компьютера
    ...

# Проверка игрового поля после хода. Если есть три одинаковых элемента подряд или закончились свободные поля, то игра
# завершается победой или ничьей соответственно. 
def checkGameBoard():
    global GameBoard
    
    #Собираем значения всех горизонталей
    horizontal = []
    horizontal = list(map(lambda x: x[1:],GameBoard))[1:]

    #Собираем значения всех вертикалей
    vertical = []
    for i in range(len(GameBoard)-1):
        v = list(map(lambda x: x[i+1],GameBoard))[1:]
        vertical.append(v)        
    
    diagonal = []
    
    #Собираем значения всех диагоналей
    
    #Основная диагональ
    d1 = []
    offset = 0
    for l1 in GameBoard[1:]:
        #print(l1[1:][offset])
        d1.append(l1[1:][offset])
        offset = offset+1
    
    #Побочная диагональ
    d2 = []
    
    #Собираем список значений без указателей строк и столбцов
    GameBoard_values = []
    for l1 in GameBoard[1:]:
        GameBoard_values.append(l1[1:])
        
    offset = 0
    for l1 in GameBoard_values:
        d2.append(l1[::-1][offset])
        offset = offset+1
        
    diagonal.append(d1)
    diagonal.append(d2)

    #Проверка значений. Если есть три одинаковых подряд, то игра завершена победой одной из сторон.
    #Если свободных полей не осталось, то игра завершается в ничью.

    #Сценарий победы одной из сторон    
    def victoryScenario(winToken:str):
        printGameBoard()
        print(f">>> Игра завершается победой {winToken} \n")
        sys.exit()

    #Сценарий ничья
    def drawScenario():
        printGameBoard()
        print(f">>> Игра завершается ничьей !\n")
        sys.exit()

    #Проверка горизонталей    
    for line in horizontal:
        if all(line[0] == x and x != '-' for x in line):
            victoryScenario(line[0])
    
    #Проверка вертикалей
    for line in vertical:
        if all(line[0] == x and x != '-' for x in line):
            victoryScenario(line[0])
    
    #Проверка диагоналей
    for line in diagonal:
        if all(line[0] == x and x != '-' for x in line):
            victoryScenario(line[0])

    #Проверка сценария ничья. Не осталось свободных('-') полей для следующего хода.    
    checkEmptyFields = list(map(lambda line: any(x == '-' for x in line), GameBoard[1:]))
    
    if not any(checkEmptyFields):
        drawScenario()         

#Запуск игры
gameInitialization()
while True:
    if userToken == 'x':        
        printGameBoard()
        userTurn = getUserTurn()
        changeGameBoard(userTurn,userToken)
        checkGameBoard()
        
        computerTurn = getComputerTurn()
        changeGameBoard(computerTurn,compToken)        
        checkGameBoard()

    else:        
        computerTurn = getComputerTurn()
        changeGameBoard(computerTurn,compToken)
        checkGameBoard()
        
        printGameBoard()
        userTurn = getUserTurn()
        changeGameBoard(userTurn,userToken)
        checkGameBoard()