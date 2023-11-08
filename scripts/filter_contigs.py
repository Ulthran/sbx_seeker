from pathlib import Path
from sunbeamlib.parse import parse_fasta, write_fasta

with open(snakemake.input.contigs) as f_in, open(
    snakemake.output.contigs, "w"
) as f_out:
    for header, seq in parse_fasta(f_in):
        if len(seq) > snakemake.params.min_contig_length:
            write_fasta((header, seq), f_out)
