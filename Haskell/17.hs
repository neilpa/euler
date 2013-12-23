-- Number letter counts
-- Problem 17
--
-- If the numbers 1 to 5 are written out in words: one, two, three, four, five, then
-- there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
--
-- If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
-- how many letters would be used?
--
-- NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
-- contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
-- "and" when writing out numbers is in compliance with British usage.

numToWord 0 = ""
numToWord 1 = "one"
numToWord 2 = "two"
numToWord 3 = "three"
numToWord 4 = "four"
numToWord 5 = "five"
numToWord 6 = "six"
numToWord 7 = "seven"
numToWord 8 = "eight"
numToWord 9 = "nine"
numToWord 10 = "ten"
numToWord 11 = "eleven"
numToWord 12 = "twelve"
numToWord 13 = "thirteen"
numToWord 15 = "fifteen"
numToWord 18 = "eighteen"
numToWord 20 = "twenty"
numToWord 30 = "thirty"
numToWord 40 = "forty"
numToWord 50 = "fifty"
numToWord 60 = "sixty"
numToWord 70 = "seventy"
numToWord 80 = "eighty"
numToWord 90 = "ninety"
numToWord 1000 = "onethousand"
numToWord n
    | n < 20 = numToWord ones  ++ "teen"
    | n < 100 = numToWord (tens * 10) ++ numToWord ones
    | n < 1000 = numToWord (hundreds) ++ "hundred" ++
        if rem /= 0 then "and" ++ numToWord rem else ""
    where ones = n `mod` 10
          tens = n `div` 10 `mod` 10
          rem = n `mod` 100
          hundreds = n `div` 100 `mod` 10

p17 = sum $ map (length.numToWord) [1..1000]

