# EDTools -- EvolvedDevelopmentTools

BEDTools style repository for passing VCF/BED files.

Designed to combined variant calls from peaked data with the reference genome. Returns the genomic sequence of the allele most present in the peak.

Example Usage:

```

import ed_tools


py_ed_tool = ed_tools.EdTool("/project/Wellcome_Discovery/esanders/fake_fastq/analysis_regions.txt")

py_ed_tool = py_ed_tool.sequence(
    fi= "/project/Wellcome_Discovery/shared/whole_genome_fasta/hg38/genome.fa",
    vcf="/project/Wellcome_Discovery/esanders/code/SkewStructure/gatk_atac/gatk-snp-indel.vcf.gz"
)
sequences = py_ed_tool.sequences

```

To run the unittests please run:

```
cd ed_tools
python -m unittest discover
```
