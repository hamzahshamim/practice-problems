s = "CTGAAGATGGGGTTGCGCTACACGGATGACGACAGCTTCCGATACGGGTTCTGAGGAACCTAACAACGGCTCTAAGTTTGTATCACTACATCTGACACTATCGACAGGTTGTGGTTGGCCCTAAGCCCCCACATACATCACTGCCCCCGGCAGCGGAACCGATCCACGGATACGTATCAGTAAAGGCGAGCATCTGAAAGCTAAGGTTAGTTTTTCTACTAGGTTTCGCTGTAAGTGAAGCTAGTAACGCTATTCGAATGTACGTTGAGTACGCCGTTTAATCCCACTACTCGGGTAAGACTCTATTTCGTCAGTGTTGCCCCGGAGCTCGCGCTTGGGTAGAAGCTGCGTCATGCGCCGTAAAGACCACCCTGGTTGTAGAACGGACATGGTCGTCTGATCTCGCTATCGTCTGTGAATAGCCTATGGTACATTCACTAGTAATGCACACAAATAATTTGACGAGCTCAAAGTACGTACCTAGGGGTTTAGATGACACCCTAGCAACCCACTAACCACATCCGCACCATCCTAACTGCGTGTATGTAGTGCAGCCCATGCCGTACGCAATATCGGTGGCAAGGGCCCAGTTTGTCGCGGCCGCTGCGTCACGTAGAATCTTGTAACAACTTCTATGACCCTACCCAATTTGAAGCTTCAAGGTGTAATGGTCTCGAAAGACAAACCCTGGCGCGTTCTAGGAACTAAATCCTGCTGCTAATCCTGCAACTTACGGAAACGGCTATCGTATGTATGATGATCACACGCAACCATCGATTATTGGGAATGTCCATTTCGAATAACACCCGCATACAAGACGTGTCGGGAAGGTGAAACCTTGGAGTAGGGGCATGTCACAGGTAAGTTCTGCCTATACGTCACTTCTCGCCCGCGGCGTCGCAGGTTGACTAGAGTTTGGAGGCCGTCACAAAACGCACCCCAGGTGCGAGTAATTACACCACCCCAATTGCTACCCAAATAAAAA"
i = 0
a, g, t, c = 0, 0, 0, 0


while i < len(s):
    if s[i] == "A":
        a = a + 1
    if s[i] == "G":
        g = g + 1
    if s[i] == "T":
        t = t + 1
    if s[i] == "C":
        c = c + 1
    i = i + 1

print "A = " + str(a)
print "G = " + str(g)
print "T = " + str(t)
print "C = " + str(c)




