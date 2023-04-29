def max(arr):
    temp = arr[0]
    for i in arr:
        if(i > temp):
            temp = i
    return temp

if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())

    grades = []
    for x in array:
        if x not in grades:
            grades.append(x)
   
    maxGrade = max(grades)
    grades.remove(maxGrade)
    print(max(grades))
        
        
