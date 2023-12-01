## problem 1 advent of code 2023
f = open("input.txt","r")



def main ():
    words = f.readlines()
    total = 0
    for index, value in enumerate(words):
        nums = []
        print(index, value)
        for char in value:
            if char.isdigit(): 
                nums.append(char)
        nums = (int(nums[0] + nums[-1]))
        total += nums
    print(total)
    

if __name__ == "__main__":
    main()