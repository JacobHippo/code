password = 'a123456'
code = input('請輸入密碼')
x = 0
y = 2
if code == password:
	print('登入成功')
while code != password and x != 2 :
	print('密碼錯誤還有' ,y )
	x = x + 1
	y = 2 - x
	code = input('請輸入密碼')
if code == password and x != 0 and x != 1:
    print('登入成功')	
raise SystemExit