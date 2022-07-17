#猜密碼

password = 'a1234'
count = 3

while count > 0:
	count = count - 1
	guess = input('請輸入密碼 : ')
	if guess == password:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!')
		if count > 0:
			print('還有', count, '次機會')
		else:
			print('失敗')
		