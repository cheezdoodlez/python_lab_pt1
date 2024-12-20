#=================================

# const getName = () => {
#   let name = prompt("what is your name?");
#   return name;
# };

get_name = input("what is your name?")
print('Hi'+ get_name)



#=============================================
# const reverseIt = () => {
#   let string = "a man, a plan, a canal, frenemies!";

#   let reverse = "";

#   for (let i=0; i < string.length; i++) {
#     reverse += string[string.length - (i+1)];
#   };

#   alert(reverse);
# };
def reverse_it():
    string = "a man, a plan, a canal, frenemies!"
    reverse = ''
    for i in range(len(string)):
        reverse += string[len(string)- (i +1)]
    print(reverse)
reverse_it()

#=============================================
# const swapEm = () => {
#   let a = 10;
#   let b = 30;
#   let temp;

#   temp = b;
#   b = a;
#   a = temp;

#   alert("a is now " + a + ", and b is now " + b);
# };


def swap_em():
    a = 10
    b = 30
    a, b = b, a 
    print(f'variable a is now {a} and variable b is now {b}') # the f is formatted string literal which lets you enclose variables in curly braces. like ${} in js
swap_em()

#==============================================
# const multiplyArray = (ary) => {
#   if (ary.length == 0) { return 1; };

#   let total = 1;
#   // let total = ary[0];

#   for (let i=0; i < ary.length; i++) {
#     total = total * ary[i];
#   };

#   return total;
# };

def multiply_array(ary):
    if len(ary) == 0:
        return 1

    total = 1
    for num in ary:
        total *= num

    return total
result = multiply_array([1, 2, 3, 4])
print(result)


#=============================================
# const fizzbuzzer = (x) => {
#   if( x%(3*5) == 0 ) {
#     return 'fizzbuzz'
#   } else if( x%3 == 0 ) {
#     return 'fizz'
#   } else if ( x%5 == 0 ) {
#     return 'buzz'
#   } else {
#     return 'archer'
#   }
# }
def fizzbuzzer(x):
    if x % (3 * 5) == 0:
        return 'fizzbuzz'
    elif x % 3 == 0:
        return 'fizz'
    elif x % 5 == 0:
        return 'buzz'
    else:
        return 'archer'
print(fizzbuzzer(15))  # Output: 'fizzbuzz'
print(fizzbuzzer(9))   # Output: 'fizz'
print(fizzbuzzer(10))  # Output: 'buzz'
print(fizzbuzzer(7))   # Output: 'archer'


#============================================
# const nthFibonacciNumber = () => {
#   let fibs = [1, 1];
#   let num = prompt("which fibonacci number do you want?");

#   while (fibs.length < parseInt(num)) {
#     let length = fibs.length;
#     let nextFib = fibs[length - 2] + fibs[length - 1];
#     fibs.push(nextFib);
#   }

#   alert(fibs[fibs.length - 1] + " is the fibonacci number at position " + num);
# };

def nth_fibonacci_number():
    fibs = [1, 1]
    num = int(input("Which Fibonacci number do you want? "))

    while len(fibs) < num:
        next_fib = fibs[-2] + fibs[-1]
        fibs.append(next_fib)

    print(f"{fibs[-1]} is the Fibonacci number at position {num}")
    
nth_fibonacci_number()




#============================================
# const searchArray = (array, value) => {
#   for(let i = 0; i < array.length-1; i++) {
#     if(array[i] == value) {
#       return true;
#       break;
#     }
#   }
#   return -1;
# };




def search_array(array, value):
    for item in array:
        if item == value:
            return True
    return False

print(search_array([1, 2, 3, 4, 5], 3))  # Output should be true
print(search_array([1, 2, 3, 4, 5], 6))  # Output should be false




#=========================================
# const isPalindrome = (str) => {
#   for(let i = 0; i < str.length/2; i++){
#     if(str[i] != str[str.length-i-1]){
#       return false;
#       break;
#     }
#   }
#   return true;
# }; 


def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True
print(is_palindrome("racecar"))  # Output: True
print(is_palindrome("hello")) 



#==========================================
# const hasDupes = (arr) => {
#   let obj = {};
#   for (i = 0; i < arr.length; i++) {
#     if(obj[arr[i]]) {
#       return true;
#     }
#     else {
#       obj[arr[i]] = true;
#     }
#   }
#   return false;
# };

def has_dupes(arr):
    seen = {}
    for item in arr:
        if item in seen:
            return True
        seen[item] = True
    return False
print(has_dupes([1, 2, 3, 4, 5]))  # Output: False
print(has_dupes([1, 2, 3, 4, 5, 3]))  # Output: True

    