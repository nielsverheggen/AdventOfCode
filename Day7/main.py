from collections import Counter
from functools import cmp_to_key

lines = []

with open("input.txt", 'r') as file:
    for line in file:
        lines.append(line)
        
scores = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}

part = 1


def get_type(hand):
    card_frequency = Counter(hand)

    if part == 2 and "J" in hand:
        joker_count = card_frequency["J"]
        del card_frequency["J"]
        if not card_frequency:
            card_frequency["A"] = 5
        else:
            most_common_card, _ = card_frequency.most_common(1)[0]
            card_frequency[most_common_card] += joker_count

    if len(card_frequency) == 1:
        return 7
    if len(card_frequency) == 2:
        if 4 in card_frequency.values():
            return 6
        if 3 in card_frequency.values():
            return 5
    if 3 in card_frequency.values():
        return 4

    if 2 in card_frequency.values():
        pair_count = sum(1 for count in card_frequency.values() if count == 2)
        if pair_count == 2:
            return 3
        else:
            return 2

    return 1


def compare_hands(hand_bundle_1, hand_bundle_2):
    hand1 = hand_bundle_1[0]
    hand2 = hand_bundle_2[0]

    hand1_type = get_type(hand1)
    hand2_type = get_type(hand2)

    if hand1_type > hand2_type:
        return 1
    elif hand2_type > hand1_type:
        return -1

    for card1, card2 in zip(hand1, hand2):
        if scores[card1] > scores[card2]:
            return 1
        elif scores[card2] > scores[card1]:
            return -1

    return 0


hand_bids = []

for hand in lines:
    hand, b = hand.split()
    hand_bids.append((hand, int(b)))


def get_winnings(hand_bids):
    in_order = sorted(hand_bids, key=cmp_to_key(compare_hands))
    total = 0
    rank = 1
    for _, bid in in_order:
        total += bid * rank
        rank += 1
    return total


print(get_winnings(hand_bids))

scores["J"] = 0
part = 2

print(get_winnings(hand_bids))
