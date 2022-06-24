import enum


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
                'title':'batman: the dark knight',
                'genre':'Action'           
            },
            {
               'title':'spiderman no way home',
               'genre':'Superhero' 
            }

         ]
    }
    
    new_movie = {'title': 'black panther','genre' : 'Science-Fiction'}
    student_info['movies'].append(new_movie)

    new_toppings = ('SAUSAGE', 'Mushroom', 'Bacon')
    add_pizza_to_info(student_info, new_toppings)
    
    print_student_info(student_info)
    print_pizza(student_info)   
    print_sentence(student_info)
    print_sentence2(student_info)

def add_pizza_to_info(info, new_toppings):

    info['pizza_toppings'].extend(new_toppings)

    for i,p in enumerate(info['pizza_toppings']):
        info['pizza_toppings'][i] = p.lower()
    
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

def print_sentence(info):
        
    print(f"I like to watch ", end='')
    movie_genre = ''
    for g in info['movies']:
        movie_genre += g['genre'] + ', '
    print(movie_genre[:-17] + ' and ' + movie_genre[-17:] ,end=' Movies.\n\n')
    

def print_sentence2(info):
    
   print(f"Some of my favourite movies are", end=' ')
   movie_title = ''
   for g in info['movies']:
       movie_title += g['title'].title() + ', '
   print(movie_title[:-2], end='!\n\n')



    

main()