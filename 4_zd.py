# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
a = int(input('Введите длинну шоколадки в дольках' ))
b = int(input('Введите ширину шоколадки в дольках' ))
c = int(input('Введите сколько долек вы хотите отломить' ))
f = bool( c%a==0 or c%b==0)
print(f)