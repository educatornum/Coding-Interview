i = 0
# n = ['white', 'white', 'black', 'white', 'black', 'white', 'white', 'white', 'black', 'black']
n = ['white', 'white', 'black', 'white', 'black']
answers = []
success_min = len(n) - 1

def find_parity(known):
    print("Нийт малгай: ", n)
    print("Мэдэгдэж байгаа: " + str(known))
    no_white = known.count('white')
    print ("Нийт цагаан малгайны тоо: " + str(no_white))
    if no_white % 2 == 0:
        parity = 'even' # even- tegsh
    else:
        parity = 'odd' # sondgoi
    # if parity == 'even':
    #     print ("Нийт цагаан малгайны тоо: ТЭГШ")
    # else:
    #     print ("Нийт цагаан малгайны тоо: СОНДГОЙ")
    print("---"*30)
    return parity

def my_hat(n, i, success_min):
    incorrect = 0
    correct = 0
    while i < len(n):
        
        # start riddle logic
        known = n[i+1:]
        # print("KNOW people", known, len(known))
        known_parity = find_parity(known)
        if i == 0:
            print("Хамгийн эхний хүн:",i+1)
            if known_parity == 'even': #tegsh
                guess = 'white'
            else:
                guess = 'black'  #odd- сондгой
        elif i == 1:
            print(i+1,"дах хүн:")
            if current_parity != known_parity:
                # print ("current_parity != known_parity")
                if guess == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
            else:
                print( "current_parity == known_parity")
        else:
            print(i+1,"дах хүн:")
            past = answers[1:]
            # print( "past: " + str(past))
            new_known = past + known
            # print ("new_known: " + str(new_known))
            last = answers[-1]
            print("last",last)
            # print ("last: " + last)

            known_parity = find_parity(new_known)
            print("known_parity:",known_parity)
            print("current_parity:",current_parity)
            if current_parity != known_parity:
                # print( "current_parity != known_parity")
                if last == 'white':
                    guess = 'black'
                else:
                    guess = 'white'
            # else:
            #     print("current_parity == known_parity")

        current_parity = known_parity
        answers.append(guess)
        print(" ТААСАН ХАРИУЛТ : " + guess)
        # print(" ХАРИУЛТ: " + str(answers))
        # end riddle logic

        if guess == n[i]:
            correct += 1
            print("ЗӨВ ХАРИУЛТЫН НИЙТ ТОО: " , str(correct))
        else:
            incorrect += 1
            print( "БУРУУ ХАРИУЛТЫН НИЙТ ТОО:" , str(incorrect))
        i += 1
    print ("minimum needed to succeed: " , str(success_min))
    return correct >= success_min

# print ("Passed? " + str(my_hat(n, i, success_min)))



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
import unittest
def solution_a(a):
    B = set(sorted(a))
    m = 1
    for x in B:
        if x == m:
            m+=1
    return m
arr = [1, 3, 6, 4, 1, 2]
# arr  = [10,20,30,40]
print(solution_a(a=arr))

class TestSolutionA(unittest.TestCase):
    def test_case0(self):
      input_list = [1, 3, 6, 4, 1, 2]
      val = solution_a(input_list)
      self.assertEqual(val, 5)

    def test_case1(self):
      input_list = [1, 2, 3]
      val = solution_a(input_list)
      self.assertEqual(val, 4)

    def test_case2(self):
      input_list = [ -1, -3]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case3(self):
      input_list = [100000, 500, 10]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case4(self):
      input_list = [ -5, -10, -2, 0]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case5(self):
      input_list = [ -5, -10, -2, 0]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

    def test_case6(self):
      input_list = [-266959, -559850, 667410, -370471, -695927, 170911, 658702, -737673, 370182, -285767]
      val = solution_a(input_list)
      self.assertEqual(val, 1)

if __name__ == '__main__':
    unittest.main()