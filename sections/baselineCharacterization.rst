Baseline characterization
#########################

Background 
^^^^^^^^^^

Initial characterization studies performed on LSSTCam were used two primary acquisition sequences.

* B protocols: this acquisition sequence consists of the minimal set of camera acquisitions, including 

  * Bias images
  * Dark images
  * Flat pairs - flats taken at varying flux levels
  * Stability flats - flats taken at consistent flux levels
  * Wavelength flats - flats taken in different LEDs
  * A persistence dataset - a saturated flat, followed by several darks

* PTCs (photon transfer curves): this acquisition sequence consists of a sequence of flat pairs taken at different flux levels. The flat acquisition sequence samples different flux levels at a higher density than the B protocol flat sequence, enabling a more precise estimate of flat pair metrics. 


.. image::   /figures/baselineCharacterization/PTC_BProtocol_Comparison.jpg
   :target:  ../figures/baselineCharacterization/PTC_BProtocol_Comparison.jpg
   :alt: Figure showing the density of sampling between PTCs (blue) and B protocols (red)


All EO camera data is processed through the `calibration products <https://github.com/lsst/cp_pipe>`__ and `electro-optical <https://github.com/lsst-camera-dh/eo_pipe/tree/main>`__ pipelines to extract key metrics from the data run. The key camera metrics from Run 7, and their comparison to previous runs are discussed below.


The naming of the EO runs was established during initial camera integration and testing. The final SLAC IR2 run from November 2023 was named "Run 6", while the data acquisitions from Cerro Pachon are considered "Run 7." Additionally, individual EO acquisitions are tagged with a run identifier. This is commonly referred to a Run ID. For all SLAC runs, the run identifier was a five digit numeric code, while the Cerro Pachon runs were "E-numbers" that started with a capital E followed by a numeric code. 

For comparison between Cerro Pachon EO runs and the final SLAC IR2, the following runs are used.

+------------+--------------+------------------+
|  Run Type  | SLAC IR2 Run | Cerro Pachón Run |
+============+==============+==================+
| B Protocol |    13557     |      E1071       |
+------------+--------------+------------------+
|    PTC     |    13591     |       E749       |
+------------+--------------+------------------+


Among all of these measurements, primary concern is that the camera has maintained its performance standards between the SLAC IR2 run in November 2023 and the Cerro Pachon run in October 2024.


Stability flat metrics
^^^^^^^^^^^^^^^^^^^^^^

Charge transfer inefficiency
"""""""""""""""""""""""""""""""""

CTI, or charge transfer inefficiency, measures the fraction of charge that fails to transfer from the image area to the readout register during image readout. Consequences of high CTI include loss of charge, distorted signals in the direction of the parallel register, and reduced sensitivity in low light imaging.
CTI measurements are made using the EPER method [EPER]_, which compares the ratio of the residual charge in the overscan pixels to the total signal charge in the imaging region. In the context of LSSTCam, we measure CTI along both the serial and parallel registers. 

Serial CTI 
""""""""""""

.. image::   /figures/baselineCharacterization/13557_E1071_SCTI_EF_43.png
   :target:  ../figures/baselineCharacterization/13557_E1071_SCTI_EF_43.png
   :alt: Figure showing the comparison between serial CTI measurements at SLAC and at Cerro Pachon

The CTI along the serial register is consistent between both Run 6 and Run 7. Both sensor types show extremely low CTI on the order of 1E-3 %, and differ on the order of ~2E-5 % for E2V sensors, and by ~4E-6 % for ITL sensors.

.. image::   /figures/baselineCharacterization/SCTI_13557_E1071_diff.png
   :target:  /figures/baselineCharacterization/SCTI_13557_E1071_diff.png
   :alt: The comparison between SCTI measurements at SLAC and at Cerro Pachon, taking the differences between measurements on a per amp basis. 



Parallel CTI
""""""""""""

.. image::   /figures/baselineCharacterization/13557_E1071_PCTI_EF_43.png
   :target:  ../figures/baselineCharacterization/13557_E1071_PCTI_EF_43.png
   :alt: Figure showing the comparison between parallel CTI measurements at SLAC and at Cerro Pachon


The CTI along the parallel register is consistent between both Run 6 and Run 7. Both sensor types show extremely low CTI on the order of 1E-5 %, and differ on the order of ~2E-7 % for E2V sensors, and by ~7E-6 % for ITL sensors.



.. image::   /figures/baselineCharacterization/PCTI_13557_E1071_diff.png
   :target:  /figures/baselineCharacterization/PCTI_13557_E1071_diff.png
   :alt: The comparison between PCTI measurements at SLAC and at Cerro Pachon, taking the differences between measurements on a per amp basis. 


Dark metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Dark current
"""""""""""""
Dark current is the small amount of electrical charge generated in the absence of light due to thermal activity within the CCD’s semiconductor material. This effect occurs when thermal energy causes electrons to be released from atoms in the CCD, mimicking the signal that light would produce. Dark current increases with temperature, so cooling the CCD is a common method to reduce it in sensitive imaging applications. Dark current introduces noise into an image, degrading its quality, particularly in low-light conditions or long exposures.
In the context of LSSTCam, we measure dark current from the combined dark images across all amplifiers.


.. image::   /figures/baselineCharacterization/13557_E1071_DARK_CURRENT_MEDIAN.png
   :target:  ../figures/baselineCharacterization/13557_E1071_DARK_CURRENT_MEDIAN.png
   :alt: Figure showing the comparison between dark current measurements at SLAC and at Cerro Pachon

Surprisingly, dark current was significantly lowered in Run 7 compared to run 6. Possible reasons for this could be improved shrouding conditions on the camera on Cerro Pachon compared to SLAC.

Bright defects
"""""""""""""""
Bright defects are localized regions or individual pixels that produce abnormally high signal levels, even in the absence of light. These defects are typically caused by imperfections in the CCD’s semiconductor material or manufacturing process. Bright defects can manifest as “hot pixels” (pixels with consistently high dark current), small clusters of pixels with elevated output, or as "hot columns" (pixels along the same parallel register that have high dark current).
In the context of LSSTCam, we extract bright pixels from the dark current, with the threshold for a bright defect set at 5 e- / pix / s, above which the pixel is registered as a bright defect.


