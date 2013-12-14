-- Largest palindrome product
-- Problem 4

-- A palindromic number reads the same both ways. The largest palindrome made from the product
-- of two 2-digit numbers is 9009 = 91 × 99.

-- Find the largest palindrome made from the product of two 3-digit numbers.

palindrome :: (Eq a) => [a] -> Bool
palindrome xs = xs == reverse xs

numPalindrome :: Int -> Bool
numPalindrome n = palindrome (show n)

products = [ x*y | x <- [100..999], y <- [x..999] ]
p4 = maximum (filter numPalindrome products)

