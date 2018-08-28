password = 'a123456'
count = 3

while count > 0 :
    your_guess = input('guess password:')
    count = count-1
    if your_guess != password :
   
      print('密碼錯誤，還有',count,'次機會')
    else:
      print('登入成功')
      break