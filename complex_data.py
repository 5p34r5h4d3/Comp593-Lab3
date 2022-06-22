def main():

    student_info = {
        'full_name': 'Benjamin Mathew',
        'student_id': '10254963',
        'pizza_toppings': [
            'Pepperoni',
            'Peppers',
            'Lots of cheese',
        ],
        'movies': [
            {
                'title':'Batman: The Dark Knight',
                'genre':'Action, Superhero'
            },
            {
               'title':'Spiderman No Way Home',
               'genre':'Action, Superhero' 
            }

         ]
    }
    
    new_movie = {'title': 'Black Panther','genre' : 'Action, Science Fiction,Superhero'}
    student_info['movies'].append(new_movie)

    new_toppings = {'Sausage', 'Mushroom','Bacon'}
    add_pizza_to_info(student_info, new_toppings)

    print_student_info(student_info)
    print_pizza(student_info)

def add_pizza_to_info(info, new_toppings):

    info['pizza_toppings'].extend(new_toppings)

    for i,p in enumerate(info['pizza_toppings']):
       info['pizza_toppings'][i] = p.islower()
       
    info['pizza_toppings'].sort()
    
def print_student_info(info):
    sentence = f"My name is { info['full_name'] },but you can call me Captain {info['full_name'].split(' ')[0]}."
    sentence2 = f"My student id is {info['student_id']}"
    print(sentence,sentence2, end='\n\n')

def print_pizza(info):
    header = "My favorite pizza toppings are:"
    print(header)
    print('-' * len(header))

    for p in info['pizza_toppings']:
        print(f"- {p}")
    print()

main()