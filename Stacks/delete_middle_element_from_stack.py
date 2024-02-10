# Problem Link : https://www.geeksforgeeks.org/delete-middle-element-stack/


st = []
st.insert(0, 1)
st.insert(0, 2)
st.insert(0, 3)
st.insert(0, 4)
st.insert(0, 5)
st.insert(0, 6)
st.insert(0, 7)

n = len(st)
temp = []
count = 0
while count < (n/2)-1:
    top = st[0]
    st.pop(0)
    temp.insert(0,top)
    count+=1
st.pop(0) # deleting middle element

while temp:
    st.insert(0,temp[0])
    temp.pop(0)

print(st)

