Bias stability
############################################
Bias instabilities (typically above the 1-ADU level) are observed over a significant number of sensors for both ITL and e2v CCDs. The main issues are referred as :

#. The ITL bias jumps : large variation of the column-wise structure from exposure to exposure.
#. The e2v yellow corners : residual 2D shape of the bias even after 2D-overscan correction. These residuals depend on the acquisition sequence and of the exposure time.
   
Both issues were observed and deeply studied in Run 6 EO data. The ITL issue is thought to be an hardware-level issue (phase shifts between Readout Electronics Boards). We tried to mitigate the e2v issue by optimizing the acquisition configuration in Run 7.

For the baseline acquisition configuration (see conclusion), three relevant stability runs were recorded :

#. Run E2136 : 15-s darks with some very long delays throughout the run
#. Run E2236 : 50 15-s darks, 50 biases recorded with 30-s delays between exposures
#. Run E2330 : 15-s and 30-s darks with variables delays between exposures

To process these runs, the eo_pipe bias stability task is used : for the ISR part, a serial ('mean_per_row') overscan correction and a bias subtraction (computed from the corresponding B-protocol run) are applied. The final data product is the mean of the per-amplifier science image over the full set of exposures of the run. Two typical examples are shown in the figures below.

.. figure:: sections/figures/E2136_R21_S21.png

   Stable case (R21 S21)

.. figure:: sections/figures/E2136_R23_S22.png

   Instable case (R23 S22)

A comparison of the results for an instable CDD is shown below for the three runs.

.. list-table::

    * - .. figure:: sections/figures/E2136_R33_S02.png

           Run E2136, R33 S02

      - .. figure:: sections/figures/E2236_R33_S02.png

           Run E2236, R33 S02

      - .. figure:: sections/figures/E2330_R33_S02.png
  	   
	   Run E2330, R33 S02

In order to highlight the 2D shape differences, a 2D-overscan correction is applied. A few exposures illustrating the variations of the 2D shape for an instable CCD are shown below.

.. figure:: sections/figures/E1880_bias_R33_S02.png

   Bias exposure, run 1880, R33 S02

.. figure:: sections/figures/E2136_dark15_R33_S02.png
	    
   15-s dark exposure, run E2136 in 'stable' conditions, R33 S02	   
	   
.. list-table::

      * - .. figure:: sections/figures/E2136_dark15_delay_R33_S02.png

	   15-s dark exposure, run E2136 after a 3-minute delay, R33 S02

        - .. figure:: sections/figures/E2330_dark30_R33_S02.png

           30-s dark exposure, run E2330, R33 S02

In order to quantify the number of e2v instable amplifiers, a stability metric *d* is defined from the eo_pipe stability task data products. More precisely, *d* is defined, for a given amplifier in a given run, as the difference between the 5th and 95th percentiles of the image mean over all the exposures. The distribution of *d* for run E2136 is shown below. Applying a threshold at 0.3, 51 amplifiers are identified as instable (see the corresponding mosaic).

.. figure:: sections/figures/E2136_distribution_d.png

   Distribution of the stability metric for the 1872 e2v amplifiers in run E2136

.. figure:: sections/figures/E2136_mosaic_d.png

   Mosaic of e2v amplifiers identified as instable in run E2136
	   
Further studies are still required in order to converge on the best mitigation strategies for the start of the LSST survey.
