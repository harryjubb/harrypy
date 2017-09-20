ONE_TO_THREE = {
    'A': 'ALA',
    'B': 'ASX',
    'C': 'CYS',
    'D': 'ASP',
    'E': 'GLU',
    'F': 'PHE',
    'G': 'GLY',
    'H': 'HIS',
    'I': 'ILE',
    'K': 'LYS',
    'L': 'LEU',
    'M': 'MET',
    'N': 'ASN',
    'P': 'PRO',
    'Q': 'GLN',
    'R': 'ARG',
    'S': 'SER',
    'T': 'THR',
    'U': 'SEC',
    'V': 'VAL',
    'W': 'TRP',
    'X': 'XAA',
    'Y': 'TYR',
    'Z': 'GLX',
    None: None
}

THREE_TO_ONE = {
    'ALA': 'A',
    'ASX': 'B',
    'CYS': 'C',
    'ASP': 'D',
    'GLU': 'E',
    'PHE': 'F',
    'GLY': 'G',
    'HIS': 'H',
    'ILE': 'I',
    'LYS': 'K',
    'LEU': 'L',
    'MET': 'M',
    'ASN': 'N',
    'PRO': 'P',
    'GLN': 'Q',
    'ARG': 'R',
    'SER': 'S',
    'THR': 'T',
    'SEC': 'U',
    'VAL': 'V',
    'TRP': 'W',
    'XAA': 'X',
    'TYR': 'Y',
    'GLX': 'Z',
    None: None
}

def _change_aa_format(aa, translator):
    '''
    General function for changing amino acids from one format to another
    using a translator dictionary.
    '''

    return translator[aa] if aa in translator else aa


def one_to_three(aa):
    'Convert one letter amino acid to three letter amino acid.'

    return _change_aa_format(aa, translator=ONE_TO_THREE)


def three_to_one(aa):
    'Convert three letter amino acid to one letter amino acid.'

    return _change_aa_format(aa, translator=THREE_TO_ONE)
