# -*- coding: utf-8 -*-
"""
Created on Mon Oct 29 22:58:39 2018

@author: 15541
这是创邻科技笔试题第二题，已经通过验证了，由于晚上要参加他们的笔试，所以做了一下
"""
#通过月份处理
def re_list_month(List,n):
   b = (n-1) % len(List)
   if b == 0:
       List = List
   else:
       List = List[b:] + List[0:b]
   return List
#通过日处理
#输入字符串和数字n，输出字符串向前移动n-1后的字符串结果。
def re_list_day(List,n):
   b = (n-1) % len(List)
   if b == 0:
       List = List
   else:
       List = List[b:] + List[0:b]
   return List

def decode():
    List = ['ABCDEFGHI','JKLMNOPQR','STUVWXYZ ']
    #第一行是用空格分隔的两个数字，第一个数字是月份，第二个数字是日子。输入保证是一个合法的日期。
    date_list = [int(i) for i in input().split()]
    #第二行为需要编码的信息字符串，仅由A~Z和空格组成，长度不超过1024个字符
    decode_list = input()
    ABC = re_list_month(List,date_list[0])
    abc = []
    for i in ABC:
        xyz = re_list_day(i,date_list[1])
        abc.append(xyz)
    ans = []
    for k in decode_list:
        for i in range(0,3):
            for j in range(0,9):
                if abc[i][j] == k:
                    a = int(str(i+1)+str(j+1))
                    ans.append(a)
    for i in ans:
        print(i,end=' ')
if __name__ == "__main__":
    decode()
