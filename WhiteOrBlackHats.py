i = 0
n = ['white', 'white', 'black', 'white', 'black', 'white', 'white', 'white', 'black', 'black']
# n = ['white', 'white', 'black', 'white', 'black']
answers = []
success_min = len(n) - 1

def find_parity(known):
    print("Нийт малгай: ", n)
    print("Мэдэгдэж байгаа: " + str(known))
    no_white = known.count('white')
    print ("Нийт цагаан малгайны тоо: " + str(no_white))
    if no_white % 2 == 0:
        parity = 'even' 
    else:
        parity = 'odd' 
    print("---"*30)
    return parity

def my_hat(n, i, success_min):
    incorrect = 0
    correct = 0
    while i < len(n):
        known = n[i+1:]
        known_parity = find_parity(known)
        if i == 0:
            print("Хамгийн эхний хүн:",i+1)
            if known_parity == 'even': 
                guess = 'white'
            else:
                guess = 'black' 
        elif i == 1:
            print(i+1,"дах хүн:")
            if current_parity != known_parity:
                if guess == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
            else:
                print( "current_parity == known_parity")
        else:
            print(i+1,"дах хүн:")
            past = answers[1:]
            new_known = past + known
            last = answers[-1]
            print("last",last)
            known_parity = find_parity(new_known)
            print("known_parity:",known_parity)
            print("current_parity:",current_parity)
            if current_parity != known_parity:
                if last == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
        current_parity = known_parity
        answers.append(guess)
        print(" ТААСАН ХАРИУЛТ : " + guess)

        if guess == n[i]:
            correct += 1
            print("ЗӨВ ХАРИУЛТЫН НИЙТ ТОО: " , str(correct))
        else:
            incorrect += 1
            print( "БУРУУ ХАРИУЛТЫН НИЙТ ТОО:" , str(incorrect))
        i += 1
    print ("minimum needed to succeed: " , str(success_min))
    return correct >= success_min

print ("Passed? " + str(my_hat(n, i, success_min)))

"""
    Explain:

    1.  The first man counts the only white hats. 
    2.  Then he can say “I’m white” if the total quantity of white hats is “even”. If it isn't even he can say “I’m black”. His chance is 50% 50%. He can mistake.
    3.  The second guy must check 2 conditions. The last total quantity of white hats is not equal to now total quantity of white hats. Second is, he can say “I’m black” if the first guy’s guess was “black”. If isn’t black he can say “I’m white”.  It will be good. Because he knows the total quantity of white hats.
    4.  The third guy can say “I’m black” if the second guy's guess is “white”. If it isn’t “white”, he is the “white”.
    5.  The next guys are the same as the third guy.
"""

"""
1. Хамгийн эхний хүн буюу 10 дах хүн өмнөх бүх хүнийхээ цагаан өнгөтэй малгайг тоолно.

2. Хэрвээ нийт тоолсон цагаан малгай нь сондгой байвал "ЦАГААН" үгүй байвал "ХАР" гэж таана.
   Энэ хүн нь л зөвхөн алдах эрхтэй ба боломж 50% 50% тай байна.


3.  Дараагийн хүн нь өмнөх хүн нь "ЦАГААН" гэж таасан бол 
    "ХАР" гэж таана үгүй бол "ЦАГААН" гэж таана.

    Өмнөх цагаан малгайны нийт тоо одоо байгаа цагаан малгайны тооноос өөр
    байгаад өмнөх хүний хариулт цагаан байсан бол хар үгүй бол цагаан
    гэж хариулна


"""
