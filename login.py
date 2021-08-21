import json#载入json模块
uap=open('data/uap.json')#打开json文件
uapv=json.load(uap)#读取json文件

uspv1=uapv['user']#获取‘user’的值
uspv2=uapv['password']#获取'password'的值
napss=""#空文本

li=0#计数
try:
    while True:
        input_u = input("User:")#显示输入框（用户名）
        password_p = input("PassWord:")#显示密码输入框
        if input_u != napss and password_p != napss:#判断是否其中或另一为空文本
            if input_u == uspv1 and password_p == uspv2:#判断密码是否输入正确
                print("欢迎！",input_u)#当登录成功时
                while True:#登录成功时操作输入
                    i=input(">>>:")
            if input_u != uspv1 or password_p != uspv2:#当密码错误时
                print("账户或密码错误，请重试！") 
        if input_u == napss or password_p == napss:#两者为空时
            print("账户或密码不能为空")
except KeyboardInterrupt:
    print("Bye!")
