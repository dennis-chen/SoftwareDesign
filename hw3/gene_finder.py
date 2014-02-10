# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 11:24:42 2014

@author: Dennis Chen
"""

# you may find it useful to import these variables (although you are not required to use them)
from amino_acids import aa, codons

def collapse(L):
    """ Converts a list of strings to a string by concatenating all elements of the list """
    output = ""
    for s in L:
        output = output + s
    return output


def coding_strand_to_AA(dna):
    """ Computes the Protein encoded by a sequence of DNA.  This function
        does not check for start and stop codons (it assumes that the input
        DNA sequence represents an protein coding region).
        
        dna: a DNA sequence represented as a string
        returns: a string containing the sequence of amino acids encoded by the
                 the input DNA fragment
    """
    aa_string = ''
    for i in range(0,len(dna),3):
        for j in range(0,len(codons)):
            if dna[i:i+3] in codons[j]:
                aa_string += aa[j]
    return aa_string

def coding_strand_to_AA_unit_tests():
    """ Unit tests for the coding_strand_to_AA function """
    print 'codon: ATG,ATG,ATT,ATC,ATA, expecting: MMIII'
    print coding_strand_to_AA('ATGATGATTATCATA')
    print 'codon: TTT,TTC, expecting: FF'
    print coding_strand_to_AA('TTTTTC')
    print 'codon: TCC,TTC,TCA,TCG,AGT,AGC,ATT,ATC,ATA, expecting: SSSSSSIII'
    print coding_strand_to_AA('TCTTCCTCATCGAGTAGCATTATCATA')
    print 'codon: TGG,TGG, expecting: WW'
    print coding_strand_to_AA('TGGTGG')
    print 'codon: TGG, expecting: W'
    print coding_strand_to_AA('TGG')

def get_reverse_complement(dna):
    """ Computes the reverse complementary sequence of DNA for the specfied DNA
        sequence
    
        dna: a DNA sequence represented as a string
        returns: the reverse complementary DNA sequence represented as a string
    """
    baseDict = {'A':'T','T':'A','C':'G','G':'C'} 
    reverse_complement = ''
    for i in range(len(dna)):
        reverse_complement = baseDict[dna[i]] + reverse_complement
    return reverse_complement
    
def get_reverse_complement_unit_tests():
    """ Unit tests for the get_complement function """
        
    print 'input: ATCG ,expected output: TAGC ,actual output: '+get_reverse_complement('ATCG')   
    print 'input: G ,expected output: C ,actual output: '+get_reverse_complement('G')

def rest_of_ORF(dna):
    """ Takes a DNA sequence that is assumed to begin with a start codon and returns
        the sequence up to but not including the first in frame stop codon.  If there
        is no in frame stop codon, returns the whole string.
        
        dna: a DNA sequence
        returns: the open reading frame represented as a string
    """
    i = 0
    stopCodonNotFound = True
    stopIndex = len(dna)
    while i in range(0,len(dna)-1,3) and stopCodonNotFound:
        codon = dna[i:i+3]
        if codon == 'TAG' or codon == 'TAA' or codon == 'TGA':
            stopCodonNotFound = False
            stopIndex = i
        i+=3
    return dna[:stopIndex]
    
    
def rest_of_ORF_unit_tests():
    """ Unit tests for the rest_of_ORF function """
    print "input: TAG ,expected output: '' ,actual output: "+rest_of_ORF('TAG')
    print 'input: GAT ,expected output: GAT ,actual output: '+rest_of_ORF('GAT')
    print 'input: ATGGTA, expected output: ATGGTA, actual output: '+rest_of_ORF('ATGGTA')
    print 'input: TACTGTATATGA ,expected output: TACTGTATA ,actual output: '+rest_of_ORF('TACTGTATATGA')

#rest_of_ORF_unit_tests()

def find_all_ORFs_oneframe(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence and returns
        them as a list.  This function should only find ORFs that are in the default
        frame of the sequence (i.e. they start on indices that are multiples of 3).
        By non-nested we mean that if an ORF occurs entirely within
        another ORF, it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
<<<<<<< HEAD
    i = 0
    ORF_list = []
    while i in range(0,len(dna)-1,3): #ignore the last codon: even if it is a start codon nothing comes after it!
        codon = dna[i:i+3]
        if codon == 'ATG':
            rest = rest_of_ORF(dna[i+3:])
            i = i+3+len(rest)-3 #the minus three at the end is because i+=3 occurs next. we really want i to equal i + 3 + len          
            if len(rest) > 0: # avoid adding empty ORFs 
                ORF_list.append(codon + rest) #used i+3 < len(dna) because that's the actual end of the ORF. 
        i+=3
    return ORF_list

        
=======
     
    # YOUR IMPLEMENTATION HERE        
     
def find_all_ORFs_oneframe_unit_tests():
    """ Unit tests for the find_all_ORFs_oneframe function """

    # YOUR IMPLEMENTATION HERE

>>>>>>> upstream/master
def find_all_ORFs(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence in all 3
        possible frames and returns them as a list.  By non-nested we mean that if an
        ORF occurs entirely within another ORF and they are both in the same frame,
        it should not be included in the returned list of ORFs.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    if len(dna)<3:
        return None
    dna_shift_1 = dna[1:]
    dna_shift_2 = dna[2:]
    return find_all_ORFs_oneframe(dna)+find_all_ORFs_oneframe(dna_shift_1)+find_all_ORFs_oneframe(dna_shift_2)
    

def find_all_ORFs_unit_tests():
    """ Unit tests for the find_all_ORFs function """
    print "input: TAGATGTGA, expected output: none ,actual output: "+str(find_all_ORFs_oneframe('TAGATGTGA'))
    print "input: TGATGA, expected output: none ,actual output: "+str(find_all_ORFs_oneframe('TGATGA'))
    print "input: ATGATGTAGTAG, expected output: [ATGATG], actual output: "+str(find_all_ORFs_oneframe('ATGATGTGATGA'))
    print "input: ATGAAATAGATGCCCTAG, expected output: [ATGAAA,ATGCCC], actual output: "+str(find_all_ORFs_oneframe('ATGAAATGAATGCCCTGA'))
    print "input: ATGAAA, expected output: [ATGAAA], actual output: "+str(find_all_ORFs_oneframe('ATGAAA'))    
    print "now test in all frames!"
    print "input: ATGAAATGATAGAATGCTAA, expected output: [ATGAAA,ATGCTAA,ATAGAATGC], actual output: "+str(find_all_ORFs('ATGAAATGATAGAATGCTAA'))
#ATG, (TAG, TAA, or TGA)
#find_all_ORFs_unit_tests()

def find_all_ORFs_both_strands(dna):
    """ Finds all non-nested open reading frames in the given DNA sequence on both
        strands.
        
        dna: a DNA sequence
        returns: a list of non-nested ORFs
    """
    reverse_complement = get_reverse_complement(dna)
    return find_all_ORFs(dna) + find_all_ORFs(reverse_complement)

def find_all_ORFs_both_strands_unit_tests():
    """ Unit tests for the find_all_ORFs_both_strands function """

    print "input: ATGAAATGATAGAATGCTAA, complement: "+get_reverse_complement('ATGAAATGATAGAATGCTAA')+' expected output: [], actual output: '+str(find_all_ORFs_both_strands('ATGAAATGATAGAATGCTAA'))
    print "input: ATGAAATAGTACTATT, complement: "+get_reverse_complement('ATGAAATAGTACTATT')+' expected output: [AAA,ATAA], actual output: '+str(find_all_ORFs_both_strands('ATGAAATAGTACTATT'))
    print "input: ATTTTTTGTATGATTATATTT, output: "+str(find_all_ORFs_both_strands('ATTTTTTGTATGATTATATTT')   )
#find_all_ORFs_both_strands_unit_tests()

def longest_ORF(dna):
    """ Finds the longest ORF on both strands of the specified DNA and returns it
        as a string"""

    all_strands = find_all_ORFs_both_strands(dna)
    max_strand_length = 0
    max_strand = None
    for i in range(len(all_strands)):
        if len(all_strands[i]) > max_strand_length:
            max_strand_length = len(all_strands[i])
            max_strand = all_strands[i]
    return max_strand
    
def longest_ORF_unit_tests():
    print "input: ATGAAATAGTACTATT, complement: "+get_reverse_complement('ATGAAATAGTACTATT')+' expected output: [ATGATAA], actual output: '+str(longest_ORF('ATGAAATAGTACTATT'))
    print "input: AATGAAAAAAAAAAA, complement: "+get_reverse_complement('AATGAAAAAAAAAAA')+' expected output: [ATGAAAAAAAAAAA], actual output: '+str(longest_ORF('AATGAAAAAAAAAAA'))
#longest_ORF_unit_tests()

def longest_ORF_unit_tests():
    """ Unit tests for the longest_ORF function """

    # YOUR IMPLEMENTATION HERE

def longest_ORF_noncoding(dna, num_trials):
    """ Computes the maximum length of the longest ORF over num_trials shuffles
        of the specfied DNA sequence
        
        dna: a DNA sequence
        num_trials: the number of random shuffles
        returns: the maximum length longest ORF """
    from random import shuffle
    orf_max_length = 0
    for i in range(num_trials):
        print i
        dna_list = list(dna)
        shuffle(dna_list)
        string_i = collapse(dna_list)
        longest_ORF_in_string_i = longest_ORF(string_i)
        if len(longest_ORF_in_string_i) > orf_max_length: 
            orf_max_length = len(longest_ORF_in_string_i)
    return orf_max_length
    
def longest_ORF_noncoding_unit_tests():
    print 'input: AGTAAATAGTACTATT, output: length 16  '+longest_ORF_noncoding('ATGAAATAGTACTATT',600)
    print 'input: AGTAAAAATAAGA, output: '+longest_ORF_noncoding('ATGAAAAAATAG',600)

#longest_ORF_noncoding_unit_tests()

def gene_finder(dna, threshold):
    """ Returns the amino acid sequences coded by all genes that have an ORF
        larger than the specified threshold.
        
        dna: a DNA sequence
        threshold: the minimum length of the ORF for it to be considered a valid
                   gene.
        returns: a list of all amino acid sequences whose ORFs meet the minimum
                 length specified.
    """
    
    all_ORFs = find_all_ORFs_both_strands(dna)
    all_ORFs_over_thres = []
    for i in range(0,len(all_ORFs)):
        if len(all_ORFs[i]) > threshold:
            all_ORFs_over_thres.append(all_ORFs[i])
    print all_ORFs_over_thres
    print coding_strand_to_AA(all_ORFs_over_thres[0])    
    all_AAs = []
    for i in all_ORFs_over_thres:
        all_AAs.append(coding_strand_to_AA(i))
    return all_AAs
   
#from load import load_seq
#dna = load_seq("./data/X73525.fa")
#longest_strand = longest_ORF_noncoding(dna,1500)
#print longest_strand #longest strand found is 660 characters long!
#res = gene_finder(dna,800)
#print res
