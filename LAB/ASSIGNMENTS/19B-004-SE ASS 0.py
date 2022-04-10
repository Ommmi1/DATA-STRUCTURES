#TASK 1
def Multiple(number):
    total = 0
    for i in range(number):

        if i % 3 == 0 or i % 5 == 0:
            print(i)
            total += i
            print("total number is: ",total)

Multiple(1000)


#TASK 3
def SplitandJoin(string):
    splitting=string.split()
    print( "-".join(splitting))

SplitandJoin("this is a string")


#TASK 4
def LongestWord(word):
    punctuation=("!@#$%^&*_-:?.<<>,+")
    for i in punctuation:
        if i in word:
            word = word.replace(i,' ')
        else:
            continue
    return max(word.split())
word = "fun&!!&time&#+"
print(LongestWord(word))



#TASK 5
def RunnerUp(lst):
    lst2 = []
    for i in lst:
        if i not in lst2:
            lst2.append(i)
    
    
    return lst2[-2]
lst = [2,4,4,4,6,7,7,9]
lst.sort()
x = RunnerUp(lst)
print(x)

#TASK 2
def process(num, index):
    ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')
    twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')
    tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')
    suffixes = ('', 'Thousand', 'Million', 'Billion')
    
    if num=='0':
        return 'Zero'
    
    length = len(num)
    
    if(length > 3):
        return False
    
    num =  num.zfill(3)
    words = ''
 
    hdigit = int(num[0])
    tdigit = int(num[1])
    odigit = int(num[2])
    
    words += '' if num[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''
    
    if(tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]
    
    elif(tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]
        
    elif(tdigit == 0):
        words += ones[odigit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '
     
    if(not len(words) == 0):    
        words += suffixes[index]
        
    return words
    
def InWords( num):
    length = len(str( num))
    
    if length>12:
        return 'This program supports upto 12 digit numbers.'
    
    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []



    
    for i in range(length - 1, -1, -3):

        words.append(process(str(num)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))

        count -= 1

    final_words = ''

    for s in reversed(words):

        temp = s + ' '
        final_words += temp
    
    return final_words

print(InWords(10))