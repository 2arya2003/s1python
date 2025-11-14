str1="hello"
str2="world"
str1_new=str1[0]+str2[1]+str1[2:]
str2_new=str2[0]+str1[1]+str2[2:]
result=str1_new+""+str2_new
print(result)