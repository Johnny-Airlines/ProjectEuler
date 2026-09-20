-- Reverses the digits of an Int written in base 10
reversed :: Int -> Int
reversed n = go n 0
  where
    go !n !result
      | n > 10 = go q (result * 10 + r)
      | otherwise = result * 10 + n
      where
        (q, r) = n `divMod` 10

-- Checks if a number is a palindrome, in base 10
isPalindrome :: Int -> Bool
isPalindrome n = n == reversed n

-- Largest palidrome from the product of two 3-digit numbers
largePalindrome :: Int
largePalindrome = go 999 999 0
  where
    go !a !b !res
      | a == 100 = res
      -- If b == 100, a*b can not be a palindrome.
      | b == 100 = go (a - 1) (a - 1) res
      | isPalindrome p && res < p = go a (b - 1) p
      | otherwise = go a (b - 1) res
      where
        p = a * b

main = print largePalindrome
