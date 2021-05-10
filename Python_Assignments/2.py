def count_substring(string,sub_string):
    l=0
    m=string.split(sub_string)
    for x in range(len(m)):
        l+=len(m[x])
    count=(len(string)-l)/len(sub_string)
    print(count)
count_substring('ABSHIZLMSHIZ','HIZ')
