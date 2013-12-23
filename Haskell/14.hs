-- Longest Collatz sequence
-- Problem 14
--
-- The following iterative sequence is defined for the set of positive integers:
--
-- n → n/2 (n is even)
-- n → 3n + 1 (n is odd)
--
-- Using the rule above and starting with 13, we generate the following sequence:
--
-- 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
--
-- It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
-- Although it has not been proved yet (Collatz Problem), it is thought that all starting
-- numbers finish at 1.
--
-- Which starting number, under one million, produces the longest chain?
--
-- NOTE: Once the chain starts the terms are allowed to go above one million.

--import Data.HashMap.Strict as HM
--import Data.Maybe



--collatz :: Int -> [Int]
--collatz 1 = [1]
--collatz 2 = [2,1]
--collatz n
--    | even n = n : (collatz $ n `div` 2)
--    | odd n = n : (collatz $ 3 * n + 1)

--collatz :: Int -> Int
--collatz 0 = 0
--collatz 1 = 0
--collatz n
--    | even n = n `div` 2
--    | odd n = 3 * n + 1
--
--collatzLength :: Int -> Int
--collatzLength = (map chain [0..] !!)
--    where chain 0 = 0
--          chain 1 = 1
--          chain n = 1 + collatzLength (collatz n)
--            | even n = 1 + collatzLength (n `div` 2)
--            | odd n = 1 + collatzLength (3 * n + 1)


--chain :: Int -> [(Int, Int)]
--chain n = scanr (\x acc -> (x, snd acc + 1)) (1, 1) (init $ collatz n)
--
--
--collatzLength hm 1 = 1
--collatzLength hm n
--    | value /= Nothing = fromJust value
--    | otherwise = collatzLength hm (head $ tail $ collatz n)
--    where value = HM.lookup n hm
--
--f hm n
--    | HM.lookup n hm /= Nothing = hm
--    | otherwise = HM.union hm $ HM.fromList $ chain n
--
--chains = foldl f HM.empty [999999,999998..0]
--maxChain k v a = if v > snd a then (k, v) else a
--p14 = HM.foldrWithKey maxChain (0, 0) chains

--main = putStrLn (show p14)

