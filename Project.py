from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions


#~~~~~Main~~~~~~#
def main():
    # x = Arrays.New_Array(1, 2, 6, 4, 5)

    # print(Arrays.Index(x, 6))

    list2 = ["a", 1, "B", 2]
    #print("enter supper")
    list2=String.Is_upper(list2)
    print(list2)
    def body(x):
        nonlocal list2
        if not isinstance(x, int):
            list2.remove(x)
            print(x)

        return

    def func(x):
        nonlocal list
        if(x%2==0):
            list.append(x)

    list = ["Lidor","Ron","Tom"]
    #Loops.ForInRange(0, 1, 1, String.Is_upper)
    #print(list)
    Loops.For(list,String.Is_upper)
    print(list)
    print("awsfdggjhjjhgdf")


if __name__ == '__main__':
    main()
