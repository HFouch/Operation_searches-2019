from class_Adjacencies import Adjacencies
adjacency_calculation = Adjacencies()




class solve_2_operation_search:
    def __init__(self):
        pass

    def __del__(self):
        pass

    #note to self: with this function you are siting with duplicates i.e. (x, y) and (y, x) are listed as inversions
    def inversion_s2_search( non_final_adjacency_list, FS_telomeric_adjacencies):
        inversions_s2 = []
        for x, y in non_final_adjacency_list:

            gene_extremity1_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, x)

            gene_extremity2_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, y)


            if (gene_extremity1_partner, gene_extremity2_partner) in non_final_adjacency_list:
                inversions_s2.append(((x,y), (gene_extremity1_partner, gene_extremity2_partner)))

            else:
                pass
        return inversions_s2

  


    def translocations_fissions_s2_search(non_final_state_adjacencies, FS_telomeric_adjacencies, adjacency_list):
        fissions_s2 = []
        balanced_translocation_s2 = []
        unbalanced_translocations_s2 = []

        for x, y in non_final_state_adjacencies:


            #print('(x,y): ', (x, y))
            x_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, x)
            y_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, y)
            #print('partners y, x: ', (y_partner,x_partner))
            #print()

            if y_partner == x_partner == 'T':
                print('IDed as fission: ', (x, y), (y_partner, x_partner))
                fissions_s2.append((x, y))
                print('Fissions: ', fissions_s2)

            if (y_partner, x_partner) not in non_final_state_adjacencies:
                #print('not in nfal: ', (y_partner,x_partner))
                pass


            elif any(adjacency[0] =='T' for adjacency in adjacency_list[adjacency_list.index((x,y)):adjacency_list.index((y_partner, x_partner))]) or any(adjacency[1] =='T' for adjacency in adjacency_list[adjacency_list.index((x,y)):adjacency_list.index((y_partner, x_partner))]):
                if y_partner != 'T' and x_partner != 'T':
                    #print('balanced translocation: ',(x,y), (y_partner,x_partner) )
                    balanced_translocation_s2.append(((x,y), (y_partner,x_partner)))
                elif y_partner == 'T' or x_partner == 'T':
                    unbalanced_translocations_s2.append(((x,y), (y_partner,x_partner)))
                else:
                    pass
            else:
                pass
        return (fissions_s2, balanced_translocation_s2, unbalanced_translocations_s2)

    # note to self: with this function you are siting with duplicates i.e. (x, y) and (y, x) are listed as fusions
    def fusion_search(non_final_adjacencies, FS_telomeric_adjacencies):
        fusions = []
        for x,y in non_final_adjacencies:
            if x == 'T':
                y_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, y)
                if (y_partner, 'T') in non_final_adjacencies:
                    fusions.append(((x, y), (y_partner, 'T')))
            elif y == 'T':
                x_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, x)
                if ('T', x_partner) in non_final_adjacencies:
                    fusions.append(((x, y), ('T', x_partner)))
            else:
                pass

        return fusions

    
    
    def transposition_s2_search(non_final_adjacencies, FS_telomeric_adjacencies):
        s2_transpositions = []
        s2_inverted_transpositions = []

        for x, y in non_final_adjacencies:
            x_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, x)
            y_partner = Adjacencies.calculate_final_state_adjacency_partner(FS_telomeric_adjacencies, y)
            print('!!(x, y): ', (x,y))

            for a,b in non_final_adjacencies:

                if b == x_partner:
                    adjacency_1 = (a, b)
                    for c,d in non_final_adjacencies[non_final_adjacencies.index((x,y)):]:
                        if c == y_partner:
                            adjacnecy_2 = (c,d)
                            s2_transpositions.append(((x,y), adjacency_1, adjacnecy_2))
                            pass

                elif b == y_partner:
                    adjacency_1 = (a,b)
                    for c,d in non_final_adjacencies[non_final_adjacencies.index((x,y)):]:
                        if c == x_partner:
                            adjacnecy_2 = (c, d)
                            s2_inverted_transpositions.append(((x, y), adjacency_1, adjacnecy_2))
                            pass

                pass

        return((s2_inverted_transpositions, s2_transpositions))