.. image::   /figures/baselineCharacterization/13557_E1071_BRIGHT_PIXELS.png
   :target:  /figures/baselineCharacterization/13557_E1071_BRIGHT_PIXELS.png
   :alt: Figure showing the comparison between bright pixel measurements at SLAC and at Cerro Pachon

Reviewing the differences in bright pixels, we find consistent bright defect counts between Run 6 and Run 7. There appears to be a small excess of bright defects in Run 7.


.. image::   /figures/baselineCharacterization/BRIGHT_PIXELS_13557_E1071_diff.png
   :target:  /figures/baselineCharacterization/BRIGHT_PIXELS_13557_E1071_diff.png
   :alt: The comparison between bright pixel measurements at SLAC and at Cerro Pachon, taking the differences between measurements on a per amp basis. 

Taking the difference of defect counts on each amplifier, and separating the amplifiers by the detector manufacturer shows a small excess of bright defects in run 7 when compared to run 6. For ITL sensors, we find 12% of the amplifiers with more bright pixels than run 6. For E2V sensors, we find 4% of the amplifiers with more bright pixels than run 6. Despite this, the number of bright defects between runs does not increase for most sensors.

Flat pair metrics
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. image::   /figures/baselineCharacterization/run7PTCsToDate.jpg
   :target:  ../figures/baselineCharacterization/run7PTCsToDate.jpg
   :alt: Figure showing the comparison between PTC measurements at SLAC and at Cerro Pachon

Linearity and PTC turnoff
"""""""""""""""""""""""""""
Linearity turnoff and PTC turnoff are two closely related metrics used to characterize the upper limit of the usable signal range for accurate imaging. 
Linearity turnoff is the point at which LSSTCam deviates from linearity in the PTC curve. In our case, the deviation threshold is 2%.
PTC turnoff refers to the high signal region of the PTC where the PTC begins to decrease noise for higher flux. This is due to blooming and saturation within the CCDs.
While slightly different, both metrics provide important information about the upper limits of the dynamic range in our sensors. Linearity turnoff is measured in units of e-, while PTC turnoff is measured in ADU.


.. image::   /figures/baselineCharacterization/13591_E749_LINEARITY_TURNOFF.png
   :target:  ../figures/baselineCharacterization/13591_E749_LINEARITY_TURNOFF.png
   :alt: Figure showing the comparison between linearity turnoff measurements at SLAC and at Cerro Pachon

In our linearity turnoff measurements, we find close agreement between our Run 7 and Run 6 measurements. Both ITL and E2V sensors show tight agreement between results. 

.. image::   /figures/baselineCharacterization/LINEARITY_TURNOFF_E749_sensorType.png
   :target:  ../figures/baselineCharacterization/LINEARITY_TURNOFF_E749_sensorType.png
   :alt: Figure showing the comparison between linearity turnoff measurements at SLAC and at Cerro Pachon, separated by sensor type.

..
   PTC turnoff removed, because the results were very screwy. I suspect a processing problem


..
  Omitted Maximum observed signal, removed due to lack of relevance


PTC Gain
""""""""""""
PTC gain is the conversion factor between the number of electrons generated in the CCD's pixels and the digital output signal. It is one of the key parameters derived from the Photon Transfer Curve, as it is the slope from where the noise is dominated by shot noise. Gain is expressed in e- / ADU, and quantifies how effective the CCD's analog signal is digitized. 

.. image::   /figures/baselineCharacterization/13591_E749_PTC_GAIN.png
   :target:  ../figures/baselineCharacterization/13591_E749_PTC_GAIN.png
   :alt: Figure showing the comparison between PTC gain measurements at SLAC and at Cerro Pachon

PTC gain measurements agree extremely closely across all sensors in the focal plane.


Brighter fatter a_00 coefficient
""""""""""""""""""""""""""""""""""

