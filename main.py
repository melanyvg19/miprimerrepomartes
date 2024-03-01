userDB="hidrotech123"
passwordDB="admin123*"

print('Software Tech Hidroituango')
print('*************')
userName= input('Digita tu usuario: ')
userPassword = input('Digite su contraseña: ')

'''if userDB == userName and passwordDB == userPassword:
    print('Éxito en su usuario')
else:
    print('Incorrecto')'''

print('Éxito en su usuario') if userDB == userName and passwordDB == userPassword else print('Incorrecto')