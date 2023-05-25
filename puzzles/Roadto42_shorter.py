from itertools import permutations

numbers = [12,34,56,7,8]

operatorDict = {'D':' / ','M':' * ','A':' + ','S':' - '}  

l = list(permutations(['D','M','A','S']))
for operatorList in l:
  stringDisplay = str(numbers[0])
  i=1
  for operator in operatorList:
    stringDisplay += (operatorDict[operator] + str(numbers[i])) 
    i += 1
  runningNum = eval(stringDisplay)   
  print(operatorList,'-->',stringDisplay,' = ' + str(runningNum))
  if(runningNum == 42):
    solution = operatorList[0]+operatorList[1]+operatorList[2]+operatorList[3]
    print("Solution: ", solution)
    break