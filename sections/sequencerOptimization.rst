Sequencer Optimization
#################################

Sequencer files have undergone evolution for both ITL and e2v versions. The latest sequencer file from Run 6 was the v26_noRG version for ITL and the regular v26 for e2v. The suffix _noRG indicates that the RG bit is not toggled during parallel transfer. This modification appears to enhance the stability of the bias structure for most ITL amplifiers.

During Run 7, several changes were implemented, as described below:

- v27 incorporated guider functionalities, including ParallelFlushG and ReadGFrame. However, the noRG change was inadvertently included. Consequently, we abandoned this version and switched to v28.
- v28 sequencer files merged v26_no_RG and v27. https://rubinobs.atlassian.net/browse/LSSTCAM-5
- v29 introduced changes to speed up the guider. https://rubinobs.atlassian.net/browse/LSSTCAM-34
- v30 primarily focused on e2v. We introduced a new approach to NopSf for e2v sensors https://github.com/lsst-camera-dh/sequencer-files/pull/17. To align timing with the ITL version, a change was made.  https://github.com/lsst-camera-dh/sequencer-files/pull/18

This section describes sequencer optimization.

- CCD clear conclusions

  The complete discussion is given in `Improvement of Clear CCD <https://sitcomtn-148.lsst.io/#serialRemnants>`__ but here is a summary:
  
  - **No Pocket** 

  We introduced the V29_NoP (No Pocket) sequencer, which is an improved clear with a serial register configuration that reduces the creation of pockets at the Image/Serial register interface. This clear shown a factor ~2 improvement in saturated image clear for e2v, and fully solved the problem for ITL, except for R01_S11 for which the result with No Pocket appends to be worse by a factor 2 than with the default clear. This ITL ccd presents for a not understood reason, a large quantities of uncleared charges(100's of lines) after a saturated flat. This issue prevents to use the No Pocket configuration with ITL. 

  - **No Pocket with Serial flush**

  We introduced in V29_NoPSF ( No Pocket with Serial Flush), an improved version of the No Pocket Clear sequencer, including a variable configuration of the Serial register during the clear (mimicking a serial flush), to further prevent the formation of pockets. This solution has been shown to completely prevent the presence of leftover charges after the clear of a saturated image for e2v devices.


   **No Pocket with Serial flush** is now the default clear method for e2v devices starting with V30. Until a solution is found for clearing saturated images in R01_S10, the initial clear method (Serial phases always up) will remain the default for ITL devices.
  
- Overlap conclusions

- e2v "No RG" conclusions


  
