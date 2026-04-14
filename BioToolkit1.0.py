"""
=====================================================================
BIOINFORMATICS TOOLKIT USING PYTHON
=====================================================================
Author:  Dr.rer.nat. Siddhesh Uday Sapre
Email:   sapresiddhesh2023@gmail.com
Version: 1.0

COPYRIGHT (c) 2026 Dr.rer.nat. Siddhesh Uday Sapre. All rights reserved.

LICENSE AGREEMENT:
This software and associated documentation files are free to use, copy, 
and modify for academic, educational, and personal research purposes. 

Any industrial or commercial use—including but not limited to 
incorporation into commercial products, use in for-profit corporate 
research, or providing as a paid service—is strictly prohibited without 
prior written permission from the author.
=====================================================================

--- MAIN MENU DEFINITIONS ---
Step 1 is Basic Input System to provide the query DNA sequence
Step 2 is to check the validity of the DNA sequence
Step 3 is for DNA compositional statistics like individual base count, total base count, and GC content
Step 4 is to obtain reverse complement DNA sequence
Step 5 is to run 'The Central Dogma of Life' i.e. DNA-->mRNA-->Protein
Step 6 is where we scan the DNA sequence for user-defined motifs and identify their functional properties
Step 7 is where we compare the primary DNA sequence with a secondary sequence to detect and classify mutations
Step 8 is where we handle multi-sequence FASTA files, extract names and sequences, organize data, and write basic analysis results directly to a file
"""

# Global variable initialization to prevent errors if a user skips steps
dna = ""
is_valid = False
length_of_dna = 0
stop_codons = ["TAA", "TAG", "TGA"]

print("=" * 70)
print("                 BIOINFORMATICS TOOLKIT USING PYTHON                  ")
print("=" * 70)
print("Author: Dr.rer.nat. Siddhesh Uday Sapre")
print("Email: sapresiddhesh2023@gmail.com")
print("Version: 1.0")
print("Copyright (c) 2026. All rights reserved.")
print("License: Free for academic and personal use. Commercial or")
print("industrial use requires prior written permission from the author.")
print("-" * 70)
print("Step 1: Basic Input System to provide the query DNA sequence")
print("Step 2: Check the validity of the DNA sequence")
print("Step 3: DNA compositional statistics")
print("Step 4: Obtain reverse complement DNA sequence")
print("Step 5: The Central Dogma of Life (DNA --> mRNA --> Protein)")
print("Step 6: Scan the DNA sequence for user-defined motifs")
print("Step 7: Compare primary DNA sequence with a secondary sequence")
print("Step 8: Handle multi-sequence FASTA files and save to file")
print("-" * 70)
print("Note: Steps 6, 7 & 8 are optional. Once the DNA sequence is provided, the program will automatically perform Step 1 through Step 5.")

# Ask for user input from step 1 to step 8
user_steps = input("\nEnter the numbers of the Steps you want to run, separated by commas (e.g., 1,6,7), or type 'all': ").strip().lower()

if user_steps == 'all':
    run_steps = ['1', '2', '3', '4', '5', '6', '7', '8']
else:
    run_steps = [s.strip() for s in user_steps.split(',')]

# Automatic execution logic for Steps 1-5
if '1' in run_steps:
    for step in ['2', '3', '4', '5']:
        if step not in run_steps:
            run_steps.append(step)


# =====================================================================
# STEP 1: Basic Input System
# =====================================================================
if '1' in run_steps:
    print("\n" + "="*50)
    print("--- Step 1: Basic Input System ---")
    print("="*50)
    
    """This is Step 1.1 where we provide the user with the flags related to input and 
       expect the user to provide us input in the valid form."""

    note1 = "Warning: This analysis is specific for Human/Eukaryotic DNA sequence. DO NOT use prokaryotic DNA sequence for analysis."
    note2 = "Initialising Note: The sequence should be in upper case, contain valid one letter DNA base codes, and without spaces."
    note3 = "If the above requirements are not met, the sequence will first be optimised to fulfill them."
    note4 = "The above note is just a requisite for error-free processing & analysis, and does not constitute a warning. Proceed with caution.\n"

    print(note1)
    print(note2)
    print(note3)
    print(note4)

    """This is Step 1.2 where we give the choice of the source for acquiring the DNA sequence 
       viz. Manual input and FASTA file"""

    choice = input("Enter 1 for manual input or 2 for FASTA file: ")

    if choice == "1":
        dna = input("Enter the DNA sequence you want to analyse: ")

    elif choice == "2":
        # Added the strip tweak here to handle path quotes
        filename = input("Enter FASTA file name or paste the path: ").strip(' "')
        
        file = open(filename, "r")
        dna = ""
        
        for line in file:
            if line.startswith(">"):
                continue
            dna = dna + line.strip()
        
        file.close()

    dna = dna.upper()           #This is from part 1 (Basic input system)
    dna = dna.replace(" ", "")  #This is from part 1 (Basic input system)
    length_of_dna = len(dna)    # Updating global variable


