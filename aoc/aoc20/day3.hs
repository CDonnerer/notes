-- Day 2 of AoC

readInt :: String -> Int
readInt = read

countOcc :: (Eq a) => a -> [a] -> Int
countOcc a [] = 0
countOcc a (x:xs) = (if a == x then 1 else 0) + (countOcc a xs)

split :: String -> Char -> [String]
split [] delim = [""]
split (c:cs) delim
    | c == delim = "" : rest
    | otherwise = (c : head rest) : tail rest
    where
        rest = split cs delim

checkValid :: [String] -> Bool
checkValid tokens = do
    let range = map readInt (split (head tokens) '-')
    let occs = countOcc (checkChar tokens) (takePass tokens)
    if occs >= (head $ take 1 range) && occs <= (head $ drop 1 range) then True else False

countValid :: ([String] -> Bool) -> [String] -> Int
countValid func [] = 0
countValid func a = (if func (take 3 a) then 1 else 0) + (countValid func (drop 3 a))

takeChar :: Int -> String -> Char
takeChar pos str = head $ drop (pos - 1) str

takePass :: [String] -> String
takePass tokens = (head (tail (tail tokens)))

checkChar :: [String] -> Char
checkChar tokens = takeChar 1 $ (head (tail tokens))

checkValidTwo :: [String] -> Bool
checkValidTwo tokens = do
    let positions = map readInt (split (head tokens) '-')
    let check_one = head positions
    let check_two = head $ tail positions
    let char_check = checkChar tokens
    if ((takeChar check_one (takePass tokens)) == char_check) /=
       ((takeChar check_two (takePass tokens)) == char_check)
       then True else False

main = do
    let file = "data/day3.data"
    contents <- readFile file
    print (words contents)
    --print (countValid checkValid (words contents))
    --print (countValid checkValidTwo (words contents))
