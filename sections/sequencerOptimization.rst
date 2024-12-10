Sequencer Optimization
#################################

Sequencer files have undergone evolution for both ITL and e2v versions. The latest sequencer file from Run 6 was the v26_noRG version for ITL and the regular v26 for e2v. The suffix _noRG indicates that the RG bit is not toggled during parallel transfer. This modification appears to enhance the stability of the bias structure for most ITL amplifiers.

During Run 7, several changes were implemented, as described below:

- v27 incorporated guider functionalities, including ParallelFlushG and ReadGFrame. However, the noRG change was inadvertently included. Consequently, we abandoned this version and switched to v28.
- v28 sequencer files merged v26_no_RG and v27. https://rubinobs.atlassian.net/browse/LSSTCAM-5
- v29 introduced changes to speed up the guider. https://rubinobs.atlassian.net/browse/LSSTCAM-34
- v30 primarily focused on e2v. We introduced a new approach to NopSf for e2v sensors https://github.com/lsst-camera-dh/sequencer-files/pull/17. To align timing with the ITL version, a change was made.  https://github.com/lsst-camera-dh/sequencer-files/pull/18

This section describes sequencer optimization.

- No-pocket conclusions
- Serial flush conclusions
- Overlap conclusions
