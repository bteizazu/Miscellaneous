from itertools import permutations

numbers = [1,4,2,8,57]



def operate(operand1, operand2, operator):
    if operator == 'A':
      return(operand1 + operand2)
    if operator == 'S':
      return(operand1 - operand2)
    if operator == 'M':
      return(operand1 * operand2)
    if operator == 'D':
      if (operand1 % operand2 == 0):
      	return(int(operand1 / operand2))
      else:
      	return(operand1 / operand2)
     

l = list(permutations(['D','M','A','S']))
for operatorList in l:
  stringDisplay = str(numbers[0])
  numbers2 = [numbers[0]]
  operatorList2 = []
  i=1
  j=1
  for operator in operatorList:
    if operator == 'A':
      stringDisplay += (' + ' + str(numbers[i]))
      operatorList2.append('A')
      numbers2.append(numbers[i])
    if operator == 'S':
      stringDisplay += (' - ' + str(numbers[i]))
      operatorList2.append('S')
      numbers2.append(numbers[i])
    if operator == 'M':
      stringDisplay += (' * ' + str(numbers[i]))
      numbers2[-1] = operate(numbers2[-1], numbers[i], operator)
    if operator == 'D':
      stringDisplay += (' / ' + str(numbers[i]))
      numbers2[-1] = operate(numbers2[-1], numbers[i], operator)
      
    i += 1
    
  assert(len(operatorList2) == 2)  
  assert(len(numbers2) == 3)
  assert(i == 5)

  runningNum = numbers2[0]
  
  for operator in operatorList2:
      runningNum = operate(runningNum, numbers2[j], operator)    
    
#    if operator == 'A':
#      runningNum = operate(runningNums, numbers2[j], operator)
      
#    if operator == 'S':
#      runningNum = operate(runningNums, numbers2[j], operator)

      j += 1
  
  assert(j == 3)
  stringDisplay += (' = ' + str(runningNum))
  print(operatorList, '-->', stringDisplay)
  if int(runningNum) == 42:
    solution = ''
    for char in operatorList:
      solution += char
    print("Solution: ", solution)
    break
