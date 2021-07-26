password = 'a123456'
x = 3
while True:
	code = input('請輸入密碼')
	if code == password:
		print('登入成功')
		break
	else:
		x = x-1
		print('密碼錯誤還剩', x, '次機會')
        if x == 0:
        	break