import sys, time
import characters
import fighting_logic

def slow_print(string_to_print):
    for letter in string_to_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
    print(" ")

def fast_print(string_to_print):
    for letter in string_to_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.01)
    print(" ")




def run_game():
    from characters import enemy_one
    print("-------------------")
    slow_print("Pogi wakes up and the room is dark...")
    slow_print("...                                         ")
    print("*Thunder and lightning strike* ")
    slow_print("Pogi panics and realizes his dad is missing...")
    print(f'*Thunder and lightning strike again* {enemy_one["name"]} appears...')
    slow_print("Pogi slowly approches")
    slow_print(f'{enemy_one["name"]} : I know what you are thinking, Pogi. Your dad has met his fate. Are you really prepared to challenge fate?')
    print(f'Pogi challenges {enemy_one["name"]}')




    
run_game()






























