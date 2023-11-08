#! /bin/bash

for i in {1..200}; do
    bash scripts/magic123/run_both_priors.sh 0 nerf dmtet /data/sandor/images/monopointcloud/multiview/reconstruction 1 0
done
