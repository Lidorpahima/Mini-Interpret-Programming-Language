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

    def body(x):
        nonlocal list2
        if not isinstance(x, int):
            list2.append(x)
        return

    # Loops.ForInRange(0, 10, 1, body)
    # print(list)
    Loops.For(list2, body)
    print(list2)
    print("awsfdggjhjjhgdf")


if __name__ == '__main__':
    main()
