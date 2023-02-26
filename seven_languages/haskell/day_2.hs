module Foo where
    my_sort :: [Integer] -> [Integer]
    my_sort [] = []
    my_sort [h] = [h]    
    my_sort (h:t) = if h > head(t) then head(t):swap_sort(h:tail(t)) else h:swap_sort(t)

    swap_sort :: [Integer] -> [Integer]
    swap_sort [] = []
    swap_sort [h] = [h]
    swap_sort (h:t) = if h > head(t) then head(t):my_sort(h:tail(t)) else h:my_sort(t)
    
