#!/usr/bin/env python3
"""
DNA Sequence Analyzer
A simple tool to analyze DNA sequences input by the user.
Calculates GC content, length, composition, and translates to protein.
"""

def is_valid_dna(sequence):
    """Check if sequence contains only valid DNA bases (A, T, G, C)"""
    valid_bases = set('ATGCatgc')
    return all(base in valid_bases for base in sequence)


def calculate_gc_content(sequence):
    """Calculate GC content (percentage of G and C bases)"""
    sequence = sequence.upper()
    if len(sequence) == 0:
        return 0
    gc_count = sequence.count('G') + sequence.count('C')
    gc_percent = (gc_count / len(sequence)) * 100
    return gc_percent


def get_base_composition(sequence):
    """Count frequency of each base (A, T, G, C)"""
    sequence = sequence.upper()
    composition = {
        'A': sequence.count('A'),
        'T': sequence.count('T'),
        'G': sequence.count('G'),
        'C': sequence.count('C')
    }
    return composition


def complement_strand(sequence):
    """Generate the complement DNA strand"""
    sequence = sequence.upper()
    complement_map = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    complement = ''.join(complement_map.get(base, 'N') for base in sequence)
    return complement


def reverse_complement(sequence):
    """Generate the reverse complement of DNA sequence"""
    complement = complement_strand(sequence)
    return complement[::-1]


def translate_dna_to_protein(sequence):
    """Translate DNA sequence to protein using standard genetic code"""
    # Standard genetic code codon table
    codon_table = {
        'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
        'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
        'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
        'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
        'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
        'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
        'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
        'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    sequence = sequence.upper()
    protein = ""
    
    # Translate in triplets (codons)
    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        if codon in codon_table:
            protein += codon_table[codon]
        else:
            protein += 'X'  # Unknown amino acid
    
    return protein


def print_separator():
    """Print a separator line"""
    print("\n" + "=" * 60 + "\n")


def main():
    """Main program"""
    print("\n" + "=" * 60)
    print("       DNA SEQUENCE ANALYZER")
    print("=" * 60)
    print("Analyze DNA sequences with this tool!")
    print("=" * 60 + "\n")
    
    # Get sequence from user
    while True:
        sequence = input("Enter your DNA sequence (A, T, G, C): ").strip()
        
        if not sequence:
            print("❌ Sequence cannot be empty. Please try again.")
            continue
        
        if not is_valid_dna(sequence):
            print("❌ Invalid sequence! Only use A, T, G, C bases.")
            continue
        
        break
    
    sequence = sequence.upper()
    print_separator()
    
    # Display analysis
    print(f"📝 SEQUENCE ANALYSIS")
    print(f"Original sequence: {sequence}")
    print(f"Sequence length: {len(sequence)} bp")
    
    print_separator()
    
    # Base composition
    composition = get_base_composition(sequence)
    print(f"📊 BASE COMPOSITION")
    print(f"  A (Adenine):  {composition['A']} ({(composition['A']/len(sequence)*100):.1f}%)")
    print(f"  T (Thymine):  {composition['T']} ({(composition['T']/len(sequence)*100):.1f}%)")
    print(f"  G (Guanine):  {composition['G']} ({(composition['G']/len(sequence)*100):.1f}%)")
    print(f"  C (Cytosine): {composition['C']} ({(composition['C']/len(sequence)*100):.1f}%)")
    
    print_separator()
    
    # GC Content
    gc = calculate_gc_content(sequence)
    print(f"🧬 GC CONTENT")
    print(f"  GC%: {gc:.2f}%")
    if gc < 30:
        print(f"  ℹ️  Low GC content (typical for AT-rich regions)")
    elif gc > 70:
        print(f"  ℹ️  High GC content (typical for GC-rich regions)")
    else:
        print(f"  ℹ️  Moderate GC content (typical for most organisms)")
    
    print_separator()
    
    # Complement strand
    complement = complement_strand(sequence)
    print(f"🔀 COMPLEMENT STRAND")
    print(f"  5' → 3': {sequence}")
    print(f"  3' ← 5': {complement}")
    
    print_separator()
    
    # Reverse complement
    rev_comp = reverse_complement(sequence)
    print(f"↩️  REVERSE COMPLEMENT")
    print(f"  Original (5' → 3'):      {sequence}")
    print(f"  Reverse Complement:      {rev_comp}")
    
    print_separator()
    
    # Protein translation
    protein = translate_dna_to_protein(sequence)
    print(f"🧫 PROTEIN TRANSLATION (Standard Genetic Code)")
    print(f"  DNA sequence: {sequence}")
    print(f"  Protein:      {protein}")
    print(f"  Length: {len(protein)} amino acids")
    
    print_separator()
    
    print("✅ Analysis complete!")
    print("\nLegend:")
    print("  * = Stop codon")
    print("  X = Unknown amino acid")
    print("\n" + "=" * 60 + "\n")


if __name__ == "__main__":
    main()
