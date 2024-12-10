Sequencer Optimization
#################################

Sequencer files have been evloved for both ITL and e2v versions. The latest sequencer file from Run 6 was the v26_noRG version for ITL and the regular v26 for e2v. The suffix _noRG indicates no toggling of RG bit during the parallel transfer. This seems to have an impact on making the bias structure stable for most of the ITL amplifiers.
During Run 7 period, a number of changes has been made as described below:

- v27 has changes incorporating guider functionalities such as ParallelFlushG, ReadGFrame. However, the noRG change didn't get included accidentally. We abandaned this version and switched to v28.
- v28 sequencer files merges v26_no_RG and v27 https://rubinobs.atlassian.net/browse/LSSTCAM-5
- v29 has changes for speeding up guider https://rubinobs.atlassian.net/browse/LSSTCAM-34
- v30 has changes in mostly e2v. We introduced another way of NopSf for e2v sensors https://github.com/lsst-camera-dh/sequencer-files/pull/17. To make timing matched the ITL version has a change https://github.com/lsst-camera-dh/sequencer-files/pull/18.

This section describes sequencer optimization.

- No-pocket conclusions
- Serial flush conclusions
- Overlap conclusions
