class Heap():
    # nary defines the kind of heap we are creating. 2 is a binary heap, 3 is a 3-nary heap and 4 is a 4-nary heap
    # I wasn't sure whether to copy and paste the code three times or stay with a single implementaion that can be used for all three,
    #  so i went with the principle not to copy the code if not needed
    def __init__(self, nary):
        self.heap = []
        self.amount = 0
        self.nary = nary

    def add_element(self, element):
        free_index = self.amount    #the current index 
        self.amount = self.amount + 1   # increment the total amount of knots 
        parent_index = (free_index-1)//self.nary    #count the index of the parent knot
        self.heap.append(element)                   # add the new element and the end of the list
        while (free_index > 0) and self.heap[parent_index] < element: # checks if the father knot is smaller, if yes, change values and calculate new father index,
            self.heap[free_index] = self.heap[parent_index]
            free_index = parent_index
            parent_index = (free_index-1)//self.nary
            if free_index == 0 or self.heap[parent_index] >= element: #if the conditions are meet set the value of the current knot to the value of the element
                self.heap[free_index] = element

    def add_multiple_ele(self, lists =[]): # mass addition function
        for i in lists:
            self.add_element(i)

    def count_levels(self): # used for counting the max level
        amount = self.amount
        levels = 0
        knots_at_level = 1
        while amount > 0:
            amount = amount - knots_at_level
            levels = levels + 1
            knots_at_level = knots_at_level*self.nary
        return levels

    def find_biggest_word(self):
        biggest = 0
        for i in self.heap:
            if len(str(i)) > biggest:
                biggest = len(str(i))
        return biggest

    def show_heap(self):
        longest_word = self.find_biggest_word()
        max_levels = self.count_levels()
        levels = 0 
        knots_at_level = 1
        knot_now =0
        last_knot_of_level = 1
        string = ''
        while knot_now <= self.amount -1:
            if last_knot_of_level == knot_now or knot_now == self.amount -1 :
                knots_at_level = knots_at_level*self.nary
                last_knot_of_level = last_knot_of_level + knots_at_level
                print(string)
                levels = levels +1
                string = ''
            extra_word = longest_word - len(str(self.heap[knot_now]))
            string = string +'-'*(self.nary**(max_levels-levels)-longest_word) +'-'*extra_word+str(self.heap[knot_now])+ '-'*self.nary**(max_levels-levels)
            knot_now = knot_now + 1

    def show_heap_4_nary(self):
        longest_word = self.find_biggest_word()
        max_levels = self.count_levels()
        levels = 0 
        knots_at_level = 1
        knot_now =0
        last_knot_of_level = 1
        string = ''
        while knot_now <= self.amount -1:
            if last_knot_of_level == knot_now or knot_now == self.amount -1 :
                knots_at_level = knots_at_level*self.nary
                last_knot_of_level = last_knot_of_level + knots_at_level
                print(string)
                levels = levels +1
                string = ''
            extra_word = longest_word - len(str(self.heap[knot_now]))
            diferrence_in_levels = max_levels - levels -1
            if diferrence_in_levels <0:
                diferrence_in_levels = 0 
            multiplier = 2*self.nary**(diferrence_in_levels)

            string = string +'-'*(multiplier-longest_word) +'-'*extra_word+str(self.heap[knot_now])+ '-'*multiplier
            knot_now = knot_now + 1


    def print_heap(self): # the show_heap_nary and show_heap_4_nary are little bit different. The second one is used to not take up so much place by the printed lines so they could easier fit in.
        if self.nary == 2:
            return self.show_heap()
        else:
            self.show_heap_4_nary()

# a sample of printing heaps using the functions
"""
heap_2 = Heap(2)
heap_3 = Heap(3)
heap_4 = Heap(4)
for i in range(60):
    heap_2.add_element(i)
for i in range(40):
    heap_3.add_element(i)
for i in range(20):
    heap_4.add_element(i)
print("##################################################################################################################")
print("Binary")
heap_2.print_heap()
print("##################################################################################################################")
print("3_ary")
heap_3.print_heap()
print("##################################################################################################################")
print("4_ary")
heap_4.print_heap()
"""
