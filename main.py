new_member = input('Please add a new member, write both their name and surname: ') + "\n"

file = open('members.txt', 'r')
data = file.readlines()
file.close()
data.append(new_member)
file = open('members.txt', 'w')
data = file.writelines(data)
file.close()

