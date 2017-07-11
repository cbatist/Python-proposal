# To RUN: python3 Script_1_run_strelka.py tumorBAMFile normalBAMFile referenceFile configFile outputDirectory

import os
import sys

tumor = sys.argv[1]
normal = sys.argv[2]
reference = sys.argv[3]
config = sys.argv[4]
outputDir = sys.argv[5]

os.system('configureStrelkaWorkflow.pl --tumor {} --normal {} --ref {} --config {} --output-dir {}'.format(tumor, normal, reference, config, outputDir))
os.system('make -C {} -j 2'.format(outputDir))
