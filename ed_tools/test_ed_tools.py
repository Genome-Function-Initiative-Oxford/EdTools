import pysam
import os

from unittest import TestCase
from ed_tools import EdTool
from pysam import VariantFile, FastaFile, VariantHeader, tabix_index, FastaFile
from tempfile import TemporaryDirectory


##ALT=<ID=NON_REF,Description="Represents any possible alternative allele not already represented at this location by REF and ALT">
##FILTER=<ID=LowQual,Description="Low quality">
##FORMAT=<ID=AD,Number=R,Type=Integer,Description="Allelic depths for the ref and alt alleles in the order listed">


class TryTesting(TestCase):
    def test_always_passes(self):
        vcfh = VariantHeader()
        vcfh.add_meta('contig', items=[('ID', "chr1"), ("assembly", "hg38"), ("species", "Homo Sapiens")])
        vcfh.add_meta('ALT', items=[('ID',"NON_REF"), ('Description','blah blah')])
        vcfh.add_meta('FILTER', items=[('ID',"LowQual"), ('Description','Low quality')])
        vcfh.add_meta('FORMAT', items=[('ID',"AD"), ('Number', 'R'), ('Type', 'Integer'), ('Description','Low quality')])
        vcfh.add_sample("ED_TOOL")
        
        with TemporaryDirectory() as tmpdirname:
            vcf_filename = os.path.join(tmpdirname, "test.vcf.gz")
            with VariantFile(vcf_filename, "w", header=vcfh) as vcf:
                new_record = vcf.new_record(
                    contig="chr1",
                    start=0, stop=1,
                    qual=10.0,
                    alleles=('A', 'T'),
                    
                )
                new_record.samples["ED_TOOL"]['AD'] = (9, 10)
                vcf.write(new_record)
            

            tabix_index(vcf_filename, preset="vcf", force=True)
            
            regions_filepath = os.path.join(tmpdirname, "regions.txt")
            with open(regions_filepath, 'w') as fp:
                fp.write("chr1:0-10\n")
            
            genome_filepath = os.path.join(tmpdirname, "genome.fa")
            
            with open(genome_filepath, 'w') as fp:
                fp.write(">chr1\n")
                fp.write("ATGATGATGATGATG\n")
            
            with open(genome_filepath + ".fai", 'w') as fp:
                fp.write("chr1\t15\t5\t15\t16")
            
            genome_file = FastaFile(genome_filepath)
            
            py_ed_tool = EdTool(regions_filepath)

            py_ed_tool = py_ed_tool.sequence(
                fi= genome_filepath,
                vcf=vcf_filename
            )
            sequences = py_ed_tool.sequences
            self.assertEqual(sequences[0], "TTGATGATGA")

