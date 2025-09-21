user_input = input("Введите выражение:")
num_list = []
op_list = []

num = ''
pre_res = 0
res = 0


for i in user_input:
    if i.isdigit() or i == '.' or i == ",":
        num = num + i
    elif i == ' ':
        continue
    elif i.isalpha():
        print("Введено неккоректное математическое выражение!")
        break
    else:
        if num != '':
            num_list.append(float(num))
            num = ''
        op = i
        if op in op_list:
            op_list[0] += op
        else:
            op_list.append(op)

if num != '':
    num_list.append(float(num))
       
res = eval(f'{num_list[0]} {op_list[0]} {num_list[1]}')

print(f"Результат: {res}")
