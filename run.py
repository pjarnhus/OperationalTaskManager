from datetime import datetime
import json
import os


def print_card(card_name, goal_name, card_width=60):
    os.system('clear')
    print(' ' + '*'*int(card_width/5))
    for _ in range(2):
        print('*'*card_width)
    print('**' + ' '*(card_width-4) + '**')
    white_space = card_width - 4 - len(card_name)
    left_space = int(white_space/2)
    right_space = white_space - left_space
    print('**' + ' '*left_space + card_name + ' '*right_space + '**')
    print('**' + ' '*(card_width-4) + '**')
    for _ in range(2):
        print('*'*card_width)
    white_space = card_width - 4 - len(goal_name)
    left_space = int(white_space/2)
    right_space = white_space - left_space
    print('**' + ' '*(card_width-4) + '**')
    print('**' + ' '*left_space + goal_name + ' '*right_space + '**')
    print('**' + ' '*(card_width-4) + '**')
    for _ in range(2):
        print('*'*card_width)

def work_on_card(card, failed_previous=False):
    goal_log = []
    work_on_goal = True
    if failed_previous:
        work_on_goal = False
    for goal in card['goals']:
        if work_on_goal:
            print_card(card['name'], goal)
            response = input('Press Enter when complete'
                             + ' or enter reason if not complete: ')
            if response == '':
                goal_log.append(
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    + f',{card["name"]}, {goal},SUCCESS\n')
            else:
                work_on_goal = False
                goal_log.append(
                    str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    + f',{card["name"]}, {goal},FAILED\n')

        else:
            goal_log.append(
                str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                + f',{card["name"]}, {goal},FAILED\n')
    return {'failed_goal': not work_on_goal, 'goal_log': goal_log}


log_file = open('log.csv', 'a')
tasks = json.load(open('tasks.json', 'r'))
failed_previous_card = False
for active_card in sorted(tasks, key=lambda x: x['priority']):
    outcome = work_on_card(active_card, failed_previous_card)
    failed_previous_card = outcome['failed_goal']
    log_file.writelines(outcome['goal_log'])


