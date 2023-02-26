from collections import defaultdict


def main(file):
    friends = defaultdict(lambda: 0)
    inputs = file.readlines()
    initialize_amount(friends, inputs)
    for line in inputs:
        actions = line.strip().split("for")
        actions[0] = actions[0].strip().split(" ")
        spending_amount = int(actions[0][-1])
        friends[actions[0][0]] += spending_amount
        people_on_which_amount_spent = actions[-1].strip().split(",")
        no_of_person = len(people_on_which_amount_spent)
        amount_spent_for_each_person = spending_amount // no_of_person
        update_amount(amount_spent_for_each_person, friends, people_on_which_amount_spent)

    return friends


def final_distribution(friends):
    for friend in friends:
        if friends[friend] < 0:
            print(friend + " gives " + str(abs(friends[friend])))
        else:
            print(friend + " gets " + str(friends[friend]))


def update_amount(amount_spent_for_each_person, friends, people_on_which_amount_spend):
    for person in people_on_which_amount_spend:
        person = person.strip()
        friends[person] -= amount_spent_for_each_person


def initialize_amount(friends, inputs):
    for line in inputs:
        actions = line.strip().split("for")
        list_of_people = actions[-1].strip().split(",")
        for person_name in list_of_people:
            person_name = person_name.strip()
            friends[person_name] = 0


def person_to_person_transaction(friends):
    while len(friends) != 1:
        sorted_friends = sorted(friends.items(), key=lambda x: x[1])
        minimum = min(abs(sorted_friends[-1][1]), abs(sorted_friends[0][1]))
        print(sorted_friends[0][0] + " needs to pay " + str(minimum) + " to " + sorted_friends[-1][0])
        diff = abs(abs(sorted_friends[-1][1]) - abs(sorted_friends[0][1]))

        if abs(sorted_friends[-1][1]) == minimum:
            friends.pop(sorted_friends[-1][0])
            friends[sorted_friends[0][0]] = diff
        else:
            friends[sorted_friends[-1][0]] = diff
            friends.pop(sorted_friends[0][0])


if __name__ == "__main__":
    file = open('/Users/preeti.priya/Projects/Data Assignment/sample.txt', 'r')
    friends = main(file)
    final_distribution(friends)
    person_to_person_transaction(friends)
