sumSquares :: [Int] -> Int
sumSquares nums = go 0 nums
  where
    go result nums
      | nums == [] = result
      | otherwise = go (result + ((nums !! 0) ^ 2)) (drop 1 nums)

main = print (((sum [1 .. 100]) ^ 2) - (sumSquares [1 .. 100]))