This redistribution causes the charge to “spill” into adjacent pixels, effectively broadening the point spread function (PSF). 
The brighter fatter effect is the most dominant source of variance in the PTC curve. The brighter-fatter effect in CCDs refers to the phenomenon where brighter pixels appear larger (or “fatter”) than dimmer ones. This occurs due to electrostatic interactions within the CCD, when a pixel accumulates a high charge from incoming photons and creates an electric field that slightly repels incoming charge carriers into neighboring pixels. The brighter fatter effect can be modeled as the most dominant source of pixel-pixel correlations. Following the PTC model from [Astier]_, a00 describes the change of a pixel area due to its own charge content, or the relative strength of the brighter-fatter effect. 
Since same-charge carriers repel each other, this pixel area has to shrink as charge accumulates inside the pixel, which implies a00 < 0. In eo_pipe, an absolute value is taken of the a_00 parameter, so the measurements appear positive.


.. image::   /figures/baselineCharacterization/13591_E749_PTC_A00.png
   :target:  /figures/baselineCharacterization/13591_E749_PTC_A00.png
   :alt: Figure showing the comparison between PTC A_00 measurements at SLAC and at Cerro Pachon

Comparing the results on the strength of the brighter fatter effect, both runs are generally comparable. A few outliers exist across the focal plane, regardless of detector type. 

.. image::   /figures/baselineCharacterization/PTC_A00_13591_E749_diff.png
   :target:  /figures/baselineCharacterization/PTC_A00_13591_E749_diff.png
   :alt: A histogram showing the comparison between PTC A_00 measurements at SLAC and at Cerro Pachon, separated by detector type

However, the differences in brighter fatter strength between run 6 and run 7 show that the strength of the A_00 coefficient decreased for most of our outliers, which implies an improvement in focal-plane performance

..
  Removed Brighter-fatter correlation, Row means variance, PTC Noise, 

Divisadero Tearing
"""""""""""""""""""""
Divisadero tearing are large signal variations at amplifier boundaries. To quantify divisadero tearing, we measure the column signal, and compare it to the mean column signal from flat fields to quantify the amplitude of the effect, measured in a percent variation relative to the mean column signal value.

.. image::   /figures/baselineCharacterization/13557_E1071_DIVISADERO_TEARING.png
   :target:  /figures/baselineCharacterization/13557_E1071_DIVISADERO_TEARING.png
   :alt: Figure showing the comparison between divisadero tearing measurements at SLAC and at Cerro Pachon

Divisadero tearing in E2V CCDs appears higher in Run 7 than Run 6. ITL sensors are very consistent between runs.

.. image::   /figures/baselineCharacterization/DIVISADERO_TEARING_13557_E1071_diff.png
   :target:  /figures/baselineCharacterization/DIVISADERO_TEARING_13557_E1071_diff.png
   :alt: A histogram showing the difference between divisadero tearing measurements at SLAC and at Cerro Pachon

Run 7 shows a ~0.3% excess in divisadero tearing for E2V sensors, compared to an excess of ~0.1% excess in run 6 divisadero tearing for ITL sensors. 

Dark defects
""""""""""""""""
Dark defects are localized regions or individual pixels that produce abnormally low signal levels, even in the presence of light. These defects are typically caused by imperfections in the CCD’s semiconductor material or manufacturing process.
In the context of LSSTCam, we extract dark pixels from combined flats, with the threshold for a dark defect set to a 20% deviation from flatness.