# =====================================================================
# STEP 2: Validity Check
# =====================================================================
if '2' in run_steps:
    print("\n" + "="*50)
    print("--- Step 2: Validity Check ---")
    print("="*50)
    
    # This is Step 2 where we check the validity of the provided sequence
    valid_bases = "ATGC" 
    is_valid = True

    if len(dna) == 0:
        is_valid = False
        print("Sequence is empty. Please ensure Step 1 was completed correctly.\n")
    else:
        print("The DNA input has been processed & the following sequence will be used for further analysis: ", dna)

        for base in dna:
            if base not in valid_bases:
                is_valid = False
                print("Invalid character found: ", base)
                break

        if is_valid:
            print("Valid DNA sequence\n")
        else:
            print("Sequence is invalid. Please check input.\n")


# =====================================================================
# STEP 3: Compositional Statistics
# =====================================================================
if '3' in run_steps:
    print("\n" + "="*50)
    print("--- Step 3: DNA Compositional Statistics ---")
    print("="*50)

    """This is Step 3, where we analyse the DNA sequence for its compositional statistics 
       like individual base count, total base count & GC content """

    if is_valid:         # This line basically starts the count with 0 and then the further syntax does the cumulative count
        Adenine_A = 0
        Thymine_T = 0
        Guanine_G = 0
        Cytosine_C = 0

        for base in dna:
            if base == "A":
                Adenine_A += 1
            elif base == "T":
                Thymine_T += 1
            elif base == "G":
                Guanine_G += 1
            elif base == "C":
                Cytosine_C += 1

        length_of_dna = len(dna)
        Total_GC = Guanine_G + Cytosine_C
        
        # Here, I added a check to prevent dividing by zero if the user enters an empty string
        if length_of_dna > 0:
            percent_GC = (Total_GC / length_of_dna) * 100
        else:
            percent_GC = 0

        print("The total nucleotide count for this DNA sequence is: ", length_of_dna)
        print("The GC content of this DNA sequence is: ", round(percent_GC, 2), "%")
        print("A: ", Adenine_A)
        print("T: ", Thymine_T)
        print("G: ", Guanine_G)
        print("C: ", Cytosine_C)

    """Additionally, I added the syntax to:
       check whether it is an exon first, and then if it has an internal stop codon."""

    if is_valid and length_of_dna >= 3: 
        is_exon = input("\nIs the provided DNA sequence an exonic sequence? (Yes/No): ").strip().lower()

        if is_exon == "yes" or is_exon == "y":
            has_internal_stop_codon = False
            internal_stop_codon_found = []
            
            # Check for a stop codon at the very end (last 3 bases)
            end_codon = dna[-3:]
            has_end_stop_codon = end_codon in stop_codons
            
            # Scan for internal stop codons in steps of 3 (assuming reading frame 1)
            for i in range(0, length_of_dna - 3, 3):
                codon = dna[i:i+3]
                if codon in stop_codons:
                    has_internal_stop_codon = True
                    internal_stop_codon_found.append((codon, i)) 
            
            print("\n--- Stop Codon Analysis ---")
            
            # Report any internal stop codons
            if has_internal_stop_codon:
                print("Warning: Internal stop codon(s) detected! This may indicate a nonsense mutation, a pseudogene, or an incorrect reading frame.")
                for codon, index in internal_stop_codon_found:
                    print(f" -> Internal stop codon '{codon}' found starting at position {index}.")
            else:
                print("Intact ORF present: No internal stop codons were found in the assumed reading frame.")
                
            # Report any terminal stop codon
            if has_end_stop_codon:
                print(f"Normal: Expected terminal stop codon ('{end_codon}') is present at the end of the sequence.")
            else:
                print("Note: No stop codon is present at the very end of this sequence.")
                
        elif is_exon == "no" or is_exon == "n":
            print("\nSequence is not an exon. Skipping stop codon analysis.")
        else:
            print("\nUnrecognized input. Skipping stop codon analysis.")
            
    elif is_valid and length_of_dna > 0 and length_of_dna < 3:
        print("\nSequence is too short to contain a full codon. Skipping stop codon analysis.")


