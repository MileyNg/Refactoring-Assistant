#coding:utf-8
while 1:
    try:
        #初期化
        key=[0]*101
        #オイラー路：すべての頂点のうち、次数が奇数であるものがちょうど２つ(入口と出口)
        while 1:
            input = map(int, raw_input().split())
            if(input[0] == 0 and input[1] == 0):
                break
            key[input[0]]+=1
            key[input[1]]+=1

        if(key[1]%2 == 1 and key[2]%2==1 and len(filter(lambda x:x%2==1,key[3:]))==0):
            print "OK"
        else:
            print "NG"
    except:
        break