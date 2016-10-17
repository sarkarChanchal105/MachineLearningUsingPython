def solution(number):
  print (number)
  array=[];i=1; multi_3=0;multi_5=0;done=False
  if number<3:
      return number
  while(done ==False and number>0):
    multi_3=3*i
    multi_5=5*i

    if 3*(i+1)>number:
        done=True

    if multi_3 not in array :
        array.append(multi_3)

    if multi_5 not in array and multi_5<number :
        array.append(multi_5)
    i+=1

  print(array)
  return sum(array)


print(solution(10))