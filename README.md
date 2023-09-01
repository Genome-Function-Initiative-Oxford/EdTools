# EDTools -- EvolvedDevelopmentTools

BEDTools style repository for passing VCF/BED files.

Designed to combined variant calls from peaked data with the reference genome. Returns the genomic sequence of the allele most present in the peak.

Example Usage:

```
import ed_tools

py_ed_tool = ed_tools.EdTool("/<path>/analysis_regions.txt")

py_ed_tool = py_ed_tool.sequence(
    fi= "/<path>/genome.fa",
    vcf="/<path>/gatk-snp-indel.vcf.gz"
)
sequences = py_ed_tool.sequences
```

To run the unittests please run:

```
cd ed_tools
python -m unittest discover
```
