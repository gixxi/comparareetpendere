def quicksort(tuple):
        if len(tuple) < 2:
            return tuple
        else:
            x = tuple[0]
            xs = tuple[1:]
            smallerSorted = quicksort(list(filter(lambda elem:elem<=x, xs)))
            biggerSorted = quicksort(list(filter(lambda elem:elem>x, xs)))            
            return smallerSorted + list((x,)) + biggerSorted

if __name__ == "__main__":
    print(quicksort((10, 0, 0, -1, -2, 4, 4, 7, 4, 1, 100, -1000)))