
from art import tprint

tprint('caesar')


while True:
    option = (input('Введите - 1 (закодировать) и - 2 (декодировать); - /stop (для остановки программы): '))
    if option == '/stop':
        exit()
    if option == '1':
        def caesar(x, n, rad):
            msg = str(x)
            alphabet = [chr(i) for i in range(97, 123)] * 11
            betalphabet = [i for i in range(0, 10)] * 11
            if n == 0:
                return msg

            # счетчики + выводимое значение
            count = 0
            st_count = 'Количество закодированных символов равняется: '
            code_msg = ''
            # hash
            a_1 = n
            a_2 = rad
            a_1 += 24 * len(msg)
            a_2 += 5 * len(msg)
            a_1 = hex(a_1)
            a_2 = hex(a_2)
            hash_ = str(a_1) + '.' + str(a_2)
            st_hash = 'Hash:  '
            for i in range(0, len(msg)):
                if msg[i] == ' ':
                    code_msg += ' '
                    continue
                if rad in range(2, len(msg) + 1):
                    if (i + 1) % int(rad) == 0:
                        code_msg += msg[i]
                        continue
                for k in range(len(betalphabet)):
                    if msg[i] == str(betalphabet[k]):
                        code_msg += str(betalphabet[k + n])
                        count += 1
                        break
                for j in range(len(alphabet)):
                    if msg[i] == alphabet[j]:
                        code_msg += str(alphabet[j + n])
                        count += 1
                        break

            st_count += str(count)
            st_hash += hash_
            return code_msg, st_count, st_hash


        # проверка и запуск + визуальная составляющая
        count_program = 1  # номер примера

        while True:  # бесконечная работа программы
            print(str(count_program) + ')')
            count_program += 1
            a = [chr(i) for i in range(97, 123)] * 11
            b = [str(i) for i in range(0, 10)] * 11
            fl1 = 0
            fl2 = 0
            fl3 = 0

            while fl1 == 0:
                msg_user = input(
                    'Введите сообщение, которое следует закодировать (используя ЦИФРЫ и буквы ЛАТИНСКОГО алфавита, также разрешены ПРОБЕЛЫ ; чтобы остановить программу введите здесь - /stop): ')
                l = 0
                if msg_user == '/stop':  # остановка программы
                    exit()
                for i in range(len(msg_user)):
                    if (msg_user[i] in a) or (msg_user[i] in b) or str(msg_user[i]) == ' ':
                        l += 1
                if l == len(msg_user):
                    fl1 = 1
                    break
            while fl2 == 0:
                num_user = input('Введите необходимый сдвиг значения (только целое число): ')
                try:
                    int(num_user)
                    fl2 = 1
                    num_user = int(num_user)
                    break
                except ValueError:
                    fl2 = 0

            while fl3 == 0:
                rad_user = input(
                    'Введите шаг кодировки (каждый n-символ не кодируется), если шаг не требуется, введите - 1 (только целое число): ')
                try:
                    int(rad_user)
                    fl3 = 1
                    rad_user = int(rad_user)
                    break
                except ValueError:
                    fl3 = 0

            print(caesar(msg_user, num_user, rad_user), '\n')
    if option == '2':
        def de_caesar(y, x):
            hash_ = x.split('.')
            alphabet = [chr(i) for i in range(97, 123)] * 11
            betalphabet = [i for i in range(0, 10)] * 11
            msgy = str(y)
            # счетчики + выводимое значение
            count = 0
            st_count = 'Количество декодированных символов: '
            msg = ''
            # hash
            a_1 = hash_[0]
            a_2 = hash_[1]
            a_1 = int(a_1, 16)
            a_2 = int(a_2, 16)
            a_1 -= 24 * len(y)
            a_2 -= 5 * len(y)
            for i in range(0, len(msgy)):
                if msgy[i] == ' ':
                    msg += ' '
                    continue
                if a_2 in range(2, len(msgy)+1):
                    if (i+1) % int(a_2) == 0:
                        msg += msgy[i]
                        continue
                for k in range(50, len(betalphabet)):
                    if msgy[i] == str(betalphabet[k]):
                        msg += str(betalphabet[k - a_1])
                        count += 1
                        break
                for j in range(130, len(alphabet)):
                    if msgy[i] == alphabet[j]:
                        msg += str(alphabet[j - a_1])
                        count += 1
                        break
            st_count += str(count)



            return msg, st_count


        # проверка и запуск + визуальная составляющая
        count_program = 1  # номер примера

        while True:        # бесконечная работа программы
            print(str(count_program) + '>>')
            count_program += 1
            a = [chr(i) for i in range(97, 123)] * 11
            b = [str(i) for i in range(0, 10)] * 11
            fl1 = 0
            fl2 = 0
            fl3 = 0

            while fl1 == 0:
                msgy_user = input('Введите сообщение, которое следует декодировать (используя ЦИФРЫ и буквы ЛАТИНСКОГО алфавита, также разрешены ПРОБЕЛЫ ; чтобы остановить программу введите здесь - /stop): ')
                l = 0
                if msgy_user == '/stop':   # остановка программы
                    exit()
                for i in range(len(msgy_user)):
                    if (msgy_user[i] in a) or (msgy_user[i] in b) or str(msgy_user[i]) == ' ':
                        l += 1
                if l == len(msgy_user):
                    fl1 = 1
                    break
            while fl2 == 0:
                hash_user = input('Введите ~Hash~ программы-кодировщика (используя ЦИФРЫ и буквы ЛАТИНСКОГО алфавита, ТОЧКА обязательна: ')
                p = 0
                fl3 = 0
                if '.' in hash_user:
                    fl3 = 1
                for i in range(len(hash_user)):
                    if ((hash_user[i] in a) or (hash_user[i] in b) or str(hash_user[i]) == ' ' or str(hash_user[i]) == '.' ) and (fl3 == 1):
                        p += 1
                if p == len(hash_user):
                    fl2 = 1
                    break

            print(de_caesar(msgy_user, hash_user), '\n')
    else:
        continue
