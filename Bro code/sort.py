# sort() method = used with lists
# sorted() function = used with iterables

students = ["squidward", "sandy", "patrick", "spongebob", "mr.krabs"]
students.sort(reverse=True)

for i in students:
    print(i)
print()
studentsTuple = ("squidward", "sandy", "patrick", "spongebob", "mr.krabs")
sorted_students = sorted(students)

for i in sorted_students:
    print(i)
print()
studentsListofTuples = [("squidward",   "B", 60),
                        ("sandy",       "A", 33),
                        ("patrick",     "F", 36),
                        ("spongebob",   "D", 20),
                        ("mr.krabs",    "C", 78)]

keyArgument = lambda tuple:tuple[1]
studentsListofTuples.sort(key=keyArgument, reverse=True)    # keyArgument is a function object via the lambda 
for i in studentsListofTuples:                              # function it's as if we'd be putting the entire 
    print(i)                                                # tuple as a key, but lambda function allows us to
                                                            # filter only the grade from that tuple which makes
                                                            # it to work as a key argument
print()
studentsTupleOfTuples = (("squidward",   "B", 60),
                        ("sandy",       "A", 33),
                        ("patrick",     "F", 36),
                        ("spongebob",   "D", 20),
                        ("mr.krabs",    "C", 78))      

age = lambda student:student[1]
sortedTupleOfStudents = sorted(studentsTupleOfTuples, key = age, reverse=True)                                                  

for i in sortedTupleOfStudents:
    print(i)