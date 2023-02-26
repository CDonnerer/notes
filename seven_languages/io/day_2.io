# day 2 of fun with Io.

# 1 fibonacci

fib := method(n, if(n==1 or n==2, 1, fib(n-1) + fib(n-2)))

for(i, 1, 10, fib(i) println)

# 2 change / to return 0

origDiv := Number getSlot("/")
Number / := method (i, 
    if (i!=0, self origDiv(i), 0)
)

"5 / 0 = " println
5 / 0 println

# 3 sum over 2d list

List twodsum := method(
    sum := 0
    self foreach(list, sum := sum + list sum)
    sum
)

"list(list(1,1)) sum" println
list(list(1,1)) twodsum println


# 4 average

List myAverage := method(
  sum := self sum
  sum / self size
)

# list(1, 2) myAverage
"list(1, 2) myAverage" println
list(1, 2) myAverage println

# 5 prototype for 2d list

TwoDList := Object clone



