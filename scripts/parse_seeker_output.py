with open(snakemake.input.seeker_out) as f_in, open(
    snakemake.output.parsed_out, "w"
) as f_out:
    flag = False
    for line in f_in.readlines():
        if line.strip() == "name\tprediction\tscore":
            flag = True
        if flag:
            f_out.write(line)
