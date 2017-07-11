# To RUN: python3 Script_2_run_snpEff.py HTMLOutput VCFSNVsInput VCFSNVsOutput

import os
import sys

HTMLOutput = sys.argv[1]
VCFSNVsInput = sys.argv[2]
VCFSNVsOutput = sys.argv[3]

os.system('java -Xmx4g -jar snpEff.jar -v -stats {} mm10 {} > {}'.format(HTMLOutput, VCFSNVsInput, VCFSNVsOutput))
