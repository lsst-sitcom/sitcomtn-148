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

..
  table here showing the density of flat pairs in a B protocol vs a dense

All EO camera data is processed through the `calibration products <https://github.com/lsst/cp_pipe>`__ and `electro-optical <https://github.com/lsst-camera-dh/eo_pipe/tree/main>`__ pipelines to extract key metrics from the data run. The key camera metrics from Run 7, and their comparison to previous runs are discussed below.

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

Row means variance
""""""""""""""""""""

Brighter-fatter correlation
""""""""""""""""""""""""""""


Brighter fatter a_00 coefficient
""""""""""""""""""""""""""""""""""


Linearity turnoff
"""""""""""""""""""


PTC turnoff
""""""""""""


Maximum observed signal
"""""""""""""""""""""""""""


PTC Gain
""""""""""""


PTC Noise
"""""""""""


Divisidero Tearing
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
