student = {'name': 'Daniel',
           'last_name': 'Ruiz',
           'height': 1.73,
           'age': 43}

school = {'groups': {'A': {'students':
                             {'danielRuiz': student,
                              'jorgeGomez': {

                              },
                              }},
                     'B': {}
                    }
          }

print('name' in student.keys())
print(student.values())
name_var = student.pop('weight', "doesn't exist")
print(name_var)
print(student)

# for each in my_dictionary:
#     print(each, my_dictionary[each])
