import random
 
guesses_made = 0
 
name = raw_input('你好，欢迎跟我一起玩猜数字游戏。请输入你的名字开始吧：\n')
 
number = random.randint(1, 20)
print '你好，{0}, 欢迎来跟我玩猜数字的游戏。我已近在1-20中选择了一个数字，你有三次机会来猜中我选的数字。每次猜测的时候，如果没猜对，我会告诉你猜测的数字是大还是小，你可以根据我的提示来进行下一次测试。明白了吗？'.format(name)
 
while guesses_made < 3:
 
    guess = int(raw_input('请输入你猜的数字：'))
 
    guesses_made += 1
 
    if guess < number:
        print '你猜的数字比我选择的有点小：'
 
    if guess > number:
        print '你猜的数字比我选择的有点大：'
 
    if guess == number:
        break
 
if guess == number:
    print '恭喜你！只用了 {1} 次机会就猜对了。'.format(name, guesses_made)
else:
    print '不好意思，机会用光了。其实我选择的数字是 {0}'.format(number)
