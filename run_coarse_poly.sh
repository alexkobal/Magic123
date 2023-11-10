#! /bin/bash
num=$1
for i in {1..num}; do
    bash scripts/magic123/run_both_priors.sh 0 nerf dmtet /data/sandor/images/monopointcloud/multiview/reconstruction 1 0
done
