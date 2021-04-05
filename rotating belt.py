def rotating_belt(n_obj,list_obj,target_obj):
    if n_obj<100 and n_obj>0:
        for objs in range(len(list_obj)):
            if list_obj[objs]==target_obj:
                break

    min_rotations=objs-1

    return min_rotations

my_list=['a','b','c','d','c','f','c',]
target_object='c'
number_of_objects=len(my_list)
minimum_rotations=rotating_belt(number_of_objects,my_list,target_object)
print(minimum_rotations)