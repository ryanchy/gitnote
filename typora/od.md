单词接龙
k = int(input())  # 起始单词索引
n = int(input())  # 单词个数
ls = []
output = []
for i in range(n):
    ls.append(input())
output.append(ls[k])
ls.remove(ls[k])

while ls:
    temp = []  # 所有首字母和前一个字符尾字母相同的字符
    for c in ls:
        if output[-1][-1] == c[0]:
            temp.append(c)
    if temp:
        temp = sorted(temp, key=lambda x: (-len(x), x))  # 长度降序（取最长），字典序升序（取最小）
        output.append(temp[0])
        ls.remove(temp[0])
    else:
        break

print("".join(output))

补种杨树
"""
# “01001010”
5
1 3 4 6 8
1
"""
3
n = int(input())
m = int(input())
death = list(map(int, input().split()))
k = int(input())  # 补种数量

nums = [1 for _ in range(n)]  # 存活的都是1
for i in death:
    nums[i-1] = 0  # 未存活的都是0

left, right, res = 0, 0, 0 # left代表填入新树后的连续树的第一个
for right in range(n):
    k -= 1-nums[right] # 遍历时,只要num[right]为0,就补一棵树,k-=1,有树时k-=0不变
    while k <0: # 当补种的白杨k不足时要拔掉前面的补充后面的
        k += 1-nums[left] # 从left=0开始往后找,遇到nums[left]==0的地方,k可以补充一颗填到后面
        left += 1 # 此刻left只能从拔掉树的这个位置的后一个开始算了
    res = max(res, right-left+1) # 每次把一颗树拔到后面都要比较前后哪个最长,最后保留的肯定是最长的
print(res)

数字涂色
"""
3
2 4 6
4
2 3 4 9
"""
n = int(input())
ls = list(map(int, input().split()))

nums = []
while len(ls) > 0:
    min_n = min(ls)
    temp = []
    i = 0
    while i < len(ls):
        if ls[i] % min_n == 0:
            temp.append(ls[i])
            ls.remove(ls[i])
            continue
        else:
            i += 1
    nums.append(temp)
    # temp.clear()不需要，因为第一个最小值的倍数数组循环结束后，临时列表temp会返回row23 重新赋值为空

print(len(nums))


数格子
"""题目
给定一个n*n二维数组，随机分布‘0’和‘1’
输入一个坐标点，输出坐标周围一圈‘1’的个数
用例：
4
1 1 1 0
1 1 1 1
1 0 1 1
1 1 1 1
0 3
"""

nn = int(input()) # 注意变量的作用域
input_ls = []
for i in range(nn):
    nums = list(map(int, input().split()))
    input_ls.append(nums)
x, y = list(map(int, input().split()))

ls = []
for j in input_ls[::-1]:
    ls.append(j)
# 目标点位
# 获取目标点位上下左右所有合法的点位
all_zb = []
for m in range(x-1, x+2):
    if 0 <= m <= len(ls[0]) -1:
        for n in range(y-1, y+2):
            if 0 <= n <= len(ls) - 1:
                all_zb.append((m, n))  # 二维数组
# 去除本身
all_zb.remove((x, y))
# 遍历点位,累加
count = 0
for e in all_zb:
    count += ls[e[1]][e[0]]  # 值就是1
print(count)

判断字符串子序列
"""
abc
abcaybec
"""
# 找最后一个子串的首字母下标；找不到子串就输出-1
# 直接倒序输入的字符串，在长字符串中找第一个子串，就是原字符串的最后一个子串；下标数就是len(列表)-(i+1)
target = list(input())
source = list(input())
n = len(source)

target = target[::-1]
source = source[::-1]
ls = []
ls1 = []  # 反转后、子串在字符串列表的下标
for i in target:
    for j in range(len(source)):
        if source[j] == i:
            ls.append(i)
            ls1.append(j)
            break
        else:
            continue
if ls == target:
    print(n - (ls1[-1] + 1))
else:
    print("-1")

太阳能板最大面积
"""
输入一排支柱的高度，间隔单位1，选择其中2根支柱安装太阳能板，使其面积最大
安装面积受限最短支柱
用例：
输入 10,9,8,7,6,5,4,3,2,1
输出 25
"""
# 下标数决定了面板宽度，短的支柱高度决定面板长度

ls = list(map(int, input().split(",")))  # 不按逗号分割就是一个元素，不能反转
ls.sort(reverse=True)
ls1 = ls[1:]
# 选取第一个作为标杆，即列表的最大值 ls1[0] ,面积取决于最短的支柱，所以ls1[0]不做计算

max_s = []  # 面积列表
for i in range(len(ls1)):
    s = int(ls1[i]) * int(i+1)
    max_s.append(s)
max_s = set(max_s)  # 去重返回无序集合
max_s1 = sorted(max_s, reverse=True)
print(max_s1[0])

寻找相同子串
"""
t是长字符串，p是子串
t的下标从1开始，输入子串p的第一个字符下标
找不到就输出no
多个子串，输出第一个字符下标最小的小标数
"""
"""用例
AVERDXIVYERDIAN
RDXI
"""
t = input()
p = input()
ls = []
if p in t:
    ls = t.split(p)
    print(len(ls[0])+1)
else:
    print("No")

\合法三角形个数
nums = list(map(int, input().split()))
nums = sorted(nums)
lens = len(nums)
count = 0
for i in range(lens-2):
    for j in range(i+1, lens-1):
        for k in range(j+1, lens):
            a = nums[i]
            b = nums[j]
            c = nums[k]
            if a + b > c:
                count += 1
print(count)

查找众数及中位数
"""
输入描述:
输入一个一维整型数组，数组大小取值范围 0<N<1000，数组中每个元素取值范围 0<E<1000
输出描述:
输出众数组成的新数组的中位数
"""
# 中位数：取余=1，就是众数本身；取余=0，就是众数/2
# 找到多个众数，count个数，然后组成新的列表，求中位数

ls_shu = []  # 所有的数
ls_num = []  # 众数
ls = input().split()  # 输入的数组
# ls = [10,11,21,19,21,17,21,16,21,18,15]，输出 21
for k in ls:
    if k not in ls_shu:
        ls_shu.append(k)
    else:
        ls_num.append(k)
        if ls_num.count(k) == 1:  # 众数列表里少一个值，需要加1
            ls_num.append(k)
ls_num.sort()

