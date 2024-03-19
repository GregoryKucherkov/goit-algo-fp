import random
import matplotlib.pyplot as plt

throws = 1000_000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(throws):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    sum_counts[dice_1 + dice_2] += 1

probabilities = {sum_val: count / throws for sum_val, count in sum_counts.items()}

#print('Sum | Probability')
print(f"| {'Sum':<5} | {'Probability':<5} |")
print(f"| {'-'*5} | {'-'*11} |")
for sum_val, prob in probabilities.items():
    print(f'|{sum_val :4}   | {prob:<11.2%} |')
print(f"| {'-'*5} | {'-'*11} |")


plt.bar(probabilities.keys(), probabilities.values())
plt.xlabel('Sum of the dices')
plt.ylabel('Probabilities')
plt.title('Probabilities of the sum out of throwing 2 dices')
plt.show()

