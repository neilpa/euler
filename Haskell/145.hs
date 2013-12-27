-- How many reversible numbers are there below one-billion?
-- Problem 145
--
-- Some positive integers n have the property that the sum [ n + reverse(n) ] consists
-- entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313.
-- We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading
-- zeroes are not allowed in either n or reverse(n).
--
-- There are 120 reversible numbers below one-thousand.
--
-- How many reversible numbers are there below one-billion (10^9)?

import Data.Char

rev :: Integer -> Integer
rev n = read $ reverse $ show n

oddDigits :: Integer -> Bool
oddDigits n = all odd $ map digitToInt $ show n

-- TODO - ugh this is slower than I expected
-- Generates all odd numbers for each power of 10 that start with an even digit
possible = concat [ [ (d * 10^e)+1, (d * 10^e)+3 .. ((d+1) * 10^e)-1 ] | d <- [2,4,6,8], e <- [0..6] ]

p145 = filter (\x -> oddDigits $ (rev x) + x) possible

