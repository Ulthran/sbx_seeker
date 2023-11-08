try:
    BENCHMARK_FP
except NameError:
    BENCHMARK_FP = output_subdir(Cfg, "benchmarks")
try:
    LOG_FP
except NameError:
    LOG_FP = output_subdir(Cfg, "logs")
try:
    VIRUS_FP
except NameError:
    VIRUS_FP = Cfg["all"]["output_fp"] / "virus"


localrules:
    all_seeker,


rule all_seeker:
    input:
        expand(VIRUS_FP / "seeker" / "{sample}.tsv", sample=Samples.keys()),


rule filter_contigs:
    input:
        contigs=ASSEMBLY_FP / "virus_id_megahit" / "{sample}_asm" / "final.contigs.fa",
    output:
        contigs=ASSEMBLY_FP / "seeker_filtered" / "{sample}.fa",
    params:
        min_contig_length=300,  # Should be 200 but seeker was complaining with 200+ bp contigs
    script:
        "scripts/filter_contigs.py"


rule run_seeker:
    input:
        contigs=ASSEMBLY_FP / "seeker_filtered" / "{sample}.fa",
    output:
        seeker_out=VIRUS_FP / "seeker" / "{sample}.txt",
    conda:
        "envs/sbx_seeker_env.yml"
    shell:
        """
        pip install seeker
        if [ -s {input.contigs} ]; then
            predict-metagenome {input.contigs} > {output.seeker_out}
        else
            echo "No contigs found for {wildcards.sample}"
            touch {output.seeker_out}
        fi
        """


rule parse_seeker_output:
    input:
        seeker_out=VIRUS_FP / "seeker" / "{sample}.txt",
    output:
        parsed_out=VIRUS_FP / "seeker" / "{sample}.tsv",
    script:
        "scripts/parse_seeker_output.py"
