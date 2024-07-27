from Library import Arrays, Loops, Math, String
    #~~~~~Main~~~~~~#
def main():
    new_array = Arrays.New_Array()
    Arrays.Append(new_array,5)
    Arrays.Append(new_array, 52)
    Arrays.Append(new_array, 2)
    Arrays.Append(new_array, 4)
    Arrays.Length(new_array)
    print(Arrays.Add(new_array,1,8))
    print("CHECK")
    print(new_array)
    print(Arrays.Remove(new_array,-1))

if __name__ == '__main__':
    main()