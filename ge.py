import string
import random

alphabet = str(string.ascii_lowercase) + ' '
target = "mutation is a genetic operation"
chance = 1

genus = lambda: ''.join([alphabet[random.randint(0, len(alphabet) - 1)] for i in range(0, len(target))])
initial_gene = genus()

reproduction_rate = 5

generations = 0

#gen_arr = []

while target != initial_gene:
    initial_gene = list(initial_gene)
    gene_pool = []
    for j in range(0, reproduction_rate):
        gene_list = []
        for i in range(0, len(initial_gene)):
            chance_mut = random.randint(0, 100)
            if chance_mut <= chance:
                if initial_gene[i] != target[i]:
                    ran_letter = alphabet[random.randint(0, len(alphabet) - 1)]
                    gene_list.append(ran_letter)
                else:
                    gene_list.append(initial_gene[i])
            else:
                gene_list.append(initial_gene[i])
        initial_gene = ''.join(gene_list)
        gene_pool.append(initial_gene)
    fitness_scores = []
    for gene in gene_pool:
        fitness_score = 0
        for m in range(0, len(target)):
            if gene[m] == target[m]:
                fitness_score += 1
            else:
                pass
        fitness_scores.append(fitness_score)
    fittest = max(fitness_scores)
    fittest_index = fitness_scores.index(fittest)
    initial_gene = gene_pool[fittest_index]
    print(initial_gene, fittest, generations)
    #gen_arr.append([generations, fitness_score])
    generations += 1

"""
with open('./gens.csv', 'wt') as output:
    for i in gen_arr:
        output.write('{},{}\n'.format(i[0], i[1]))
"""
print('Generations: {}, Mutation rate: {}%, Reproduction rate: {}'.format(generations, chance, reproduction_rate))
