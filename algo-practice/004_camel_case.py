import sys
def camel_case_4(input):
    first = input[0]
    second = input[2]
    phrase = input[4:]
    if first=='S':
        #split operation
        if second=='M':
            phrase = phrase[:-2]
        phrase = phrase[0].upper()+phrase[1:] #for consistency between object names
        upper_idx = [idx for idx, char in enumerate(phrase) if char.isupper()]+[len(phrase)]
        output = ' '.join([phrase[upper_idx[i]:upper_idx[i+1]].lower() for i in range(0,len(upper_idx)-1)])
    else:
        output = phrase.split(' ')
        output = ''.join([x[0].upper()+x[1:] for x in output])
        if second != 'C':
            output = output[0].lower()+output[1:]
        if second == 'M':
            output += '()'
    return output
    
if __name__=='__main__':
    if 1:
        inputData = [line.rstrip('\n\r') for line in sys.stdin.readlines()]
        for i in inputData:
            print(camel_case_4(i))
    else:
        # test cases:
        test_cases = ['S;M;plasticCup()','C;V;mobile phone','C;C;coffee machine','S;C;LargeSoftwareBook','C;M;white sheet of paper','S;V;pictureFrame']
        desired_output = ['plastic cup','mobilePhone','CoffeeMachine','large software book','whiteSheetOfPaper()','picture frame']
        all_pass = True
        for test, desired in zip(test_cases, desired_output):
            output = camel_case_4(test)
            if output == desired:
                score = 'Pass'
            else:
                score = 'Fail'
                all_pass = False
            print(f'Test: {test}\nOutput: {output}\nResult: {score}\n')
        if all_pass:
            print('ALL TESTS PASS')
        else:
            print('NOT ALL TESTS PASS')