'''
#celsius to fahenheit converter
def c_to_f(c):
    f=(1.8*c)+32
    return f
f=c_to_f(22)
print('farenheit is:'+str(f))


#miles to km converter
m=int(input('please enter miles:'))
k=m//1.6  #floor division operator:divides and return int
print(str(m)+' miles is '+str(k)+' kilometers')
'''

#fizzbuzz
vals=[]
n=1
max_num=int(input('maximum number: '))
while n<max_num+1:
    vals.append(n)
    n+=1
print(vals)

for i in range(max_num+1):
    print (i)
    if i % 2 == 0:
        continue
    if i%3==0 and i%5==0:
        print('Fizzbuzz')
        continue
    if i%3==0:
        print('Fizz')

    elif i%5==0:
        print('Buzz')


    else :
       print('not EVEN OR divisible by 3 or 5')



