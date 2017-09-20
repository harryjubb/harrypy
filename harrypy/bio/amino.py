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

PROT_ATOM_TYPES = {
    "hbond acceptor":       [
        "ALAO",         # all the carbonyl Oxygens in the main chain
        "ARGO",
        "ASNO",
        "ASPO",
        "CYSO",
        "GLNO",
        "GLUO",
        "GLYO",
        "HISO",
        "ILEO",
        "LEUO",
        "LYSO",
        "METO",
        "PHEO",
        "PROO",
        "SERO",
        "THRO",
        "TRPO",
        "TYRO",
        "VALO",
        "ALAOXT",         # all the carbonyl Oxygens terminals
        "ARGOXT",
        "ASNOXT",
        "ASPOXT",
        "CYSOXT",
        "GLNOXT",
        "GLUOXT",
        "GLYOXT",
        "HISOXT",
        "ILEOXT",
        "LEUOXT",
        "LYSOXT",
        "METOXT",
        "PHEOXT",
        "PROOXT",
        "SEROXT",
        "THROXT",
        "TRPOXT",
        "TYROXT",
        "VALOXT",
        "ASNOD1",
        "ASNND2",  # for the ambiguity of the position of the N and O
        "ASPOD1",
        "ASPOD2",
        "GLNOE1"
        "GLNNE2",  # for the ambiguity of the position of the N and O
        "GLUOE1",
        "GLUOE2",
        "HISND1",  # for the ambiguity of the position of the N/C
        "HISCE1",  # for the ambiguity of the position of the N/C
        "HISNE2",  # for the ambiguity of the position of the N/C
        "HISCD2",  # for the ambiguity of the position of the N/C
        "METSD",  # http://pubs.acs.org/doi/abs/10.1021/jz300207k and pubid 19089987
        # pubid 19089987, also when they from
        # di-sulfide (Cys-Cys, fig 8 paper)
        "CYSSG",
        "SEROG",  # isostar plots
        "THROG1",  # isostar plots
        "TYROH"  # isostar plots
    ],
    "hbond donor":          [
        "ALAN",          # all the amide nitrogens in the main chain except proline
        "ARGN",
        "ASNN",
        "ASPN",
        "CYSN",
        "GLNN",
        "GLUN",
        "GLYN",
        "HISN",
        "ILEN",
        "LEUN",
        "LYSN",
        "METN",
        "PHEN",
        "SERN",
        "THRN",
        "TRPN",
        "TYRN",
        "VALN",
        "ARGNE",
        "ARGNH1",
        "ARGNH2",
        "ASNND2",
        "ASNOD1",  # for the ambiguity of the position of the N and O
        "CYSSG",  # http://www.ncbi.nlm.nih.gov/pubmed/19089987
        "GLNNE2",
        "GLNOE1",  # for the ambiguity of the position of N/O
        "HISND1",  # for the ambiguity of the position of the N/C
        "HISCE1",  # for the ambiguity of the position of the N/C
        "HISNE2",  # for the ambiguity of the position of the N/C
        "HISCD2",  # for the ambiguity of the position of the N/C
        "LYSNZ",
        "SEROG",
        "THROG1",
        "TRPNE1",
        "TYROH"
    ],
    "xbond acceptor": [
        "ALAO",         # all the carbonyl Oxygens in the main chain
        "ARGO",
        "ASNO",
        "ASPO",
        "CYSO",
        "GLNO",
        "GLUO",
        "GLYO",
        "HISO",
        "ILEO",
        "LEUO",
        "LYSO",
        "METO",
        "PHEO",
        "PROO",
        "SERO",
        "THRO",
        "TRPO",
        "TYRO",
        "VALO",
        "ALAOXT",         # all the carbonyl Oxygens terminals
        "ARGOXT",
        "ASNOXT",
        "ASPOXT",
        "CYSOXT",
        "GLNOXT",
        "GLUOXT",
        "GLYOXT",
        "HISOXT",
        "ILEOXT",
        "LEUOXT",
        "LYSOXT",
        "METOXT",
        "PHEOXT",
        "PROOXT",
        "SEROXT",
        "THROXT",
        "TRPOXT",
        "TYROXT",
        "VALOXT",
        "ASNOD1",
        "ASNND2",  # for the ambiguity of the position of the N and O
        "ASPOD1",
        "ASPOD2",
        "GLNOE1"
        "GLNNE2",  # for the ambiguity of the position of the N and O
        "GLUOE1",
        "GLUOE2",
        "HISND1",  # for the ambiguity of the position of the N/C
        "HISCE1",  # for the ambiguity of the position of the N/C
        "HISNE2",  # for the ambiguity of the position of the N/C
        "HISCD2",  # for the ambiguity of the position of the N/C
        "METSD",  # http://pubs.acs.org/doi/abs/10.1021/jz300207k and pubid 19089987
        # pubid 19089987, also when they from
        # di-sulfide (Cys-Cys, fig 8 paper)
        "CYSSG",
        "SEROG",  # isostar plots
        "THROG1",  # isostar plots
        "TYROH"  # isostar plots
    ],
    "weak hbond acceptor": [
        "ALAO",         # all the carbonyl Oxygens in the main chain
        "ARGO",
        "ASNO",
        "ASPO",
        "CYSO",
        "GLNO",
        "GLUO",
        "GLYO",
        "HISO",
        "ILEO",
        "LEUO",
        "LYSO",
        "METO",
        "PHEO",
        "PROO",
        "SERO",
        "THRO",
        "TRPO",
        "TYRO",
        "VALO",
        "ALAOXT",         # all the carbonyl Oxygens terminals
        "ARGOXT",
        "ASNOXT",
        "ASPOXT",
        "CYSOXT",
        "GLNOXT",
        "GLUOXT",
        "GLYOXT",
        "HISOXT",
        "ILEOXT",
        "LEUOXT",
        "LYSOXT",
        "METOXT",
        "PHEOXT",
        "PROOXT",
        "SEROXT",
        "THROXT",
        "TRPOXT",
        "TYROXT",
        "VALOXT",
        "ASNOD1",
        "ASNND2",  # for the ambiguity of the position of the N and O
        "ASPOD1",
        "ASPOD2",
        "GLNOE1"
        "GLNNE2",  # for the ambiguity of the position of the N and O
        "GLUOE1",
        "GLUOE2",
        "HISND1",  # for the ambiguity of the position of the N/C
        "HISCE1",  # for the ambiguity of the position of the N/C
        "HISNE2",  # for the ambiguity of the position of the N/C
        "HISCD2",  # for the ambiguity of the position of the N/C
        "METSD",  # http://pubs.acs.org/doi/abs/10.1021/jz300207k and pubid 19089987
        # pubid 19089987, also when they from
        # di-sulfide (Cys-Cys, fig 8 paper)
        "CYSSG",
        "SEROG",  # isostar plots
        "THROG1",  # isostar plots
        "TYROH"  # isostar plots
    ],
    "weak hbond donor": [
        "ALACA",         # all the c-alphas
        "ARGCA",
        "ASNCA",
        "ASPCA",
        "CYSCA",
        "GLNCA",
        "GLUCA",
        "GLYCA",
        "HISCA",
        "ILECA",
        "LEUCA",
        "LYSCA",
        "METCA",
        "PHECA",
        "PROCA",
        "SERCA",
        "THRCA",
        "TRPCA",
        "TYRCA",
        "VALCA",
        "ALACB",  # cb and further down
        "ARGCB",
        "ARGCG",
        "ARGCD",
        "ASNCB",
        "ASPCB",
        "CYSCB",
        "GLNCB",
        "GLNCG",
        "GLUCB",
        "GLUCG",
        "GLNCB",
        "HISCB",
        "ILECB",
        "ILECG1",
        "ILECD1",
        "ILECG2",
        "LEUCB",
        "LEUCG",
        "LEUCD1",
        "LEUCD2",
        "LYSCB",
        "LYSCG",
        "LYSCD",
        "LYSCE",
        "METCB",
        "METCG",
        "METCE",
        "PHECB",
        "PHECG",
        "PHECD1",
        "PHECD2",
        "PHECE1",
        "PHECE2",
        "PHECZ",
        "PROCB",
        "PROCG",
        "PROCD",
        "SERCB",
        "THRCB",
        "THRCG2",
        "TRPCB",
        "TRPCD1"
        "TRPCE3",
        "TRPCZ3",
        "TRPCH2",
        "TRPCZ2",
        "TYRCB",
        "TYRCD1",
        "TYRCD2",
        "TYRCE1",
        "TYRCE2",
        "TRYCB",
        "VALCB",
        "VALCG1",
        "VALCG2"
    ],
    "pos ionisable":   [
        "ARGNE",
        "ARGCZ",
        "ARGNH1",
        "ARGNH2",
        "HISCG",
        "HISND1",
        "HISCE1",
        "HISNE2",
        "HISCD2",
        "LYSNZ"
    ],
    "neg ionisable": [
        "ASPOD1",
        "ASPOD2",
        "GLUOE1",
        "GLUOE2"
    ],
    "hydrophobe": [
        "ALACB",
        "ARGCB",
        "ARGCG",
        "ASNCB",
        "ASPCB",
        "CYSCB",  # sulfur in Cys has an Hydrogen, it is polarised
        "GLNCB",
        "GLNCG",
        "GLUCB",
        "GLUCG",
        "GLNCB",
        "HISCB",
        "ILECB",
        "ILECG1",
        "ILECD1",
        "ILECG2",
        "LEUCB",
        "LEUCG",
        "LEUCD1",
        "LEUCD2",
        "LYSCB",
        "LYSCG",
        "LYSCD",
        "METCB",
        "METCG",
        "METSD",
        "METCE",
        "PHECB",
        "PHECG",
        "PHECD1",
        "PHECD2",
        "PHECE1",
        "PHECE2",
        "PHECZ",
        "PROCB",
        "PROCG",
        "THRCG2",
        "TRPCB",
        "TRPCG",
        "TRPCD2",
        "TRPCE3",
        "TRPCZ3",
        "TRPCH2",
        "TRPCZ2",
        "TRYCB",
        "TYRCG",
        "TYRCD1",
        "TYRCD2",
        "TYRCE1",
        "TYRCE2",
        "VALCB",
        "VALCG1",
        "VALCG2"
    ],
    "carbonyl oxygen":  [
        "ALAO",         # all the carbonyl Oxygens in the main chain
        "ARGO",
        "ASNO",
        "ASPO",
        "CYSO",
        "GLNO",
        "GLUO",
        "GLYO",
        "HISO",
        "ILEO",
        "LEUO",
        "LYSO",
        "METO",
        "PHEO",
        "PROO",
        "SERO",
        "THRO",
        "TRPO",
        "TYRO",
        "VALO"
    ],
    "carbonyl carbon": [
        "ALAC",
        "ARGC",
        "ASNC",
        "ASPC",
        "CYSC",
        "GLNC",
        "GLUC",
        "GLYC",
        "HISC",
        "ILEC",
        "LEUC",
        "LYSC",
        "METC",
        "PHEC",
        "PROC",
        "SERC",
        "THRC",
        "TRPC",
        "TYRC",
        "VALC"
    ],
    "aromatic": [
        "HISCG",
        "HISND1",
        "HISCE1",
        "HISNE2",
        "HISCD2",
        "PHECG",
        "PHECD1",
        "PHECD2",
        "PHECE1",
        "PHECE2",
        "PHECZ",
        "TRPCG",
        "TRPCD1",
        "TRPCD2",
        "TRPNE1",
        "TRPCE2",
        "TRPCE3",
        "TRPCZ2",
        "TRPCZ3",
        "TRPCH2",
        "TYRCG",
        "TYRCD1",
        "TYRCD2",
        "TYRCE1",
        "TYRCE2",
        "TYRCZ"

    ]
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
