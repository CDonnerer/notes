-- Day 1 of AoC

readInt :: String -> Int
readInt = read

partOne :: [Int] -> Int
partOne xs = head [x*y | x <- xs, y <- xs, x+y == 2020]

partTwo :: [Int] -> Int
partTwo xs = head [x*y*z | x <- xs, y <- xs, z <- xs, x+y+z == 2020]

main = do
    let file = "data/day1.data"
    contents <- readFile file
    let expenses = map readInt (words contents)
    print (partOne expenses)
    print (partTwo expenses)

