from Library import Arrays
from Library import Loops
from Library import Math
from Library import String
from Library import Tuples
from Library import Conditions
from Library import Lexer


# ~~~~~Main~~~~~~#
def main():
    arr = Arrays.New_Array(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    strArr= Arrays.New_Array("Ron","Lidor","Avi","Moshe")
    str2Arr = Arrays.New_Array("abcdefg")
    print(arr)
    print(f"arr len ={Arrays.Length(arr)}") #עד פה עובד
    print(f"strArr len ={Arrays.Length(strArr)}")
    print(f"str2Arr len ={Arrays.Length(str2Arr)}")#עד פה עובד
    print(f"value 1 in Index arr = {Arrays.GetIndex(arr, 1)}")
    print(f"value 3 in Index  = {Arrays.GetIndex(arr, 3)}")
    print(f"value 10 in Index  = {Arrays.GetIndex(arr, 10)}")
    Arrays.Append(arr, 11)
    print(f" append arr 11 => {arr}") #קודם לבצע את הפונקציה אחר כך להדפיס כדי להמנע מNone
    print(f" arr value Array i=2 => {Arrays.GetValue(arr, 2)}")
    Arrays.add(arr, 11, 22)
    print(f" add arr 22 in new index (11) => {arr}")
    print(f" add arr 24 in index 0 => {Arrays.add(arr, 0, 24)}")
    print(f" remove arr -1 in index 11 => {Arrays.Remove(arr, -1)}")
    print(String.Is_upper(123))
if __name__ == '__main__':
    main()
