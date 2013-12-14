-- Problem 2
-- Even Fibonacci numbers
--
-- Each new term in the Fibonacci sequence is generated by adding the previous two terms. By
-- starting with 1 and 2, the first 10 terms will be:
--
-- 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
--
-- By considering the terms in the Fibonacci sequence whose values do not exceed four million,
-- find the sum of the even-valued terms.

-- Normal recursive lame-ness and slow
-- fib 0 = 0
-- fib 1 = 1
-- fib n = fib(n-1) + fib(n-2)

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)
limit = 4 * 10^6

p2 = sum (filter even (takeWhile (<limit) fibs))
