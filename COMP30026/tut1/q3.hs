-- Consider an n by m grid. We want to find out how many different paths there are that one
-- can travel along, starting from the bottom left and ending in the top right cell, given that
-- one can only move up or right. Write a Haskell function
-- paths :: Integer -> Integer -> Integer
-- so that paths m n returns the number of such paths. (We use Integers as the numbers can
-- get quite large.)


paths :: Integer -> Integer -> Integer
paths 1 1 = 1
paths m 1 = 1
paths 1 n = 1
paths m n = (paths (m-1) n) + (paths m (n-1))


-- Linear solution (via combinatorics)?
-- Essentially m+n choose n is equivalent to the solution

paths' :: Integer -> Integer -> Integer
paths' 1 1 = 1
paths' m n = (length * m-1) + (length * n-1)
	where length = (m-1 + n-1)

-- Essentially we can only go up n-1 times and right m-1 times
-- This results in m + n - 1 for the length of the path
-- This will eventually be equivalent to
-- m+n-2 choose n-1 which equals m+n-2 choose m-1