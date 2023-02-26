module Foo where
    reverseList [] = []
    reverseList x  = last x : reverseList(init x)

    twoTuples x = [(a,b) | a <- x, b <- x, a < b]

    multiplicationTable x = [(a,b,a*b) | a <-[1..x], b<-[1..x], a<b]