mid_num = 0  # 中位数
if len(ls_num) % 2 == 1:  # 奇数个众数列表
    for i in range(len(ls_num)):
        mid_num = ls_num[len(ls_num) // 2 + 1]
else:
    for i in range(len(ls_num)):
        mid_num = (int(ls_num[len(ls_num) // 2]) + int(ls_num[len(ls_num) // 2 + 1])) / 2
print(int(mid_num))

求解连续数列
# 连续数列公式s = (k[0] + k[n]) * n / 2
# k[0] = s * 2 / n - k[n]
s, n = map(int, input().split())  # s是数列之和，n是数列长度
ls = []
k = (s * 2 / n - (n - 1)) / 2  # x就是k[0]
for i in range(n):
    # 数列的k是一个连续递增的整数，所以只要k+i就可以，不要惯性思维写成k+=i !!!
    ls.append(int(k+i))
for k in ls:
    if k <= 0:
        print(-1)
        break
    else:
        print(*ls)

组成最大数
# 思路一：先找出最短字符串长度，然后切片其他字符串，比较这个长度的每个字符串大小;降序排列，然后子串按这个顺序拼接
# 思路二：先排序，因为计算机会按照ASCII码排序，唯一的争议点在于若遇到前几位数字相同的字符串，需要判断下
ls = input().split(",")
len_min = []
n = 0
ls2 = []
for a in ls:
    len_min.append(len(a))
    n = min(len_min)  # 找出输入列表最短字符长度n
for a in ls:
    ls2.append(a[:n])
ls2.sort(reverse=True)  # 切片n长度ls2=[999,458,414,101]

ls3 = []
for b in ls2:
    for a in ls:  # 嵌套循环：在ls2中遍历每个b，找到原列表ls中每个对应的a
        if b == a[:n]:
            ls3.append(a)
            ls.remove(a)
print("".join(ls3))

# 欠考虑前n位数相等的情况

字符串分割
k = int(input())
head, tail = input().split('-', 1)  # 必须加1,表示从第一个分隔符开始，把字符串分割1次，即分割为两个子串
tail = tail.replace('-', '')  # replace()
ls = ""
for a in range(0, len(tail), k):  # 获取以k长度的子串格式： for i in range(start,end,k)
    line = tail[a:a+k]  # 赋值分割后的子串
    upper = 0
    lower = 0
    for c in line:
        if c.isupper():
            upper += 1
        else:
            lower += 1
    if upper == lower:
        ls += line
    elif upper > lower:
        ls += line.upper()
    else:
        ls += line.lower()

new_ls = []
for b in range(0, len(ls), k):
    new_ls.append(ls[b:b+k])  # 重新装进列表，之前是字符串

print(f"{head}-{'-'.join(new_ls)}")

59 考勤
# 思路：三个条件并行，满足一个都返回False
n = int(input())
ls = []
ls_input = []
for i in range(n):
    ls_input = input().split()
    ls.append(ls_input)

result = []
for ls_input in ls:
    result_3 = []  # 记录三种情况下有无不满足
    if ls_input.count('absent') > 1:
        result_3.append('False')

    for j in range(len(ls_input)):
        if len(ls_input) > 1:
            if ls_input[j] and ls_input[j - 1] == 'late' or 'leaveearly':
                result_3.append('False')

        else:
            continue
        if ls_input[j] == 'absent' or 'late' or 'leaveearly':
            c = 0
            ls1 = ls_input[j + 1: j + 7]  # 如果发现了三个情况之一，那么从当前字符开始往后6个字符数，是否超过3次
            c += ls1.count('absent')
            c += ls1.count('late')
            c += ls1.count('leaveearly')
            if c >= 3:
                result_3.append('False')
    if "False" in result_3:
        result.append('False')
    else: result.append("True")
print(*result)

60消消乐
# 从输入的字符串中逐一拿出字符，放进新的列表
# 将字符与新列表的最后一个字符比较，如果相同就删掉新列表的最后一个字符，如果不同，就增加

# 方法一：
ls = input()  # 或者直接输入转成列表ls=list(str(input()))
              # 绝对不能input().split()，这样会把输入的字符串分割成一个整体
new_ls = []
for k in ls:
    if len(new_ls) > 0:
        if k == new_ls[-1]:
            new_ls.pop()
        else:
            new_ls.append(k)
    else:
        new_ls.append(k)
print(len(new_ls))

# 方法二：
ls = input()
new_ls = []
for i in ls:
    if new_ls and new_ls[-1] == i:
        new_ls.pop()
    else:
        new_ls.append(i)
print(len(new_ls))

49 货车装快递
# 快递货车最多装多少数量的快递，你看重量、不看体积，输出最多装的快递数量
# 思路：升序排列，求前几项的和、count数量

ls = list(map(int, input().split(",")))
n = int(input())  # 货车载重量
ls.sort()
num = []  # 可以装进去的快递
total = 0  # 装进货车的快递总重量
for k in ls:
    if (total+k) <= n:  # 应该"<="
        total += k
        num.append(k)
    else:
        break
print(len(num))

38 拼接URL
# 思路：前缀部分如果以“/”结尾，则直接装入列表；否则，加上”/“，装进列表
# 后缀部分，如果开头没有“/”，直接装进列表，否则切掉再装入
# 最后合并.join
a, b = input().split(",")
ls = []
if a == b == "":
    print("/")
if a[-1] == "/":
    ls.append(a)
else:
    a += "/"  # 保证前缀有/
    ls.append(a)
if b[0] == "/":
    # b.replace(b[0],"")
    ls.append(b[1:])  # 不要总是想着删掉“/”，切片放入想要的部分也可以啊！！
else:
    ls.append(b)
new_ls = "".join(ls)
print(new_ls)

快递车
ls = list(map(int, input().split(",")))
n = int(input())  # 货车载重量
ls.sort()
num = []  # 可以装进去的快递
total = 0  # 装进货车的快递总重量
for k in ls:
    if (total+k) <= n:  # 应该"<="
        total += k
        num.append(k)
    else:
        break
print(len(num))

第K个排列
# 排列 15分钟完成的itertools版本只能算到9个提高效率只运算到前k个数23分钟完成
import time,itertools

time_st = time.time()
ip = "9 4".split()
n = int(ip[0])
k = int(ip[1])
n_list = [f"{i}" for i in range(1,n+1)]
zuhe_list = list(itertools.permutations(n_list,n))

zhhe_int_list = []
for i in zuhe_list:
    zhhe_int_list.append("".join(i))
zhhe_int_list.sort()
for i in range(k):
    print(zhhe_int_list[i])
print(time.time()-time_st)


#篮球比赛25分钟
#输入10个成员的战斗力，选出战斗力总和差值最小的两个组合
# 输入10 9 8 7 6 5 4 3 2 1
# 不需要考虑异常输入
# 输出：最小战斗力差值，如：1
ip_list = ["10 9 8 7 6 5 4 3 2 1","1 1 1 1 1 3 3 3 3 3 "]

# 输出分组的所有可能性
dw1_list = []
def dfx(dw1,dw2):
    if len(dw1) < 5:
        for i in range(len(dw2)):
            dfx(dw1+[dw2[i]],dw2[:i]+dw2[i+1:])
    else:
        dw1.sort()
        if not dw1 in dw1_list:
            dw1_list.append(dw1)

# 输入
for ip in ip_list:
    dfx([],list(map(int,ip.split())))
    yiban = sum(list(map(int,ip.split())))/2
    chazhi = 0.0
    min_zhi = yiban
    zuixiao = 0
    zuhe = None
    for i in dw1_list:
        if (sum(i)- yiban)**2 < min_zhi:
            min_zhi = (sum(i)- yiban)**2
            zuixiao =  sum(i)
            zuhe = i
    print(zuixiao)



#编写对象
class Bianjiqi():
    def __int__(self, text):
        self.text = text
        self.zhizheng = 0
        self.textlen = len(self.text)

    def forward(self,order):
        order_list = order.split()
        if int(len(order[1])) + self.zhizheng > self.textlen:
            self.zhizheng = self.textlen + 1
        else:
            self.zhizheng += int(len(order[1]))
    def backward(self,order):
        order_list = order.split()
        if self.zhizheng - int(len(order[1])) < 0:
            self.zhizheng = 0
        else:
            self.zhizheng -= int(len(order[1]))
    def search_forward(self,order):
        order_list = order.split()
        if self.zhizheng != self.textlen +1:
            for j in range(self.zhizheng,self.textlen):
                if order_list[1] == self.text[j:j+len(order_list)]:
                    self.zhizheng -= j
                break
    def search_backward(self,order):
        if self.zhizheng != 0:
            order_list = order.split()
            for j in range(self.zhizheng-1,0,-1):
                if order_list[1] == self.text[j:j+len(order_list)]:
                    self.zhizheng += j
                break
    def delete(self,order):
        order_list = order.split()
        len_insert = len(order_list[1])
        self.text = self.text[:self.zhizheng] + self.text[self.zhizheng + len_insert:]
        self.textlen = len(self.text)

    def insert(self,order):
        order_list = order.split()
        len_insert = len(order_list[1])
        self.text = self.text[:self.zhizheng] + order_list[1] +self.text[self.zhizheng:]
        self.textlen = len(self.text)
        if self.zhizheng + len_insert > self.textlen:
            self.zhizheng = self.textlen +1
        else:
            self.zhizheng += len_insert
    def replace(self,order):
        order_list = order.split()
        len_insert = len(order_list[1])
        self.text = self.text[:self.zhizheng] + order_list[1] + self.text[self.zhizheng + len_insert:]
        self.textlen = len(self.text)
        if self.zhizheng + len_insert > self.textlen:
            self.zhizheng = self.textlen + 1
        else:
            self.zhizheng += len_insert
    def print(self):
        print(self.text)
#输入
for ip in input_list:
    mingling_len = int(ip[0])
    wenbeng = ip[1]
    mingling_list = ip[2:]
    bjq = Bianjiqi()
    bjq.__int__(wenbeng)
    for i in mingling_list:
        if i.split()[0] == "FORWARD":
            bjq.forward(i)
        elif i.split()[0] == "BACKWARD":
            bjq.backward(i)
        elif i.split()[0] == "SEARCH-FORWARD":
            bjq.search_forward(i)
        elif i.split()[0] == "SEARCH-BACKWARD":
            bjq.search_backward(i)
        elif i.split()[0] == "INSERT":
            bjq.insert(i)
        elif i.split()[0] == "REPLACE":
            bjq.replace(i)
        elif i.split()[0] == "DELETE":
            bjq.delete(i)
    bjq.print()

#实例对象

#输出



# 示例1：输入
# 1
# ello
# INSERT h
# 输出：
# Hello 说明：在文本开头插入
# 示例2：
# 输入
# 2
# hllo
# FORWARD 1
# INSERT e
# 输出
# hello 说明：在文本的第一个位置插入
# 示例3：
# 输入
# 2
# hell
# FORWARD 1000
# INSERT o
# 输出
# hello 说明：在文本的结尾插入
# 示例4
# 输入
# 1
# hello
# REPLACE HELLO
# 输出
# HELLO说明：替换
# 示例5
# 输入
# 1
# hello
# REPLACE HELLO_WORLD
# 输出
# HELLO_WORLD 说明:超过文本替换
# 示例6
# 输入
# 2
# hello
# FORWARD 10000
# REPLACE O
# 输出
# hellO说明：超出文本长度替换
# 备注：文本长度不超过256K

射击比赛
#答题结果：规定时间内完成
#射击比赛对选手成绩进行排序（每个人取最高的三个分数之和）
#要求1：一个人多个射击成绩，次序不固定
#要求2：一个选手成绩少于3个，成绩无效，排名忽略该选手
#成绩相等按ID降序排列

# 输入：
# 第一行：整数N，表示总共进行了N次射击，产生了N个成绩分数（2<=N<=100)
# 第二行：长度为N的整数序列，表示选手ID
# 第三行：长度为N的整数序列，表示选手对应的成绩
# 例如
# 输入：
# 13
# 3,3,7,4,4,4,4,7,7,3,5,5,5
# 53,80,68,24,39,76,66,16,100,55,53,80,55
# 输出
# 5,3,7,4
ip_list = [["13","3,3,7,4,4,4,4,7,7,3,5,5,5","53,80,68,24,39,76,66,16,100,55,53,80,55"],
           ["6","3,4,4,3,3,4","66,55,55,66,66,55"]]

#--------获取输入
for ipp in ip_list:
    a = int(ipp[0])
    b = list(map(int,ipp[1].split(",")))
    c = list(map(int,ipp[2].split(",")))
#--------用字典存储成绩和ID并进行筛选，
    score_dic = {}
    for i in range(a):
        if not b[i] in list(score_dic.keys()):
            score_dic[b[i]] = [c[i]]
        else:
            score_dic[b[i]].append(c[i])
    ID_list = list(score_dic.keys())
    ID_list.sort(reverse=True)
    id_dict = {}
    for i in ID_list:
        #如果成绩小于3个，跳过
        e_s_list = score_dic[i]
        if len(e_s_list) < 3:
            pass
        #否则：取最高的三个求和，
        else:
            e_s_list.sort(reverse=True)
            sum_max3 = sum(e_s_list[:3])

              #将成绩呵呵ID对号填入字典，如果成绩一致，DI逆序排列
            if not sum_max3 in list(id_dict.keys()):
                id_dict[sum_max3] = str(i)
            else:
                id_dict[sum_max3] += f",{str(i)}"

#-------对Key进行排序，输出有效的排名序列
    scor_list = list(id_dict.keys())
    scor_list.sort(reverse=True)
    outt = id_dict[scor_list[0]]
    for i in range(1,len(scor_list)):
        outt += f",{id_dict[scor_list[i]]}"
    print(outt)


求解连续数列
# 用时37分钟 状态机混乱

# 求解
ip_list = [
    "3 5"

]

for ip in ip_list:
    S = int(ip.split()[0])
    n = int(ip.split()[1])
    junzhi = S//n
    shulie_list = []
    chazhi = 1
    flag = 0
    flag2 = 0
    #思路，算出平均值后，取平均值周围n + 2 个数，遍历求是否存在
    shulie_list.append(junzhi)
    for i in range(n//2 + 1 ):
        shulie_list.append(junzhi - chazhi)
        shulie_list.append((junzhi + chazhi))
        chazhi += 1
    shulie_list.sort()

    for i in range(len(shulie_list)-n):
        if sum(shulie_list[i:i+6]) == S:
            for e in shulie_list[i:i+6]:
                if e < 0: flag2 = -1
                break
            if flag2 == 0:
                print(" ".join(list(map(str,shulie_list[i:i+6]))))
                flag = 1
                break
            else:
                pass
    if flag == 0:
        print("-1")

字符匹配
#21分钟完成验算过程，规则与正则表达式完全一致
#输入
# ab aab
# .*
#输出
# 0,1
import re
ip_list = [["ab aab",".*"],["asdf abcd agddf","a.*d"]]
for ip in ip_list:
    a = ip[0]
    b = ip[1]
    pattern = re.compile("^"+b+"$")
    resoult_list = []
    for i,j in enumerate(a.split()):
        if pattern.match(j):
            resoult_list.append(i)
    print(",".join(list(map(str,resoult_list))))

分班
#答题结果：用时45分钟 做题过程有干扰
#两个班的小朋友混在一起，每个人都知道之前前面的是否和自己一班，区分出两个班的小朋友
# 与前同表示Y，不同N
# 小朋友不超过999
# 输出：从小到大排序，第一个编号的小朋友所在的班在第一行
# 只有一个班第二行为空
#输入不符合要求输出“ERROR”
# 输入1/N 2/Y 3/N 4/Y
# 输出
# 1 2
# 3 4

#-------------解题
#模拟多种输入
ip_list = ["1/N 2/Y 3/N 4/Y","5/Y 6/N 3/Y", "4/Y 3/Y 2/Y 10/Y"]
for ip in ip_list:

#获取输入 一行
    a = ip.split()
#判断输入有效,首先用空格分割，逐个判断是否格式满足要求
    flag_a_ok = 1
    for i in a:
        i_ss = i.split("/")
        if len(i_ss) != 2 or i_ss[1] not in ("Y","N") or not i_ss[0].isdigit():
            flag_a_ok = 0
        if i_ss[0].isdigit():
            if int(i_ss[0]) > 999 or int(i_ss[0]) < 0:
                flag_a_ok = 0
    if flag_a_ok == 1:
        # 分组
        f_zz = [[],[]]
        flag_j_12 = 0
        for i,j in enumerate(a):
            if i == 0:
                f_zz[0].append(j.split("/")[0])
            else:
                j_list = j.split("/")
                if j_list[1] == "Y":
                    f_zz[flag_j_12].append(j_list[0])
                else:
                    if flag_j_12 == 0: flag_j_12 = 1
                    else: flag_j_12 = 0
                    f_zz[flag_j_12].append(j_list[0])
        for i in f_zz:
            if i:
                out_list = list(map(int,i))
                out_list.sort()
                out_str = " ".join(list(map(str,out_list)))
                print(out_str)


    else:
        print("ERROR")

#排序后输出，第二组为空则不输出


拼接url
# 答题结果：用时14分钟 字符串拼接和处理
#  给定通过“，”分割的url 拼接成完整的url 前缀结尾和后缀开头都没有"/",则补全，前缀结尾和后缀开头都有，则去重
#约束：不用考虑前后缀合不合法
#输入：小于100的字符串
# /acm,/bb
# 输出凭借后的字符串
# /acm/bb

#-------------解题
#-----输入列表
ip_list = ["/acm,/bb"]

#获取输入
for ip in ip_list:
    ip_lt = ip.split(",")
    while ip_lt[0][-1] == "/":
        ip_lt[0] = ip_lt[0][:-1]
    while ip_lt[1][0] == "/":
        ip_lt[1] = ip_lt[1][1:]
    print("/".join(ip_lt))


出错的或电路
# 答题结果：注意，是不一样，不是种类，超时5分钟
import itertools

# 思路：两位数的组合
# 交换的结果
def jiaohuan(a,b):
    id_list = [i for i in range(int(n))]
    jhjg_list = itertools.combinations(id_list,2)
    result_list = []
    yuan = ""
    for i in range(int(n)):
        if a[i] == "1" or b[i]== "1":
            yuan += "1"
        else:
            yuan += '0'
    for e_l in jhjg_list:#交换两个顺序后和b进行或
        # print(e_l)
        new_a = list(a)
        e1 = new_a[e_l[0]]
        new_a[e_l[0]] = new_a[e_l[1]]
        new_a[e_l[1]] = e1
        ahb = ""
        for i in range(int(n)):
            if new_a[i] == "1" or b[i] == "1":
                ahb += "1"
            else:
                ahb += "0"
        if ahb != yuan:
            result_list.append(ahb)
    return len(result_list)






ip_list = [["6","011011","110110"]]
# ip_list = [["3","010","110"],["6","011011","110110"]]
for ip in ip_list:
# 输入：N 1<=N<=1000000
    n = ip[0]
# 输入：会比特交换
    a = ip[1]
# 输入：
    b = ip[2]
# 运算
    print(jiaohuan(a,b))


求字符串中所有整数的最小和
# 答题结果：49分钟写完，除了错用来re，还写错了变量
# import re
# 处理
def dfx(ip):
    # 取出字符串中所有最小的数，如果正：取单个数字，如果负数，贪婪取出
    ip_to_list = list(ip)
    min_list = []
    # ii = 0
    flag = 0
    while ip_to_list:
        if flag == 0 and ip_to_list[0] in "1234567890":
            min_list.append(ip_to_list[0])
            ip_to_list = ip_to_list[1:]
        elif ip_to_list[0] == "-":
            flag = 1
            fs = "-"
            ip_to_list = ip_to_list[1:]
            while ip_tp_list[0] in "1234567890":
                fs += ip_to_list[0]
                ip_to_list = ip_to_list[1:]
            min_list.append(fs)
            flag = 0
        else:
            ip_to_list = ip_to_list[1:]
    return sum(list(map(int,min_list)))



ip_list = ["bb1-234aa","bb12-34aa"]

for ip in ip_list:
    # 获取输入
    print(dfx(ip))
    #输出


TLV解码
# 答题结果
# TLV解码
# 码流字符串最大长度不超过50000个字节
ip_list = [
    [
        "31",
        "32 01 00 AE 90 02 00 01 02 30 03 00 AB 32 31 31 02 00 32 33 33 01 00 CC",
    ]
]
# 输入
for ip in ip_list:

    tag,ml_list = int(ip[0]),list(ip[1].split())
    dgml_list = []
    while ml_list:
        dgml_list.append(ml_list[:3+int(ml_list[1])])
        ml_list = ml_list[3+int(ml_list[1]):]
    for i in dgml_list:
        if i[0] == "31":
            print(" ".join(i[3:]))
            break
招聘
# 测验结果：超时20分钟，失败，原因为面试官姓名状态变量写错位置写在循环内

# 招聘
# 思路：创建一个面试官的状态机，随时间线的推移，判断是否需要新的面试官和面试官剩余的场次
ip_list = [["2","5","1 2","2 3","3 4","4 5","5 6",]]
for ip in ip_list:
    m = int(ip[0])
    n = int(ip[1])
    changci_list = [list(map(int,i.split())) for i in ip[2:]]
    # 面试官的状态机:字典值为一个列表，记录了该面试官当前的剩余次数、面试场次
    msg_dict = {}
    now_time = 0
    # 随时间增加，如果有面试开始
    last_time = 0
    for i in changci_list:
        if i[1] > last_time:
            last_time = i[1]
    msg_name = 1
    while now_time <= last_time:

        for e_m in changci_list:
            # if e_m[1] == now_time:# 优先结束面试，再开始面试
            #     for e_name in msg_dict.keys():
            #         if msg_dict[e_name][1] == e_m:

            if e_m[0] == now_time:
                # 遍历面试官，空闲者接管
                if not msg_dict:
                    msg_dict[msg_name] = [1, e_m]
                else:# 不为空，判断是否有人
                    flag_yr = 0
                    for e_name in msg_dict.keys():
                        if msg_dict[e_name][0] < m and msg_dict[e_name][1][1] <= now_time:
                            msg_dict[e_name][0] += 1
                            msg_dict[e_name][1] = e_m
                            flag_yr = 1
                            break
                    if flag_yr == 0:
                        msg_name += 1
                        msg_dict[msg_name] = [1, e_m]
        now_time += 1

    print(len(msg_dict))


字符串序列判定
# 答题结果：用时32分钟，因为反向操作字符串时索引有误

# 字符串序列判定
import re
ip_list = [
    [
        "ace"
        ,"abcde"
    ],
    [
        "fgh",
        "abcde"
    ]
]
# 获取输入

def dfx(a,b):
    # 判断条件：a的字符在b中能找到
    m_a = "^"+".*".join(list(a))+".*$"
    patern = re.compile(m_a)
    flag = 0
    last = 0
    for i in range(len(b)-1,-1,-1):
        if patern.match(b[i:]):
            flag = 1
            for j in range(len(b[i:])-1,-1,-1):
                if b[i:][j] == a[-1]:
                    last = j
            break
    if flag:
        return last
    else:
        return -1




for ip in ip_list:
    a,b = ip[0],ip[1]
    print(dfx(a,b))baowen


报文回路
#答题结果：25分钟结束
# 思路:设置一个列表记录每个站点的人数，初始值为0，对每个人的上下车进行统计，哪几站在车上，那几站人数加一
ip_list = [
    ["6",
     "1 3"
     ,"2 4"
     ,"1 4",
     "4 5"
     ,"4 6"
     ,"1 5"
     ,"3 4",
     "4 5",
     "4 7"]
]
def dfx(sxz):
    sxz_list = [list(map(int,i.split())) for i in sxz]
    zhandian_max = 0
    for i in sxz_list:
        if i[1]>zhandian_max:
            zhandian_max = i[1]

    renshu_list = [0 for i in range(zhandian_max+1)] # 记录每个站点后车身人数
    for i in sxz_list:
        for j in range(i[0],i[1]):
            renshu_list[j] += 1
    return renshu_list.index(max(renshu_list))

for ip in ip_list:
    n, sxz = ip[0],ip[1:]
    print(dfx(sxz))

5键键盘的输出
i
# 答题结果：39f分钟，由于一个判断的字符未加引号导致卡顿

#5键键盘的输出
def dfx(ml):
    ml_list = ml.split()
    textt = ""
    jinaqie = None
    quanxuan = None
    for e_m in ml_list:
        if e_m == "1":
            if quanxuan:
                textt = "a"
            else:
                textt += "a"
            quanxuan = None
        elif e_m == "2":
            if quanxuan:
                jinaqie = quanxuan
        elif e_m == "3":
            if quanxuan:
                jinaqie = quanxuan
                textt = ""
                quanxuan =None
        elif e_m == "4":
            if jinaqie:
                if quanxuan == None:
                    textt += jinaqie
                else:
                    textt = jinaqie
                quanxuan = None
        else:
            quanxuan = textt
    return len(textt)
# 输入
ip_list = [
    "1 1 5 1 5 2 4 4"
    ,"1 1 1"
]
for ip in ip_list:
    print(dfx(ip))

最长方连续方波信号
# 答题结果：42分钟，读题不清晰导致浪费时间，多思考
# 思路：1.将字符串以“00”分割后判断其中是否有连续高位（即”11“） 如果没有且其中有1则满足要求，再判断是否为最长
ip_list = [
    "00101010101100001010010"
]
def dfx(ip):
    # 遍历吧
    ii_list = ip.split("00")
    max_str = ""
    for i in ii_list:
        ipp = "0"+i.strip("0")+"0"
        if "11" in ipp:
            pass
        elif "1" in ipp:
            if len(ipp) > len(max_str):
                max_str = ipp

    return max_str if len(max_str) >= 3 else -1
for ip in ip_list:
    print(dfx(ip))


找车位
# 答题结果:用时39分钟
# 找车位
# 思路：使用动态规划，从左到右和从右到左分别求距离，每个位置取最小值

ip_lsit = [
    "1,0,0,0,0,0,1,0,0,1,0,1"
]
for ip in ip_lsit:
    chewei_list = ip.split(",")
    lenn = len(chewei_list)
    # 分别从左到右和从右到左
    jl_xy = [0 for ii in range(lenn+1)]
    jl_xz = [0 for ii in range(lenn+1)]
    jl_xy[0] = 0
    jl_xz[-1] = 0
    for i in range(1,lenn+1):
        if chewei_list[i-1] == "1":
            jl_xy[i] = 0
        else:
            jl_xy[i] = jl_xy[i-1] + 1
        if chewei_list[lenn-i] == "1":
            jl_xz[lenn-i] = 0
        else:
            jl_xz[lenn-i] = jl_xz[lenn-i+1] +1
    jl_xy.pop(0)
    jl_xz.pop(-1)
    resoult_list = [min([jl_xz[i],jl_xy[i]]) for i in range(lenn)]
    print(max(resoult_list))

找车位
# 答题结果
# 思路：将数字填充好后，逐行遍历
# 规则：对于每个值，如果等于目标值，判断左侧是否为空，为空 周长+1，上方为空，周长+1，右侧为空周长加一，下方为空周长加一

# 解题
import io

ip_list = [
    [
        "2",
        "1 1 3 2 2 2 3 2 4 3 2 3 3 3 4 4 1 4 2 4 3 4 4 5 2 5 3",
        "2 3 7 3 8 4 5 4 6 4 7 4 8 5 4 5 5 5 6 5 7 5 8 6 4 6 5 6 6 6 7 6 8 7 4 7 5 7 6 7 7 7 8"
    ]
]
for ip in ip_list:
    n = int(ip[0])
    tuxing_list = [i.split() for i in ip[1:]]
    #初始化二维列表
    dp =[[0 for i in range(64)] for j in range(64)]
    # 填充坐标
    zhouchang_dict = {}
    zhouchang_list = []
    for e_tx in tuxing_list:
        tianchong = e_tx[0]
        zhouchang_dict[tianchong] = 0
        zhouchang_list.append(tianchong)
        for i in range(1, len(e_tx)-1, 2):
            dp[int(e_tx[i])][int(e_tx[i+1])] = tianchong
    #分别求周长
    for i in range(64):
        for j in range(64):
            for z in zhouchang_list:
                if dp[i][j] == z:
                    if dp[i][j-1] != z:
                        zhouchang_dict[z] += 1
                    if dp[i-1][j] != z:
                        zhouchang_dict[z] += 1
                    if dp[i][j+1] != z:
                        zhouchang_dict[z] += 1
                    if dp[i+1][j] != z:
                        zhouchang_dict[z] += 1
    print(" ".join(list(map(str,list(zhouchang_dict.values())))))

we are a team
# 答题结果：超时6分钟
ip_list =[
    [
        "5 6",
        "1 2 0",
        "1 2 1",
        "1 5 0",
        "2 3 1",
        "2 5 1",
        "1 3 2 "

    ]
]
def dfx(ip):
    n, m = map(int, ip[0].split())
    if n < 1 or m < 1 or n > 100000 or m > 100000:
        return "NULL"
    out_list = []
    xioaxi_list = [i.split() for i in ip[1:]]
    guilei_list = []
    guilei_dict = {}
    shuchu_list = []
    tuandui_num = 0
    for e_xx in xioaxi_list:
        if not 0 <= int(e_xx[0]) <= 100000 and 0 <= int(e_xx[1]) <= 100000:
            out_list.append("da pian zi")
        else:
            if e_xx[2] == "0":
                if e_xx[0] in list(guilei_dict.keys()):
                    if e_xx[1] not in list(guilei_dict.keys()):
                        guilei_dict[e_xx[1]] = guilei_dict[e_xx[0]]
                    else:
                        for e_n in list(guilei_dict.keys()):
                            if guilei_dict[e_n] == guilei_dict[e_xx[1]]:
                                guilei_dict[e_n] = guilei_dict[e_xx[0]]
                elif e_xx[1] in list(guilei_dict.keys()):
                    if e_xx[0] not in list(guilei_dict.keys()):
                        guilei_dict[e_xx[0]] = guilei_dict[e_xx[1]]
                    else:
                        for e_n in list(guilei_dict.keys()):
                            if guilei_dict[e_n] == guilei_dict[e_xx[0]]:
                                guilei_dict[e_n] = guilei_dict[e_xx[1]]

                else:
                    guilei_dict[e_xx[0]] = guilei_dict[e_xx[1]] = tuandui_num
                    tuandui_num += 1
            elif e_xx[2] == "1":
                if e_xx[0] in list(guilei_dict.keys()) and e_xx[1] in list(guilei_dict.keys()):
                    if guilei_dict[e_xx[0]] == guilei_dict[e_xx[1]]:
                        out_list.append("we are a team")
                    else:
                        out_list.append("we are not a team")
                else:
                    out_list.append("we are not a team")
            else:
                out_list.append("da pian zi")
    return out_list


for ip in ip_list:
    print(dfx(ip))

最小传输时延
# 用时刚好
import idlelib.scrolledlist
import itertools
ip_list = [
    [
        "3 3",
        "1 2 11",
        "2 3 13",
        "1 3 50",
        "1 3",
    ]
]

def dfx(ip):
    N, M = map(int,ip[0].split())
    M_list = [i.split() for i in ip[1:-1]]
    qiu = list(map(int,ip[-1].split()))
    zuhe_list = list(itertools.combinations([i for i in range(1, N+1)], 2))
    zuhe_dict = {}
    for i in zuhe_list:
        zuhe_dict[i] = 100000

    for i in M_list:
        ii = list(map(int,i))
        zuhe_dict[tuple(ii[:-1])] = min(ii[2],zuhe_dict[tuple(ii[:-1])])
        for jj in zuhe_list:
            if jj[1] == ii[0]:
                zuhe_dict[tuple([jj[0],ii[1]])] = min(ii[2]+zuhe_dict[tuple(jj)],zuhe_dict[tuple([jj[0],ii[1]])])
            if jj[0] == ii[1]:
                zuhe_dict[tuple([ii[0],jj[1]])] = min(ii[2]+zuhe_dict[tuple(jj)],zuhe_dict[tuple([ii[0],jj[1]])])
    return zuhe_dict[tuple(qiu)] if zuhe_dict[tuple(qiu)] != 100000 else "-1"
for ip in ip_list:
    print(dfx(ip))

靠谱的车
# 靠谱的车 存疑
import time

ip_list = [
    "5"
    ,"100",
    "88888888"
]
def dfx(ip):
    time_st = time.time()
    out_put = None
    num = int(ip)
    biaoxian = 0
    shiji = 0
    while biaoxian <= num:
        bx_s = str(biaoxian)
        for i in range(len(bx_s)):
            if "4" in bx_s:
                bx_s = bx_s.replace("4", "5")
                biaoxian = int(bx_s)
        biaoxian += 1
        shiji += 1
    print(time.time() - time_st)
    return shiji -1


for ip in ip_list:
    print(dfx(ip))

最长字符串的长度
# 思路，遍历字符串

ip_list = [
    "bcbcbc",
    "looxdolx"
]
max_len = 0
for ip in ip_list:
    len_ip = len(ip)
    ip = ip + ip
    for i in range(len(ip)):
        for j in range(len(ip), -1, -1):
            if ip[i:j].count("o")%2 == 0:
                max_len = len(ip[i:j]) if len_ip>=len(ip[i:j]) > max_len else max_len

    print(max_len)


# N进制减法
# 2<= n <= 35
ip_list = [
    "2 11 1"

]
def dfx(ip):
    ip_li = list(map(int,ip.split()))
    ip_s_list = ip.split()
    # 判断
    if ip_li[1] != 0 and ip_s_list[1][0] == "0":
        return "-1"
    if ip_li[2] != 0 and ip_s_list[2][0] == "0":
        return "-1"
    if len(ip_s_list[1]) > 100 or len(ip_s_list[2])> 100:
        return "-1"
    fuhao = 0
    if ip_li[0] == 2:
        try:
            result = eval("0b{}".format(ip_li[1])) - eval("0b{}".format(ip_li[2]))

        except:
            return "-1"
        if result < 0 : fuhao = 1
        result = bin(result).split("b")[1]
        return f"{fuhao} {result}"
    elif ip_li[0] == 8:
        try:

    elif ip_li[0] == 10:
        pass
    elif ip_li[0] == 11:
        pass
for ip in ip_list:
    print(dfx(ip))
    # 判断输入是否异常

百钱买百鸡
xj_max = 100
while xj_max >= 0:
    mj_max = 0
    while mj_max <= 33:
        jw_max = 0
        while jw_max <= 20:
            if 5*jw_max +3 * mj_max + 1/3*xj_max == 100 and jw_max + mj_max + xj_max == 100:
                print(f"{jw_max} {mj_max} {xj_max}")
            jw_max += 1
        mj_max += 1
    xj_max -= 1

二十四点运算
import itertools
a = "7 2 1 10"
#迭代规则，从四个数字中随机拿出两个数，再从四个运算符中拿出一个，然后计算将结果放入待运算列表继续计算，直到待运算列表中只有一个数字

a_num = list(map(int,a.split()))
def yunsuan(leave_num):
    leave_num_list = []
    for i in itertools.combinations(leave_num,2):
        new_leave = []
        new_leave.append(i[0]*i[1])
        a_num_list = leave_num.copy()
        a_num_list.remove(i[0])
        a_num_list.remove(i[1])
        new_leave+=a_num_list
        leave_num_list.append(new_leave)
        if i[1] != 0:
            new_leave = []
            new_leave.append(i[0] / i[1])
            a_num_list = leave_num.copy()
            a_num_list.remove(i[0])
            a_num_list.remove(i[1])
            new_leave+=a_num_list
            leave_num_list.append(new_leave)
        new_leave = []
        new_leave.append(i[0] + i[1])
        a_num_list = leave_num.copy()
        a_num_list.remove(i[0])
        a_num_list.remove(i[1])
        new_leave+=a_num_list
        leave_num_list.append(new_leave)
        new_leave = []
        new_leave.append(i[0] - i[1])
        a_num_list = leave_num.copy()
        a_num_list.remove(i[0])
        a_num_list.remove(i[1])
        new_leave+=a_num_list
        leave_num_list.append(new_leave)
    return leave_num_list
flag = []
fuhao_list = ""
def dfx(leave_num):
    if len(leave_num) == 1 and leave_num[0] == 24:
        flag.append(1)
    else:
        if len(leave_num) > 1:
            for i in yunsuan(leave_num):
                dfx(i)
    # return False
dfx(a_num)
if flag:
    print("true")
else:
    print("false")
# print(yunsuan([1,2,3,4]))

放苹果
import time

time_start = time.time()

m,n = 9,8
n_list = [0 for i in range(n)]

# result_list = []
# #使用迭代的方法
# def dfx(n_list):
#     if sum(n_list) < m:
#         tmp_list = []
#         for i in range(n):
#             tmp = n_list.copy()
#             tmp[i] += 1
#             tmp.sort()
#             if tmp not in tmp_list:
#                 tmp_list.append(tmp)
#         for i in tmp_list:
#             dfx(i)
# #             del tmp
#         pass
#     else:
#         tmp = n_list.copy()
#         tmp.sort()
#         if tmp not in result_list:
#             result_list.append(tmp)


result_list = []
#使用迭代的方法
def dfx(n_list):
    if sum(n_list) < m:
        tmp_list = []
        for i in range(n):
            tmp = n_list.copy()
            tmp[i] += 1
            tmp.sort()
            if tmp not in tmp_list:
                tmp_list.append(tmp)
        print(tmp_list)
        for i in tmp_list:
            dfx(i)
#             del tmp
        pass
    else:
        tmp = n_list.copy()
        tmp.sort()
        if tmp not in result_list:
            result_list.append(tmp)
dfx(n_list)
print(len(result_list))

购物车
n, m = map(int,"1000 5".split())
primary, annex = {}, {}
ip_list = """800 2 0
400 5 1
300 5 1
400 3 0
500 2 0""".split("\n")
for i in range(1,m+1):
    x, y, z = map(int, ip_list[i-1].split())
    if z==0:
        primary[i] = [x, y]
    else:
        if z in annex:
            annex[z].append([x, y])
        else:
            annex[z] = [[x,y]]
dp = [0]*(n+1)
for key in primary:
    w, v= [], []
    w.append(primary[key][0])#1、主件
    v.append(primary[key][0]*primary[key][1])
    if key in annex:#存在附件
        w.append(w[0]+annex[key][0][0])#2、主件+附件1
        v.append(v[0]+annex[key][0][0]*annex[key][0][1])
        if len(annex[key])>1:#附件个数为2
            w.append(w[0]+annex[key][1][0])#3、主件+附件2
            v.append(v[0]+annex[key][1][0]*annex[key][1][1])
            w.append(w[0]+annex[key][0][0]+annex[key][1][0])#4、主件+附件1+附件2
            v.append(v[0]+annex[key][0][0]*annex[key][0][1]+annex[key][1][0]*annex[key][1][1])
    for j in range(n,-1,-10):#物品的价格是10的整数倍
        for k in range(len(w)):
            if j-w[k]>=0:
                dp[j] = max(dp[j], dp[j-w[k]]+v[k])
print(dp)

将真分数分解为埃及分数
a = list(map(int,input().split("/")))

a_value = a[0]/a[1]
fenmu = 2
aiji_list = []
while a_value > 0:
    if a_value - 1/fenmu >= 0:
        a_value -= 1/fenmu
        aiji_list.append(f"1/{fenmu}")
    fenmu += 1
print("+".join(aiji_list))

矩阵乘法计算量估算
n = "3"
juzheng_list = [[50,10],[10,20],[20,5]]
# for i in range(n):
#     juzheng_list.append(list(map(int, input().split())))
gongshi = "(A(BC))"
juzheng_dict = {}
t_i = 0
for i in gongshi:
    if i not in "()":
        juzheng_dict[i] = juzheng_list[t_i]
        t_i += 1


def jisuan_liangg(J_a, J_b):
    return (J_a[0] * J_a[1] * J_b[1], [J_a[0], J_b[1]])


jisuanliang = 0

daijisuan = []
for i in range(len(gongshi)):
    if gongshi[i] == ")":
        jsl = jisuan_liangg(daijisuan[-2], daijisuan[-1])
        daijisuan = daijisuan[:-2]
        daijisuan.append(jsl[1])
        jisuanliang += jsl[0]
    elif gongshi[i] != "(":
        daijisuan.append(juzheng_dict[gongshi[i]])
    else:
        pass
while len(daijisuan) >= 2:
    jsl = jisuan_liangg(daijisuan[0], daijisuan[1])
    daijisuan = [jsl[1]] + daijisuan[2:]
    jisuanliang += jsl[0]
print(jisuanliang)

梅花桩
n = 6
num_list = list(map(int, "2 5 1 5 4 5".split()))
help_list = [1] * n
for i in range(1, n):
    for j in range(i):
        if num_list[i] > num_list[j]:
            help_list[i] = max(help_list[i], help_list[j] + 1)
max_len = max(help_list)
print(max_len)

素数伴侣
#求得的“最佳方案”组成“素数伴侣”的对数。
inputt = list(map(int,"2 5 6 13".split(" ")))
lenn = len(inputt)
pipei_dic = {}

def sum_is_sushu(a,b):
    c = a + b
    i = 2
    flag = 0
    while i ** 2 <= c:
        if c/i - c//i >0:
            flag =1
        i += 1
    return True if flag == 0 else False

for i,j in enumerate(inputt):
    pipei_dic[i] = None
for i,a in enumerate(inputt):
    for j in range(i+1,lenn):
        if sum_is_sushu(a,inputt[j]):
            if pipei_dic[j]:
                for z in range(pipei_dic[j]+1,lenn):
                    if sum_is_sushu(inputt[pipei_dic[j]],inputt[z]) and not pipei_dic[z]:
                        pipei_dic[pipei_dic[z]] = pipei_dic[j]
                        pipei_dic[j] = i
                        break
            else:
                pipei_dic[j] = i
                break
print(pipei_dic)

通配符
a = "u*w"
b = "uyw"
#使用迭代
flag = []
def is_pp(a,b):
    if not a and not b:
        flag.append(1)
    elif len(a) > 0 and len(b)> 0 and a[0] == b[0]:
        is_pp(a[1:],b[1:])
    else:
        if a[0] not in ("?","*"):
            pass
        else:
            if a[0] == "?" and b[0] in "qwertyuioplkjhgfdsazxcvbnm0123456789":
                is_pp(a[1:],b[1:])
            if a[0] == "*":
                addd = 0
                while addd < len(b):
                    is_pp(a[1:],b[addd:])
                    addd += 1

is_pp(a,b)
print("true" if 1 in flag and 2 not in flag else "false")

在字符串中找出连续最长的数字串：
def have_zc(a):
    # 获取输入

    len_a = len(a)
    # 从大到小遍历截取，发现后收集长度字符串并按先后顺序保存
    resoult_list = []
    len_pd = len_a
    while len_pd > 0:
        for i in range(len_a - len_pd+1):
            if a[i:i + len_pd].isdigit():
                resoult_list.append(a[i:i + len_pd])
        if resoult_list:
            return resoult_list
        len_pd -= 1
    return False


# 按格式输出
while True:
    try:
        a = input()
        havv = have_zc(a)
        if havv:
            print("".join(havv) + ",{}".format(len(havv[0])))
    except:
        break


