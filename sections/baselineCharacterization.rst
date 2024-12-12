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

+------------+--------------+------------------+
|  Run Type  | SLAC IR2 Run | Cerro Pachón Run |
+============+==============+==================+
| B Protocol |    13557     |      E1071       |
+------------+--------------+------------------+
|    PTC     |    13591     |       E749       |
+------------+--------------+------------------+

Among all of these measurements, there is particular concern that they have not degraded between the SLAC IR2 run in November 2023 and the Cerro Pachon run in October 2024.


Bias metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Charge transfer inefficiency
"""""""""""""""""""""""""""""""""
CTI, or charge transfer inefficiency, measures the fraction of charge that fails to transfer from the image area to the readout register during image readout. Consequences of high CTI include loss of charge, distorted signals in the direction of the parallel register, and reduced sensitivity in low light imaging.
In the context of LSSTCam, we measure CTI along both the serial and parallel registers. 

Serial CTI 
"""""""""""


Parallel CTI
"""""""""""""



..
  Bias Stability?

Dark metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dark current
"""""""""""""
Dark current is the small amount of electrical charge generated in the absence of light due to thermal activity within the CCD’s semiconductor material. This effect occurs when thermal energy causes electrons to be released from atoms in the CCD, mimicking the signal that light would produce. Dark current increases with temperature, so cooling the CCD is a common method to reduce it in sensitive imaging applications. Dark current introduces noise into an image, degrading its quality, particularly in low-light conditions or long exposures.
In the context of LSSTCam, we measure dark current from the combined dark images across all amplifiers.


Bright defects
"""""""""""""""
Bright defects are localized regions or individual pixels that produce abnormally high signal levels, even in the absence of light. These defects are typically caused by imperfections in the CCD’s semiconductor material or manufacturing process. Bright defects can manifest as “hot pixels” (pixels with consistently high dark current), small clusters of pixels with elevated output, or as "hot columns" (pixels along the same parallel register that have high dark current).
In the context of LSSTCam, we extract bright pixels from the dark current, with the threshold for a bright defect set at 5 e- / pix / s, above which the pixel is registered as a bright defect.


Stability flat metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..
  Gain stability? Or would we use the gain stability runs to describe this?


Flat pair metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. 
  Add a figure of the PTC from the SLAC IR2 run and the CP run

Linearity and PTC turnoff
"""""""""""""""""""""""""""
Linearity turnoff and PTC turnoff are two closely related metrics used to characterize the upper limit of the usable signal range for accurate imaging. 
Linearity turnoff is the point at which LSSTCam deviates from linearity in the PTC curve. In our case, the deviation threshold is 2%.
PTC turnoff refers to the high signal region of the PTC where the PTC begins to decrease noise for higher flux. This is due to blooming and saturation within the CCDs.
While slightly different, both metrics provide important information about the upper limits of the dynamic range in our sensors.

Maximum observed signal
"""""""""""""""""""""""""""


PTC Gain
""""""""""""
PTC gain is the conversion factor between the number of electrons generated in the CCD's pixels and the digital output signal. It is one of the key parameters derived from the Photon Transfer Curve, as it is the slope from where the noise is dominated by shot noise. Gain is expressed in e- / ADU, and quantifies how effective the CCD's analog signal is digitized. 

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
Dark defects are localized regions or individual pixels that produce abnormally low signal levels, even in the presence of light. These defects are typically caused by imperfections in the CCD’s semiconductor material or manufacturing process.
In the context of LSSTCam, we extract dark pixels from combined flats, with the threshold for a dark defect set to a 20% deviation from flatness.



Persistence
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Differences from previous runs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


..
  table here showing the metrics and their comparison to IR2 metrics

..
  currently we do not use different LED flats for analysis - should we make mention of them at all?
