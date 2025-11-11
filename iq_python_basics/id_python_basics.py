# You have an array of integers, nums of length n spanning 0 to n with one missing. Write a function missing_number that returns the missing number in the array.

# Note: Complexity of 
# O
# (
# n
# )
# O(n) required.

# Example:

# Input:

# nums = [0,1,2,4,5] 
# missing_number(nums) -> 3

nums = [0,1,2,4,5] 
nums1 = []
first_num = nums[0]
final_num = nums[-1]
n_nums = [num for num in range(first_num, final_num +1)]
for n_num in n_nums:
  if n_num not in nums: print(n_num)






def missing_number(nums):
  nums1 = []
  first_num = nums[0]
  final_num = nums[-1]
  n_nums = [num for num in range(first_num, final_num +1)]
  for n_num in n_nums:
    if n_num not in nums: return n_num
    
A= [-1, 0, 1, 2, 3, 5, 6]
missing_number(A)


# Write a function called find_bigrams that takes a sentence or paragraph of strings and returns a list of all its bigrams in order.

# Note: A bigram is a pair of consecutive words.

# Example:

# Input:

sentence = """
Have free hours and love children? 
Drive kids to school, soccer practice 
and other activities.
"""
A = sentence.split(" ")
[a.strip() for a in A]
# Output:

# def find_bigrams(sentence) ->

#  [('have', 'free'),
#  ('free', 'hours'),
#  ('hours', 'and'),
#  ('and', 'love'),
#  ('love', 'children?'),
#  ('children?', 'drive'),
#  ('drive', 'kids'),
#  ('kids', 'to'),
#  ('to', 'school,'),
#  ('school,', 'soccer'),
#  ('soccer', 'practice'),
#  ('practice', 'and'),
#  ('and', 'other'),
#  ('other', 'activities.')]

  

def find_bigrams(sentence):
  new_list = []
  sentence_list = sentence.split(" ")
  sentence_list = [word.strip().lower() for word in sentence_list if word != ""]
  for i in range(len(sentence_list)):
    if i + 1 < len(sentence_list):
      new_list.append((sentence_list[i], sentence_list[i+1]))
      
  return new_list



find_bigrams("Hi Mehdi")
find_bigrams(sentence)

sentence_1 = "need someone to talk to? I am here  ...   My      best friend."
sentence_1.split(" ").remove("")
find_bigrams(sentence_1)

# Given two sorted lists, write a function to merge them into one sorted list.

# Bonus: What’s the time complexity?

# Example:

# Input:

# list1 = [1,2,5]
# list2 = [2,4,6]
# Output:

# def merge_list(list1,list2) -> [1,2,2,4,5,6]


list1 = [1,2,5]
list2 = [2,4,6]

sorted(list1 + list2)

def merge_list(list1, list2):
  return sorted(list1+list2)

merge_list(list1, list2)

# Given a string str, write a function perm_palindrome to determine whether there exists a permutation of str that is a palindrome.

# Example:

# Input:

# str = 'cacerra'
# def perm_palindrome(str) -> True
# “cacerra” returns True since it can be rearranged to form “racecar” which is a palindrome.
str = 'cacerra'
len(str)
if len(str) % 2 == 1:
  let_list = [let for let in str]
  
sorted(let_list)

odd_in_list= []
for i in range(len(let_list)):
  if let_list.count(let_list[i])%2 == 0:
    odd_in_list.append(0)
  else:
    odd_in_list.append(1)

if sum(odd_in_list)%2 == 1:
  True    
  
if len(str) % 2 == 0:
  let_list = [let for let in str]
  
sorted(let_list)

even_in_list= []
for i in range(len(let_list)):
  if let_list.count(let_list[i])%2 == 0:
    odd_in_list.append(0)
  else:
    odd_in_list.append(1)

if sum(odd_in_list)%2 == 1:
  False   

    
def perm_palindrome(str):
  let_list = [let for let in str]
  len_list = len(let_list)
  in_list= []
  for i in range(len(let_list)):
    in_list.append(let_list.count(let_list[i]))
  if len_list % 2 == 1:
    let_list1 = [let for let in in_list if let%2 == 1]
    if len(let_list1)>1 or len(let_list1)==0:
      return False
    else:
      return True
  else:
    let_list1 = [let for let in in_list if let%2 == 1]
    if len(let_list1) == 0:
      return True
    else:
      return False
    
    
        
# Given a list of integers, find the index at which the sum of the left half of the list is equal to the right half.

# If there is no index where this condition is satisfied return -1.

# Example 1:

# Input:

# nums = [1, 7, 3, 5, 6]
# Output:

# equivalent_index(nums) -> 2
# Example 2:

# Input:

# nums = [1,3,5]
# Output:

# equivalent_index(nums) -> -1  

my_list = []

list_to_sum = []
help_list = my_list.copy()
for i in range(len(my_list)):
  list_to_sum.append(my_list[i])
  help_list.remove(help_list[i])
  if sum(help_list) == sum(list_to_sum):
    print(i) 
    break
else:
  print("-1")
  
  
  
def equivalent_index(nums):
  list_to_sum = []
  help_list = nums.copy()
  for i in range(len(nums)):
    list_to_sum.append(nums[i])
    help_list.remove(nums[i])
    if sum(help_list) == sum(list_to_sum):
      return i
      break
  else:
    return -1
  
  
nums = [2, 27, 29]
equivalent_index(nums) 
  
  
  

