from typing import Dict, List, Tuple
import numpy as np

AAs: str = 'ALGVSREDTIPKFQNYMHWCUZO'


def get_aa_composition(protein_seq: str) -> Dict[str, int]:
    return {}


def k_mers(alphabet: str, k: int) -> List[str]:
    if k == 0:
        return ['']
    if k < 0:
        print("The length of k-mers can not be negative. =(")
        return ['']
    list_of_k_mers = []
    for char in alphabet:
        for item in k_mers(alphabet, k - 1):
            list_of_k_mers.append(char + item)
    return list_of_k_mers


def get_kmer_composition(protein_seq: str, k: int) -> Dict[str, int]:
    return {}


def get_alignment(protein_seq_1: str, protein_seq_2: str,
                  gap_penalty: int, substitution_matrix: Dict[str, Dict[str, int]]) -> Tuple[str, str]:
    return '', ''

print(k_mers(AAs, 3))