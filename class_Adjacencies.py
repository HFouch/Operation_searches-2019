import numpy as np

class Adjacencies:
    def __init__(self):
        pass

    def __del__(self):
        pass

    ## Reads the tab-delimited text file into a list of genes
    def genes( filename):
        genes = []
        gene_positions = []

        # Generation of the list of sequence blocks from the tab-delimited text file
        names_and_positions_of_genes = np.loadtxt(filename, delimiter='\t', unpack=True, dtype=object)
        gene_names = names_and_positions_of_genes[0, :]
        # gene_positions = names_and_positions_of_genes[1, :]

        for i in range(0, len(gene_names)):
            genes.append(int(gene_names[i]))
            # block_positions.append(tuple(sequence_block_positions[i]))
            # (The block_positions variable will be incorporated at a later stage of development)

        return genes

    def create_gene_extremities(signed_gene_list):
        gene_extremities = []

        for chromosome in signed_gene_list:

            if isinstance(chromosome, int):
                if chromosome > 0:
                    gene_extremities.append('T')
                    gene_extremities.append((int(chromosome), 't'))
                    gene_extremities.append((int(chromosome), 'h'))
                    gene_extremities.append('T')
                else:
                    gene_extremities.append('T')
                    gene_extremities.append((int(abs(chromosome)), 'h'))
                    gene_extremities.append((int(abs(chromosome)), 't'))
                    gene_extremities.append('T')

            else:
                for gene in chromosome:
                    if chromosome[0] == gene:
                        gene_extremities.append('T')

                    if gene > 0:
                        gene_extremities.append((int(gene), 't'))
                        gene_extremities.append((int(gene), 'h'))
                    else:
                        gene_extremities.append((int(abs(gene)), 'h'))
                        gene_extremities.append((int(abs(gene)), 't'))

                    if chromosome[-1]==gene:
                        gene_extremities.append('T')

        return gene_extremities


    def create_adjacency_list(gene_extremities):
        adjacency_list = []
        for i in range(0, len(gene_extremities),2):
            adjacency_list.append((gene_extremities[i], gene_extremities[i+1]))

        return adjacency_list


    def find_non_FS_adjacencies( adjacency_list, FS_adjacencies):
        adjacency_list_non_FS = []

        for x,y in adjacency_list:
            if (x, y) in FS_adjacencies:
                pass
            elif (y, x) in FS_adjacencies:
                pass
            else:
                adjacency_list_non_FS.append((x, y))

        return adjacency_list_non_FS

    def calculate_list_of_final_state_telomeric_adjacencies( final_state_adjacency_list):
        final_state_telomeric_adjacencies = []
        for x,y in final_state_adjacency_list:
            print()
            print('x, y: ', (x,y))
            if x == 'T' or y == 'T':
                print('Yess')
                final_state_telomeric_adjacencies.append((x,y))

        return final_state_telomeric_adjacencies


    def calculate_final_state_adjacency_partner( list_of_final_state_telomeric_adjacencies, gene_extremity ):

        for x,y in list_of_final_state_telomeric_adjacencies:

            if x == gene_extremity or y == gene_extremity:
                print(gene_extremity)
                partner = 'T'
                return partner
            else:
                continue

        if gene_extremity[1] == 'h':
            partner = (gene_extremity[0]+1, 't')
        else:
            partner = (gene_extremity[0]-1, 'h')
        return partner


'''

    genes = [1, -5, -4, 2, 3, 6]

    x = create_gene_extremities(genes)
    print(x)

    y = create_adjacency_list(x)
    print()
    print(y)

    genesA = [1, 2, 3, 4, 5, 6]

    a = create_gene_extremities(genesA)
    print(a)

    b = create_adjacency_list(a)
    print()
    print(b)

    c = calculate_list_of_final_state_telomeric_adjacencies(b)

    
    m = find_non_FS_adjacencies(y, b)
    print()
    
    print(m)

    print()
    print(c)

    gene_ext = (6, 'h')

    d = calculate_final_state_adjacency_partner(c, gene_ext)
    print()
    print(d)

'''
