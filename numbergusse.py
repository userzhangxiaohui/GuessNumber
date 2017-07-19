def playGame():
    """两个玩家轮流猜对方手牌数字的游戏"""
    active = 0
    Numberlist = [i for i in range(12)]
    leftnumber = Numberlist[:]
    player1 = []
    player2 = []
    player_1 = ['_*_','_*_','_*_']
    player_2 = ['_*_','_*_','_*_']
    getnum = 0
    import random
    print('Welcome to play the game')
    while True:
        msg = input('Which player start first?\n1 for player1, 2 for player2: ')
        #选择玩家1或者2开始，对active赋值作为控制变量
        if msg == '1' or '2':
            active = int(msg)
            print("Let's enjoy the game!")
            break
        else:
            print('Please choose the player!')
    player1,player2,leftnumber = getPlayersnum(player1,player2,leftnumber)
    #从牌堆中（0到11）给玩家随机发牌，每人三个数字
    while True:
        if checknum(player_1) or checknum(player_2):
            break
        #检查双方手牌是否被猜完，猜完结束游戏
        getnum,leftnumber = getnew(getnum,leftnumber)
        #猜牌玩家摸一张牌
        while True:
            judge = guess(active,player1,player_1,player2,player_2,getnum)
            #玩家猜数字，猜对返回True，否则返回False
            if checknum(player_1) or checknum(player_1):
                break
            #检查双方手牌是否被猜完，猜完结束游戏    
            if judge == 0:
                active += 1
                break
            #如果猜错，active+1，换另一个玩家猜牌，猜对继续由当前玩家猜牌
    if active%2 == 0:
        print('Congratulations! Player2 wins.')
    if active%2 == 1:
        print('Congratulations! Player1 wins.')
    #猜牌全部结束后，判断哪个玩家胜利，输出相应信息
    last = input('Enter y for a new game, or n to exit: ')
    #询问开启新一轮或是离开游戏
    if last == 'y':
        return playGame()
    else:
        print('Goodbye')
        

            
        


def getPlayersnum(player1,player2,leftnumber):
    """游戏开始给玩家发牌,从0-11牌堆中每个随机发三张，
       返回玩家手牌，桌面剩余的牌"""
    import random
    player1 = random.sample(leftnumber,3)
    player1.sort()
    for char in player1:
        leftnumber.remove(char)
    player2 = random.sample(leftnumber,3)
    player2.sort()
    for char in player2:
        leftnumber.remove(char)
    return player1,player2,leftnumber


def getnew(getnum,leftnumber):
    """从桌面剩余牌中随机抽一张，发给将要猜牌的玩家"""
    from random import choice
    getnum = choice(leftnumber)
    leftnumber.remove(getnum)
    return getnum,leftnumber

def dealnum(getnum,L1,L2):
    """猜错对方一张牌时，将getnum按顺序放在自己手牌中，
       并展示给对方看"""
    L1.append(getnum)
    L1.sort()
    x = L1.index(getnum)
    L2.insert(x,getnum)

def dealnum2(getnum,L1,L2):
    """放弃自己这一轮猜牌时，将getnum按顺序放在自己手牌
       中，不展示给对方看"""
    L1.append(getnum)
    L1.sort()
    x = L1.index(getnum)
    L2.insert(x,'_*_')

def guess(active,player1,player_1,player2,player_2,getnum):
    """猜一轮手牌，并进行相应处理，返回才手牌结果，True or False"""
    #打印空行，防止同时显示双方手牌
    for i in range(4):
        print('\n')
    #active判断哪个玩家在猜牌
    if active%2 == 1:
        #展示自己手牌和对方能显示的牌
        print("Player1's numbers are: " + str(player1) + 'and %d'%getnum)
        print("Player2's numbers are: " + str(player_2))
        print('Which number do you want to guess? Start at 0 to %d'%(len(player_2)-1))
        locate = input('Or enter e to finish: ')
        #获取要猜的牌位置，牌的大小
        if locate == 'e':
            dealnum2(getnum,player1,player_1)
            return False
        else: 
            locate = int(locate)
            num = int(input('You think the number is: '))
            #正确则展示对方被猜中的手牌，错误则结束猜牌，展示自己的getnum
            if player2[locate] == num:
                player_2[locate] = num
                print('Right!')
                return True
            else:
                dealnum(getnum,player1,player_1)
                print('Wrong!')
                return False
    if active%2 == 0:
        print("Player2's numbers are: " + str(player2) + 'and %d'%getnum)
        print("Player1's numbers are: " + str(player_1))
        locate = input('Which number do you want to guess? Or enter e to finish: ')
        if locate == 'e':
            dealnum2(getnum,player2,player_2)
            return False
        else:
            locate = int(locate)
            num = int(input('You think the number is: '))
            if player1[locate] == num:
                player_1[locate] = num
                print('Right!')
                return True
            else:
                dealnum(getnum,player2,player_2)
                print('Wrong!')
                return False

def checknum(L):
    """检查双方手牌是否被全部猜中"""
    count = 0
    for char in L:
        if isinstance(char,int):
            count += 1
    if count == len(L):
        return True
    else:
        return False

if __name__ == '__main__':
    playGame()