# =====================================================================
# STEP 4: Reverse Complement Analysis
# =====================================================================
if '4' in run_steps:
    print("\n" + "="*50)
    print("--- Step 4: Reverse Complement Analysis ---")
    print("="*50)
    
    # Here, I have included syntax to obtain reverse complement of the input DNA sequence
    if is_valid and length_of_dna > 0:
        # str.maketrans creates a mapping table to swap A with T, and G with C
        complement_map = str.maketrans("ATGC", "TACG")
        
        # dna[::-1] reverses the string, and .translate() swaps the bases using the map
        reverse_complement = dna[::-1].translate(complement_map)
        
        print(f"Original Sequence (5' -> 3'):   {dna}")
        print(f"Reverse Complement (5' -> 3'): {reverse_complement}")


# =====================================================================
# STEP 5: Transcription & Translation
# =====================================================================
if '5' in run_steps:
    print("\n" + "="*50)
    print("--- Step 5: Transcription & Translation Analysis ---")
    print("="*50)

    """This is Step 5 where we transcribe the DNA sequence into mRNA 
       and translate the mRNA into a protein sequence."""

    if is_valid and length_of_dna > 0:
        # 1. Transcription
        mRNA = dna.replace("T", "U")
        print(f"mRNA Sequence (5' -> 3'): {mRNA}")

        # 2. Translation
        print("Note: Standard one-letter abbreviations for amino acids have been used to define the codon:protein output.\n")
        if len(mRNA) >= 3:
            codon_table = {
                'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
                'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
                'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
                'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
                'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
                'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
                'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
                'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
                'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
                'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
                'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
                'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
                'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
                'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
                'UAC':'Y', 'UAU':'Y', 'UAA':'*', 'UAG':'*',
                'UGC':'C', 'UGU':'C', 'UGA':'*', 'UGG':'W'
            }
            
            protein_sequence = ""
            
            for i in range(0, len(mRNA), 3):
                codon = mRNA[i:i+3]
                if len(codon) == 3:
                    amino_acid = codon_table.get(codon, "?")
                    protein_sequence += amino_acid
                else:
                    break
                    
            print(f"Protein Sequence:      {protein_sequence}")
            print("Note: In the protein sequence above, '*' represents a stop codon.")
            
        else:
            print("Sequence is too short to translate into a protein.")


# =====================================================================
# STEP 6: Motif Analysis
# =====================================================================
if '6' in run_steps:
    print("\n" + "="*50)
    print("--- Step 6: Motif Analysis ---")
    print("="*50)

    """This is Step 6 where we scan the DNA sequence for user-defined 
       motifs and identify their functional properties."""

    if is_valid and length_of_dna > 0:
        
        do_motif = input("Do you want to look for a specific motif? (Yes/No): ").strip().lower()
        
        if do_motif == "yes" or do_motif == "y":
            """
            Examples of different motifs:
            - ATG: Start Codon (Initiates translation)
            - TAA, TAG, TGA: Stop Codons (Ends translation)
            - TATAAA: TATA Box (Promoter motif, initiates transcription)
            - CCAAT: CAAT Box (Promoter motif, initiates transcription)
            - GGGCGG: GC Box (Promoter motif, initiates transcription)
            - GCCACCATGG or GCCGCCATGG: Kozak Sequence (Translation efficiency)
            - GT: 5' Splice Site / Donor (RNA processing, removes intron)
            - AG: 3' Splice Site / Acceptor (RNA processing, removes intron)
            - AATAAA: Polyadenylation Signal (mRNA processing)
            - CG: CpG Island region (Epigenetic regulation / promoter marker)
            - TTAGGG: Telomeric Repeat (Protection of the chromosome)
            """
            print("\nIMPORTANT NOTE: Most biological motifs are consensus patterns rather than exact sequences. For example, the TATA Box consensus is TATAAA, but it may also appear naturally as TATATA or TATAAT.")
            
            print("\nExamples of different motifs you can search for:")
            print(" - ATG: Start Codon (Initiates translation)")
            print(" - TAA, TAG, TGA: Stop Codons (Ends translation)")
            print(" - TATAAA: TATA Box (Promoter motif, initiates transcription)")
            print(" - CCAAT: CAAT Box (Promoter motif, initiates transcription)")
            print(" - GGGCGG: GC Box (Promoter motif, initiates transcription)")
            print(" - GCCACCATGG: Kozak Sequence (Translation efficiency)")
            print(" - GT: 5' Splice Site / Donor (RNA processing, removes intron)")
            print(" - AG: 3' Splice Site / Acceptor (RNA processing, removes intron)")
            print(" - AATAAA: Polyadenylation Signal (mRNA processing)")
            print(" - CG: CpG Islands (Epigenetic regulation)")
            print(" - TTAGGG: Telomeric Repeats (Protection of the chromosome)\n")
            
            motif = input("Enter the motif (pattern) you want to search for: ").strip().upper()
            
            if len(motif) > 0:
                # Define exact match functional motifs
                motif_functions = {
                    "ATG": "Start Codon (Initiates translation)",
                    "CCAAT": "CAAT Box (Promoter motif, initiates transcription)",
                    "GGGCGG": "GC Box (Promoter motif, initiates transcription)",
                    "GT": "5' Splice Site / Donor (RNA processing, removes intron)",
                    "AG": "3' Splice Site / Acceptor (RNA processing, removes intron)",
                    "AATAAA": "Polyadenylation Signal (mRNA processing)",
                    "CG": "CpG Island region (Epigenetic regulation / promoter marker)",
                    "TTAGGG": "Telomeric Repeat (Protection of the chromosome)"
                }
                
                # Define consensus variant lists
                tata_variants = ["TATAAA", "TATATA", "TATAAT"]
                kozak_variants = ["GCCACCATGG", "GCCGCCATGG"] # R represents Purine (A or G)
                
                # Identify the Motif Function
                function_annotation = "Custom user motif (Unknown specific function)"
                
                if motif in motif_functions:
                    function_annotation = motif_functions[motif]
                elif motif in stop_codons: 
                    function_annotation = "Stop Codon (Ends translation)"
                elif motif in tata_variants:
                    function_annotation = "TATA Box (Promoter motif, initiates transcription)"
                elif motif in kozak_variants:
                    function_annotation = "Kozak Sequence (Translation efficiency)"
                    
                print(f"\nTarget Motif: {motif}")
                print(f"Annotation: {function_annotation}")
                
                # Find all occurrences using a loop, slicing, and string comparison
                motif_positions = []
                motif_length = len(motif)
                
                for i in range(length_of_dna - motif_length + 1):
                    current_window = dna[i:i+motif_length]
                    if current_window == motif:
                        motif_positions.append(i)
                        
                # Report the findings
                total_occurrences = len(motif_positions)
                if total_occurrences > 0:
                    print(f"Total occurrences found: {total_occurrences}")
                    print(f"Indices where motif starts: {motif_positions}")
                else:
                    print("Status: Motif not found in this DNA sequence.")
                    
            else:
                print("Invalid motif input.")
                
        elif do_motif == "no" or do_motif == "n":
            print("\nSkipping Motif Analysis.")
        else:
            print("\nUnrecognized input. Skipping Motif Analysis.")


