def calc_averagetemperature(num_list):
    total = 0
    y = 0
    for items in num_list:
        total += items
        y +=1
    average = total/y
    #print(average)
    return(average)

def calc_min_max_temperature(num_list):
    x = num_list[0]
    i = 0

    for items in num_list:
        if (x<num_list[i]):
           x =  num_list[i]
        else:
            i+=1
    #print(x)

    z= max(num_list)
    print(z)

    y = min(num_list)
    print(y)

    list = (int(z),int(y))

    return(list)


def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67,32): ")
    return

def get_user_input():
    num_string = input()
    num_list = num_string.split(",")
    num_list = [float(item) for item in num_list]


    return(num_list)

def main():
    print("ET0735 (DevOps for AIOT) - Lab 2 -Introduction of Python")
    display_main_menu()
    num_list= get_user_input()
    print(calc_averagetemperature(num_list))
    print(calc_min_max_temperature(num_list))


if __name__ == "__main__":
    main()