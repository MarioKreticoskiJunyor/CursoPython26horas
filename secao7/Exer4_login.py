# Usuário digita login e senha

# no sistema crie o um username e password de acordo com:

# username: admin
# password: 123456

# certo: login ok 
# Errado: usuário e senha incorreto

username = 'admin'
password = '123456'

login = input('Informe seu login:')
senha = input('Infome sua senha:')


if login == username and senha == password:
    print('Login e senha correto!')
else:
    ('login e senha incorreto!')
