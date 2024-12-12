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

.. list-table:: 

    * - .. figure:: sections/figures/E2136_R21_S21.png

           Stable case (R21 S21)

      - .. figure:: sections/figures/E2136_R23_S22.png

           Instable case (R23 S22)

A comparison of the results for an instable CDD is shown below for the three runs.

.. list-table::

    * - .. figure:: sections/figures/E2136_R33_S02.png

           Run E2136, R33 S02

      - .. figure:: sections/figures/E2236_R33_S02.png

           Run E2236, R33 S02

      - .. figure:: sections/figures/E2330_R33_S02.png
  	   
	   Run E2330, R33 S02

#. Some yellow corner images (bias, 15-s exposure, 30-s exposure)
#. Mosaic of stability metric

Discussion  about the possible mitigation strategies 
