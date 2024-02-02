import random
import timeit

from bubblesort import bubble_sort
from binarysearch import binary_search

def generate_data(size=10, max=100):
    return [ random.randint(0,max) for _ in range(size) ]

def main():
    data = generate_data(100,1000)
    print(data)
    
    
    time_start = timeit.default_timer()
    sorted_data=bubble_sort(data)
    print(timeit.default_timer()-time_start)
    print(sorted_data)
    
    while True:
        try:
            x = int(input())
        except:
            print("not a number")
            continue
        else:
            break
    
    try:
        time_start = timeit.default_timer()
        wynik = binary_search(sorted_data,x)
        print(timeit.default_timer()-time_start)
        print(wynik)
        
    except:
        print("not in the array")
    
    

if __name__ == "__main__":
    main()