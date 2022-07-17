#猜密碼

password = 'a123'

guess = input('請輸入密碼 : ')

count = 2

while  True:
	if guess != password:
		if count <= 0:
			print('失敗!')
			break
		else:
			
			print('密碼錯誤! 還有', count, '次機會')
			guess = input('請輸入密碼 : ')
			count = count  - 1
	else:
		print('登入成功!')
		break