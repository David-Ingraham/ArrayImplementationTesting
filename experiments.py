from MyList import *
from progress.bar import Bar  # or choose your favorite
from time import perf_counter
import random

################################################################################
def oneExperiment(min_list_size: int, max_list_size: int) -> 'tuple[int, int, int]':
    ''' function to conduct one experiment by creating a MyList object,
        then appending a random number (between the given min and max values)
        of integers each chosen at random between 1 and 1000 inclusive
    Parameters:
        min_list_size: integer corresponding to the smallest possible MyList
        max_list_size: integer corresponding to the largest possible MyList
    Returns:
        a tuple of post-experiment stats, in order:
            - the length of the MyList (entries, not internal array capacity)
            - the number of array resizes required across all appends
            - the number of array-to-array elements copied across all appends
    '''

    size = random.randint(min_list_size, max_list_size)

    l1 = MyList()

    for i in range(size):
        l1.append(random.randint(1, 1000))



    res: dict = MyList.getStatsDict()

    tup = (res["resizes"], res["copies"], len(l1))


    return tup


    

################################################################################
def main() -> None:
    # you will need to add more code throughout below

    random.seed(8675309)
    num_experiments = 30
    bar = Bar('Processing', max = num_experiments)

    total_resizes = 0
    total_copies = 0
    total_lengthOf_lists = 0

    total_time = 0

    for i in range(num_experiments):
        # conduct one experiment keeping track of the stats to print
        # averages later... remember to time each experiment

        start = perf_counter()
        x: tuple = oneExperiment(100000,999999)
        end = perf_counter()

        elapsed_time = end - start

        total_copies += x[1]
        total_resizes += x[0]
        total_lengthOf_lists += x[2]

        total_time += elapsed_time


        MyList.resetStats()


        bar.next()

    bar.finish()

    print(f'Avgerage copies : {total_copies/ num_experiments} \nAverage resizes : {total_resizes / num_experiments} \nAverage Length of List : {total_lengthOf_lists / num_experiments}  \nAverage Time : {total_time / num_experiments}')

if __name__ == "__main__":
    main()
