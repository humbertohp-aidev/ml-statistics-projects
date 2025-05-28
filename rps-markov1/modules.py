import random
import numpy as np

#This module validates the selection input
def validate_input():
  while True:
    movement=input('Rock (r), Paper (p) or Scissors (s): ').upper()
    if movement in ['R','P','S', 'Q']:
      return movement
    else:
      print('Invalid input')

#This module updates the matrix counts to construct the probability matrix
def count_movements(prev, current, matrix):
  if prev=='R':
    if current=='R':
      matrix[0][0]+=1
    elif current=='P':
      matrix[0][1]+=1
    elif current=='S':
      matrix[0][2]+=1
  elif prev=='P':
    if current=='R':
      matrix[1][0]+=1
    elif current=='P':
      matrix[1][1]+=1
    elif current=='S':
      matrix[1][2]+=1
  elif prev=='S':
    if current=='R':
      matrix[2][0]+=1
    elif current=='P':
      matrix[2][1]+=1
    elif current=='S':
      matrix[2][2]+=1
  return matrix

#It defines the counter for each movement
counter_attack={
    'R':'P',
    'P':'S',
    'S':'R'
}

#Selection names dictionary
select={
    'R':'Rock',
    'P':'Paper',
    'S':'Scissors'
}

#This module is used to decide the winner of each round based on the player movement and model prediction
def decide_winner(player_move, next_move, player_score, computer_score):
  decision=None
  prediction=counter_attack[next_move]
  if prediction==counter_attack[player_move]:
    computer_score+=1
    decision='Markov wins!!!'
  elif player_move==counter_attack[prediction]:
    player_score+=1
    decision='You win!!!'
  else:
    decision="OMG!!! It's a draw!!!"
  return player_score, computer_score, decision

#This module creates the transition matrix for Markov model and takes control of movements and counts
def rps_markov(movements_list=[], random_test=False):
    random_movements=[]
    number=None
    if random_test:
        while True:
            number=int(input('Enter the lenght of random Movements: '))
            if type(number)==int:
                break
            else:
                print('Invalid input. Try again')
        random_movements=generate_random(number)
    else: print('Welcome to Rock, Paper and Scissors (Enter q to exit):')
    matrix=np.zeros((3,3))
    last_move=''
    next_move=''
    rounds=0
    player_score=0
    computer_score=0
    movement=None
    while True:
        if random_test:
            if rounds<number:
                movement=random_movements[rounds]
            else: break
        else: 
            movement=validate_input()
            if movement=='Q':
                break
        if len(movements_list)<3:
            next_move=np.random.choice(['R','P','S'], p=[1/3,1/3,1/3])
            if not random_movements:
                print(f'You choose: {select[movement]} | Computer choose: {select[counter_attack[next_move]]}')
            player_score, computer_score, decision=decide_winner(movement, next_move, player_score, computer_score)
            movements_list.append(movement)
        else:
            if len(movements_list)==3:
                for i in range(len(movements_list)-1):
                    matrix=count_movements(movements_list[i],movements_list[i+1],matrix)
                last_move=movements_list[-1]

            aux_matrix=matrix.copy()
            for i in range(len(aux_matrix)):
                row_sum=sum(aux_matrix[i])
                aux_matrix[i]=aux_matrix[i]/row_sum if row_sum!=0 else 1/3
            if last_move=='R':
                next_move=np.random.choice(['R','P','S'],p=aux_matrix[0])
            elif last_move=='P':
                next_move=np.random.choice(['R','P','S'],p=aux_matrix[1])
            elif last_move=='S':
                next_move=np.random.choice(['R','P','S'],p=aux_matrix[2])
            if not random_movements:
                print(f'You choose: {select[movement]} | Computer choose: {select[counter_attack[next_move]]}')
            player_score, computer_score, decision=decide_winner(movement, next_move, player_score, computer_score)
            movements_list.append(movement)
            matrix=count_movements(last_move,movement,matrix)
            last_move=movement
        rounds+=1
        if not random_movements:
            print(f'{decision} | Player Score: {round(player_score/rounds*100,2)}% - Computer Score: {round(computer_score/rounds*100,2)}%')
            print('-'*70)
    if random_movements:
        print('-'*50)
        print(f'|   Player Score: {round(player_score/rounds*100,2)}% - Computer Score: {round(computer_score/rounds*100,2)}%   |')
        print('-'*50)

#This module generates a random number of movements
def generate_random(n=100):
    return [random.choice(['R', 'P', 'S']) for _ in range(n)]
