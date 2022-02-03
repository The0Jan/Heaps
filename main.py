from kopce import Heap
import matplotlib.pyplot as plt
import timeit
import numpy as  np

#creates one single array of elements from which later smaller parts are used in the test
def get_numbers(amount= 100,low= 1 , high= 3000):
    array = []
    for i in range(amount):
        array.append(np.random.randint(low , high))
    return array

#used for taking a smaller array of the big array for the tests
def get_sub_array(amount, array=[]):
    sub_array = []
    for i in array:
        sub_array.append(i)
        amount = amount -1
        if amount == 0:
            return sub_array

# used for drawing the results for multiple functions,methods, etc.
def draw_multi_results(colors =[], *args):
    index = 0
    for containers in args:
        plt.plot(containers[0], containers[1], color = colors[index], label = "Heap_nary:" + str(containers[2]))
        index +=  1
    plt.legend()
    plt.ylabel("Time[s]")
    plt.xlabel("Amount of words")
    plt.title("Multiple results graph")
    plt.show
    plt.savefig("various_results.png")
    plt.close()

#function for drawing a graph
def draw_graph(times, amount, title, color = "blue"):
    y = times
    x = amount
    plt.plot(x, y, color)
    plt.ylabel("Time[s]")
    plt.xlabel("Amount of words")
    plt.title(title)
    plt.show
    plt.savefig(title + ".png")
    plt.close()

#function for creating a .txt file with the measurments
def create_file(times, amounts,sort_type, file_name = "results"):
    full_name = file_name + ".txt"
    indexes = len(times)
    with open(full_name, 'a+') as file:
        file.write(sort_type + '\n')
        for  index in range(0,indexes):
            current_amount = amounts[index] 
            current_time  = times[index]
            line = "Numbers given:" + str(current_amount) + '\t' + "Time:" + str(current_time) + '\n'
            file.write(line)

def create_results(ary_type, name_of_sort = ' ',words_bank = [], max = 20000, increment = 500 ):
    amount= 0
    times =[]
    words = []
    print(name_of_sort)
    while amount < max:
        heap_ary = Heap(ary_type)
        amount = amount + increment
        collection = get_sub_array(amount, words_bank)
        time = (timeit.timeit(lambda:heap_ary.add_multiple_ele(collection), number = 100))/100 #average executing time of adding new
        rounded = round(time, 4)
        times.append(rounded)
        words.append(amount)
        print('Amount of numbers:',amount, ' Rounded_time(s):', rounded)
    print("\n ------------- \n")
    #These functions are used for creating the graph and adding the data to the .txt file
    #draw_graph(times, words, name_of_sort)
    #create_file(times, words, name_of_sort)
    return words, times , ary_type


#Create a bank of numbers and taking every time bigger amounts from it note the times.
collection = get_numbers(25000)

results_2 = create_results(2, "Heap_2_nary", collection)
results_3 = create_results(3, "Heap_3_nary", collection)
results_4 = create_results(4, "Heap_4_nary", collection)

#This function is used for the creating of a single graph for all three arrays
#draw_multi_results(["blue", "red", "green"], results_2, results_3, results_4)


