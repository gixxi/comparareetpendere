quicksort :: (Ord a) => [a] -> [a]
quicksort [] = []
quicksort (x:xs) = smallerSorted ++ [x] ++ biggerSorted
	where smallerSorted = quicksort (filter (<=x) xs)
	biggerSorted = quicksort (filter (>x) xs)

print (quicksort [10, 0, 0, -1, -2, 4, 4, 7, 4, 1, 100, -1000])