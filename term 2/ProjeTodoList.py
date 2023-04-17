do=input("Enter show, add, delete, end: ")
To_Do_list=["job1","job2","job3"]
Time_List=[11,22,33]
Status_list=["start","busy","start"]
print(len(To_Do_list))
while do!="end":
    if do=="show":
        for i in range(len(To_Do_list)):
            print (f"{i+1},{To_Do_list[i]} {Time_List[i]} {Status_list[i]}")
    elif do=="add":
        New_Do=input("Enter sth to add: ")
        To_Do_list.append(New_Do)
        New_Do=input("Enter a time: ")
        Time_List.append(New_Do)
        New_Do=input("Enter a status: start, busy, done: ")
        while New_Do!="start" and New_Do!="busy" and New_Do!="done":
            print("please enter a status!")
            New_Do=input("Enter a status: start, busy, done: ")
        Status_list.append(New_Do)
        print("task added.")
    elif do=="delete":
        delete_item=int(input("enter number of item to delete:"))-1
        while delete_item<0 and len(To_Do_list)<delete_item:
            print("please enter a valid number!")
            delete_item=int(input("enter number of item to delete:"))
        del To_Do_list[delete_item]
        del Time_List[delete_item]
        del Status_list[delete_item]
        print("task deleted!.")

        # To_Do_list.pop(delete_item+1)
        # Time_List.pop(delete_item+1)
        # Status_list.pop(delete_item)

        # Delete_item=input("Enter Item to delete: ")
        # if Delete_item in To_Do_list:
        #     for j in range(len(To_Do_list)):
        #         if Delete_item==To_Do_list[j]:
        #             To_Do_list.pop(j)
        #             Time_List.pop(j)
        #             print(f"item {Delete_item} deleted")
        #             break
        # else:
        #     print("item not found")
    else:
        print("try again!")
    do=input("Enter show, add, delete, end: ")