.. image::   /figures/baselineCharacterization/13557_E1071_DARK_PIXELS.png
   :target:  /figures/baselineCharacterization/13557_E1071_DARK_PIXELS.png
   :alt: Figure showing the comparison between dark pixel measurements at SLAC and at Cerro Pachon

Dark pixels measures between SLAC and Cerro Pachon average ~1800 per amplifier, regardless of manufacturer. The reason for the high dark pixel counts is due to a picture-frame response near the edges of the sensors.

.. image::   /figures/baselineCharacterization/detector_85.jpg
   :target:  /figures/baselineCharacterization/detector_85.jpg
   :alt: Figure showing the picture frame masking of a typical detector, with the mask plane showed in yellow.


Due to the contamination of the edge frame response, it is difficult to extract useful information about the dark defects in the focal plane. The configuration for generating dark defects considers a border pixel region that is masked differently from the dark pixels. The default configuration has a border of zero. The largest region allowed for the picture frame region is 9 pixels, determined by LCA-19363. 
Due to incompatibility with the current pipelines, a direct comparison of a 9 pixel mask using run 6 data is not currently available. However, a 9 pixel mask can be applied to the Run 7 data. 

..
  Add 9 pixel mask statistics here

Add conclusion when pipelines on E1071 are complete

Persistence
^^^^^^^^^^^^^^^^

Persistence is a feature in LSSTCam where charge is trapped in the surface layer after high flux exposures [Persistence]_. Persistence is described in detail in the `persistence optimization section <https://sitcomtn-148.lsst.io/#persistence-optimization>`__. Here we will consider the measurements taken as part of a persistence measurement task in the typical B protocol.
For a persistence measurement, a high flux acquisition is taken, followed by a sequence of dark images. The persistence signal has been shown to decrease in subsequent dark images. To create a metric for persistence, one can take the difference between the residual ADU in the first dark image and the average of the residual ADU in the final dark images.


.. image::   /figures/baselineCharacterization/persistence_plot_LSSTCam_R22_S11_u_lsstccs_eo_persistence_E1110_w_2024_35_20240926T235141Z.png
   :target:  /figures/baselineCharacterization/persistence_plot_LSSTCam_R22_S11_u_lsstccs_eo_persistence_E1110_w_2024_35_20240926T235141Z.png
   :alt: Figure showing the residual ADU in R22_S11 for E1071, our first Run 7 B protocol. The persistence measurement is taken as the difference between the median in the blue box, and the median in the red box. 

In the initial run 7 measurements, we have not changed any operating parameters of LSSTCam, so we would expect persistence to still be present in the focal plane. 

.. image::   /figures/baselineCharacterization/13557_E1071_persist.png
   :target:  /figures/baselineCharacterization/13557_E1071_persist.png
   :alt: Figure showing the comparison between persistence measurements at SLAC and at Cerro Pachon

Both runs show a consistent persistence signal in E2V sensors. Several outliers exist with higher persistence signal in Run 7. The outliers in these measurements are due to higher initial persistence signal measurements, resulting in an excess of ~5 ADU when comparing run 6 with run 7.


.. image::   /figures/baselineCharacterization/persistence_plot_LSSTCam_R12_S21_u_lsstccs_eo_persistence_E1071_w_2024_35_20240925T180602Z.png
   :target:  /figures/baselineCharacterization/persistence_plot_LSSTCam_R12_S21_u_lsstccs_eo_persistence_E1071_w_2024_35_20240925T180602Z.png
   :alt: Figure showing the persistence measurements for R12_S21 taken at Cerro Pachon

.. image::   /figures/baselineCharacterization/persistence_plot_LSSTCam_R12_S21_u_lsstccs_eo_persistence_13557_w_2023_41_20231118T050437Z.png
   :target:  /figures/baselineCharacterization/persistence_plot_LSSTCam_R12_S21_u_lsstccs_eo_persistence_13557_w_2023_41_20231118T050437Z.png
   :alt: Figure showing the persistence measurements for R12_S21 taken at SLAC

Differences from previous runs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I will add this once we have agreed upon the set of parameters important for characterization

..
  table here showing the metrics and their comparison to IR2 metrics



.. [Persistence] https://dmtn-276.lsst.io/

.. [Astier] https://www.aanda.org/articles/aa/abs/2019/09/aa35508-19/aa35508-19.html 

.. [EPER] https://www.spiedigitallibrary.org/journals/Journal-of-Astronomical-Telescopes-Instruments-and-Systems/volume-7/issue-4/048002/Characterization-and-correction-of-serial-deferred-charge-in-LSST-camera/10.1117/1.JATIS.7.4.048002.full 


