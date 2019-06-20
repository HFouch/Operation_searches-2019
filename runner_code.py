from class_Adjacencies import Adjacencies

from class_solve_2_operation_search import solve_2_operation_search


if __name__ == '__main__':

        adjacency_calculation = Adjacencies()
        s2_operation_search = solve_2_operation_search()

        genes = [(1, 2, 3,4,7,8), (5, 6), (9, 10, 11), (12,15), (14, 13), (16, 17), (18)]

        list_of_gene_extremities = Adjacencies.create_gene_extremities(genes)
        print('List of gene extremities:', list_of_gene_extremities)


        adjacency_list = Adjacencies.create_adjacency_list(list_of_gene_extremities)
        print()
        print('List of adjacnecies', adjacency_list)



        genesA = [(1, 2, 3, 4) ,(5, 6, 7, 8), (9), (10, 11), (12, 13), (14, 15), (16, 17, 18)]

        list_of_gene_extremitiesA = Adjacencies.create_gene_extremities(genesA)
        print('FS List of gene extremities:', list_of_gene_extremitiesA)

        adjacency_listA = Adjacencies.create_adjacency_list(list_of_gene_extremitiesA)
        print()
        print('FS List of adjacnecies', adjacency_listA)

        final_state_telomeric_adjacencies = Adjacencies.calculate_list_of_final_state_telomeric_adjacencies(adjacency_listA)
        print()
        print('telomeric adjs:', final_state_telomeric_adjacencies)

        non_FS_adjacencies = Adjacencies.find_non_FS_adjacencies(adjacency_list, adjacency_listA)
        print()
        print('non final state adjacencies', non_FS_adjacencies)


        s2_inversion_searching = solve_2_operation_search.inversion_s2_search(non_FS_adjacencies, final_state_telomeric_adjacencies)

        #print()
        #print(s2_inversion_searching)

        s2_translocation_and_fission_searching = solve_2_operation_search.translocations_fissions_s2_search(non_FS_adjacencies, final_state_telomeric_adjacencies, adjacency_list)
        s2_fissions = s2_translocation_and_fission_searching[0]
        s2_balanced_translocations = s2_translocation_and_fission_searching[1]
        s2_unbalanced_translocations =s2_translocation_and_fission_searching[2]

        print('fissions: ', s2_fissions)
        print()
        print('balanced translocations: ', s2_balanced_translocations)
        print()
        print('unbalanced translocations: ', s2_unbalanced_translocations)

        fusions = solve_2_operation_search.fusion_search(non_FS_adjacencies, final_state_telomeric_adjacencies)
        print()
        print('Fussions: ',fusions)