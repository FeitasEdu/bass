import random
 
guesses_made = 0
 
name = raw_input('小朋友你好，快来和我一起玩猜数字游戏吧.请输入输入你的英文名并按回车键开始游戏\n')
 
number = random.randint(1, 20)
print '{0}小朋友, 我现在想好了一个1到20之间的整数数字，你有三次机会来猜.前两次如果你没猜对我会告诉你你猜的数字是大了还是小了，你可以根据我的提示来继续猜，明白了吗？'.format(name)
 
while guesses_made < 3:
 
    guess = int(raw_input('请输入你猜的数字并按回车键：'))
 
    guesses_made += 1
 
    if guess < number:
        print '你猜的数字比我想的有点小，请继续猜：'
 
    if guess > number:
        print '你猜的数字比我想的有点大，请继续猜：'
 
    if guess == number:
        break
 
if guess == number:
    print '哇, 恭喜你！只用了 {1} 次机会就猜对了，难道你就是未来的数学小天才吗？小的我佩服，佩服!'.format(name, guesses_made)
else:
    print '不好意思，机会用完了. 其实我心里想的数字是 {0}'.format(number)
