def main():
    grocery_list = []
    grocery_list = collect_input()
    sorted_dict = create_dictionary(grocery_list)
    if sorted_dict:
        for item in sorted_dict:
            print(f"{sorted_dict[item]} {item}")
    else:
        print("You don't need to go to the store! You would only buy stupid shit you don't need ;)")

def collect_input():
    grocery_list = []
    while True:
        try:
            item = input().strip().upper()            
        except EOFError:
            return grocery_list
        grocery_list.append(item)
        

def create_dictionary(list):
    unsorted_dict = {}
    for i in list:
        if i in unsorted_dict:
            unsorted_dict[i] += 1
        else:
            unsorted_dict[i] = 1
    sorted_dict = dict(sorted(unsorted_dict.items()))
    return sorted_dict
    

if __name__=="__main__":
    main()