conv_nums = {"one" : 1.8, "two": 1.4, "four" :.6, "five" : .2}
one_weight, two_weight, three_weight, four_weight, five_weight = 1
def found(input_num, one, two, three, four, five):
    lower_bound = .98
    upper_bound = 1.02
    total_agg = one + two + three + four + five
    score = two * 1.2 + three + four * .8 + one * one_weight + five * five_weight
    if(input_num == "one"):
        if(score > 1.25 and score < 1.4):
            return 1
        if(score < 1.25):
            conv_nums["one"] =  conv_nums["one"] + .01
        else:
            conv_nums["one"] =  conv_nums["one"] - .01
    elif(input_num == "two"):
        if(score < 1.25 and score > 1.1):
            return 1
        if(score < 1.1):
            conv_nums["two"] =  conv_nums["two"] + .01
        else:
            conv_nums["two"] =  conv_nums["two"] - .01
    elif(input_num == "four"):
        if(score < 1.2  and score > 1):
            return 1
        if(score < 1):
            conv_nums["four"] =  conv_nums["four"] + .01
        else:
            conv_nums["four"] =  conv_nums["four"] - .01
    else:
        if(score > lower_bound and score < upper_bound):
            return 1
        elif(score > lower_bound):
            conv_nums["five"] =  conv_nums["five"] - .01
        else:
            conv_nums["five"] =  conv_nums["five"] + .01
            
    return score

def opt_app(num_in,  one_count, two_count, three_count, four_count, five_count):
    convergance = 100
    while(convergance != 1):
        print("Starting: ", num_in, "with weight: ",  conv_nums[num_in])
        convergance = found(num_in, one_count, two_count, three_count, four_count, five_count) 
    return 



def converge(one, two, three, four, five):
    #NP HARD search problem, use approximation alg for covergance
    one_weight = 1.3
    two_weight = 1.1
    three_weight = 1
    four_weight = .9
    five_weight = .7

   
    #find optimal one_weight
    opt_app(one, one, two, three, four, five)
    opt_app(four, one, two, three, four, five)
    opt_app(two, one, two, three, four, five)
    opt_app(five, one, two, three, four, five)
   
    


def main():
    #Calculate score weight
    one_count = input("How many 1's are in this catagory?")
    two_count = input("How many 2's are in this catagory?")
    three_count = input("How many 3's are in this catagory?")
    four_count = input("How many 4's are in this catagory?")
    five_count = input("How many 5's are in this catagory?")
    converge(one_count, two_count, three_count, four_count, five_count)
    print("Results:")
    print("One weight: ", one_weight)
    print("Two weight: ", two_weight)
    print("Three weight: ", three_weight)
    print("Four weight: ", four_weight)
    print("Five weight: ", five_weight)



if __name__ == "__main__":
    main()