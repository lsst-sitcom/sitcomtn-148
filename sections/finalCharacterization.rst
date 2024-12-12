Baseline characterization
############################################

Background 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Initial characterization studies performed on LSSTCam were used two primary acquisition sequences.

* B protocols: this acquisition sequence consists of the minimal set of camera acquisitions, including 

  * Bias images
  * Dark images
  * Flat pairs
  * Stability flats
  * Wavelength flats
  * A persistence dataset

* PTCs (photon transfer curves): this acquisition sequence consists of a sequence of flat pairs taken at different flux levels. The flat acquisition sequence samples different flux levels at a higher density than the B protocol flat sequence, enabling a more precise estimate of flat pair metrics. 

.. image::   /figures/PTC_BProtocol_Comparison.jpg
   :target:  ../figures/PTC_BProtocol_Comparison.jpg
   :alt: Figure showing the density of sampling between PTCs (blue) and B protocols (red)

All EO camera data is processed through the `calibration products <https://github.com/lsst/cp_pipe>`__ and `electro-optical <https://github.com/lsst-camera-dh/eo_pipe/tree/main>`__ pipelines to extract key metrics from the data run. The key camera metrics from Run 7, and their comparison to previous runs are discussed below.


For comparison between Cerro Pachon EO runs and the final SLAC IR2, the following runs are used.

+------------+--------------------------+--------------------------+
|  Run Type  | Initial Cerro Pachón Run | Final Cerro Pachón Run   |
+============+==========================+==========================+
| B Protocol |      E1071               |      E1071               |
+------------+--------------------------+--------------------------+
|    PTC     |       E749               |       E749               |
+------------+--------------------------+--------------------------+

Bias metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

CTI
""""""""""""


Bias stability
"""""""""""""""""


Dark metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dark current
"""""""""""""

Bright defects
"""""""""""""""


Stability flat metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gain stability
""""""""""""""""


Flat pair metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Linearity turnoff
"""""""""""""""""""


PTC turnoff
""""""""""""


Maximum observed signal
"""""""""""""""""""""""""""


PTC Gain
""""""""""""


Brighter fatter a_00 coefficient
""""""""""""""""""""""""""""""""""


Brighter-fatter correlation
""""""""""""""""""""""""""""


Row means variance
""""""""""""""""""""


PTC Noise
"""""""""""


Divisadero Tearing
"""""""""""""""""""""


Dark defects
""""""""""""""""


Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Differences from previous runs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


..
  table here showing the metrics and their comparison to IR2 metrics?


..
  currently we do not use different LED flats for analysis - should we make mention of them at all?