# =====================================================================
# STEP 7: Comparative Mutation Analysis
# =====================================================================
if '7' in run_steps:
    print("\n" + "="*50)
    print("--- Step 7: Comparative Mutation Analysis ---")
    print("="*50)

    """This is Step 7 where we compare the primary DNA sequence with a 
       secondary sequence to detect and classify mutations."""

    if is_valid and length_of_dna > 0:
        compare_choice = input("Do you want to compare a second DNA sequence against the primary one? (Yes/No): ").strip().lower()

        if compare_choice == "yes" or compare_choice == "y":
            dna2 = input("Enter the second DNA sequence (mutated string / patient sample): ").upper().replace(" ", "")
            
            valid_dna2 = True
            for base in dna2:
                if base not in valid_bases:
                    valid_dna2 = False
                    print(f"Invalid character '{base}' found in the second sequence. Aborting comparative analysis.")
                    break
                    
            if valid_dna2:
                len_dna2 = len(dna2)
                mismatches = [] 
                
                # Scenario A: Equal length implies point mutations / substitutions
                if length_of_dna == len_dna2:
                    for i in range(length_of_dna):
                        if dna[i] != dna2[i]:
                            mismatches.append((i, dna[i], dna2[i]))
                            
                    total_mutations = len(mismatches)
                    print(f"\nLengths match exactly ({length_of_dna} bp).")
                    print(f"Total mutations detected: {total_mutations}")
                    
                    if total_mutations > 0:
                        print("Mutation Type Detected: Substitution (Point Mutations / Mismatch Errors)")
                        print("Detailed Breakdown:")
                        for mut in mismatches:
                            print(f" -> Mismatch at Index {mut[0]}: Original '{mut[1]}' mutated to '{mut[2]}'")
                    else:
                        print("The sequences are 100% identical. No mutations detected.")
                
                # Scenario B: Unequal length implies Insertions, Deletions (Indels), CNVs, or Frameshifts
                else:
                    len_diff = abs(length_of_dna - len_dna2)
                    print(f"\nLengths differ! Primary Sequence: {length_of_dna} bp | Secondary Sequence: {len_dna2} bp.")
                    
                    mutation_type = "Insertion" if len_dna2 > length_of_dna else "Deletion"
                    
                    if len_diff > 500: 
                        mutation_type += " | Chromosomal Mutation (Large-scale) / Possible CNV"
                    elif len_diff % 3 != 0:
                        mutation_type += " | Frameshift Mutation (High biological impact if in coding region)"
                    else:
                        mutation_type
