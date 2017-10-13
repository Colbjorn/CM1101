def call_health(health, maxhealth):
    print('HP: [' + '#'*int(health/5) + ' '*int((maxhealth-health)/5) + ']' + ' ' + str(health) + '/' + str(maxhealth))


def call_mana(mana, maxmana):
    print('MP: [' + 'O' * int(mana/5) + ' ' * int((maxmana - mana)/5) + ']' + ' ' + str(
        mana) + '/' + str(maxmana))


def call_stats(health, maxhealth, mana, maxmana):
    call_health(health, maxhealth)
    call_mana(mana, maxmana)

call_stats(57, 100, 15, 20)