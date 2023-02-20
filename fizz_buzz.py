class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        arr = [0] * n
        for i in range(n):
            arr[i] = repr(i+1)
        for i in range(len(arr)):
            if (int(arr[i]) % 3 == 0) and (int(arr[i]) % 5 == 0):
                arr[i] = 'FizzBuzz'
            elif (int(arr[i]) % 3 == 0):
                arr[i] = 'Fizz'
            elif (int(arr[i]) % 5 == 0):
                arr[i] = 'Buzz'
        return arr