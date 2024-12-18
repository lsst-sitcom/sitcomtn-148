Persistence optimization
############################################

Leftover signal in the following dark after a blast of illumination has been observed. It is called "Persistence". 
Persistence has been observed in an early prototype E2V sensor as early as 2014 ([D2014]_). It was confirmed that the amplitude of the persistence decreased as the parallel swing voltage got smaller. This is consistent with the Residual Surface Image [J2001]_ -- the excessive charges are being stuck at the surface layer. The level of persistence is about 10--20 ADU, and the decaying time constant is about 30 sec [dmtn-276]_.

During the EO testing in 2021, we also found the persistence made a streak toward the readout direction from the place where the bright spot located in a previous image. We call this trailing persistence.

E2V sensors have another major problem, so-called "tearing", which is considered a consequence of the non-uniform distribution of holes. Our primary focus in the optimization was given to mitigate the tearing over years, and we have successfully eliminated the tearing by bringing the E2V voltage from the unipolar voltage (both parallel rails high and low are positive) to the bipolar voltage (the parallel high is positive, and the low is negative) following the formula [Bipolar]_. However, the persistence issue still remained unchanged.

For the persistence issue, if this is the residual surface image, two approaches could be taken as discussed in [U2024]_. Either 1) establishing the pinning condition where the holes make a thin layer at the front surface so that the excessive charges recombine with the holes or 2) narrowing the parallel swing so that the accumulated charges in the silicon do not get close to the surface state. 

The pinning condition could be established by bringing the parallel low voltage down as low as -7V or lower. The transition voltage needs to be empirically determined. However, E2V pointed out that the measured current flow increases as the parallel low voltage goes low, which increases the risk of damaging the sensor by making a breakdown [1]_. Also, the excessive charges could get recombined by the thin layer of the holes, which could disturb the linearity at the high flux end where charges start to interact with the holes. 

The parallel swing determines the fullwell. Depending on whether the accumulated charges spread over the columns or interact with the surface layer, there are blooming fullwell regimes and the surface fullwell regime. The fullwell between these two regimes is considered as the optimal fullwell [J2001]_, where we don't have persistence and as high dynamic range as possible. Seeing the persistence, we likely operate the sensor in the surface fullwell condition and we need to go to a narrower voltage to get the blooming fullwell or the optimal fullwell. The obvious downside is to narrow the fullwell. 

The voltages are defined relative to each other. Changing the parallel swing (for example) also requires changes to all other voltages to operate the sensor properly, for example, properly reset the amplifier. The initial voltage was given in the original formula [Bipolar]_ but to go to the narrow voltage we had to switch to the new formula in order to satisfy constraints [PersistenceMitigationVoltage]_. 

[S2024]_, set up a single sensor test-stand at UC Davis. They attempted multiple different approaches mentioned above and reported the results [DavisReport]_. The summary is as follows:

- The new voltages following the rule work fine. 
- Narrowing the parallel swing eliminates the persistence.
- Lowering the parallel low voltage didn't seem to work as we expected; the going further negative voltage is probably needed.

Note that the UCD setup didn't show up the persistence. It might be due to the characteristic of the sensor, or might be due to the difference in the electronics (the long cable between CCD and REB, for example). They need to move the parallel rails up. 

.. [1] We note that ITL operates at the parallel low voltage of -8V. We have observed the increased current flow. But we have the software protection so that the current flow does not go too high. 
.. [dmtn-276] https://dmtn-276.lsst.io
.. [Bipolar] https://github.com/lsst-camera-dh/mkconfigs/blob/master/newformula.py
.. [PersistenceMitigationVoltage] https://github.com/lsst-camera-dh/e2v_voltages/blob/main/setup_e2v_v4.py
.. [DavisReport] https://docs.google.com/document/d/1V4o9tzKBLnI1nlOlMFImPko8pDkD6qE7jzzk-duE-Qo/edit?tab=t.0#heading=h.frkqtvvyydkr
.. [J2001] https://www.spiedigitallibrary.org/ebooks/PM/Scientific-Charge-Coupled-Devices/eISBN-9780819480392/10.1117/3.374903
.. [D2014] https://ui.adsabs.harvard.edu/abs/2014SPIE.9154E..18D/abstract
.. [U2024] https://ui.adsabs.harvard.edu/abs/2024SPIE13103E..0WU/abstract
.. [S2024] https://ui.adsabs.harvard.edu/abs/2024SPIE13103E..21S/abstract 

Persistence optimization
^^^^^^^^^^^^^^^^^^^^^^^^

Based on this test result, we decided to try out the new voltage with the narrower voltage swing on the main camera focal plane. Keeping the parallel low voltage at -6V in order to operate the sensor safely (very conservative limit), we changed the parallel swing voltage from 9.3V to 8.0V as well as all the other voltages using the new formula. We overexposed CCDs and took 20 darks after.
The image shown below is the mean or median of pixel-by-pixel difference between the first and the last dark exposures, as a function of the parallel swing. As the parallel swing is lowered, the residual signal becomes small; it becomes roughly 10 times lower than the original 9.3V. Although we sampled midpoints between 8.0 and 9.3V, 8.0V appears to work the best and could be lower with the penalty of losing the full well.

.. figure:: sections/figures/e2v_transient_dark_vs_dp.png

    The remaining charges measured in every amplifier but aggregated by mean or median as a function of the parallel clock swing are shown.

The following figures display how the persistence is reduced by the voltage change. The images were processed by the standard instrumental signature removal and get assembled in the full focal-plane view. The dark exposure was taken right after the 400ke-equivalent flat exposure. The figure shows the distinct pattern of elevated signal associated with the vendor. The inner part of the focal plane is filled by e2v sensors which have the persistence signal.

.. figure:: sections/figures/E1110dp93.png

    The first dark exposure after a 400k flat image under the parallel swing of 9.3V (Run E1110).

The next figure shows the same dark exposure but taken with the narrow parallel swing voltage of 8.0V. The distinct pattern goes away. This demonstrates the persistence in e2v sensors becomes the level of ITL's ones.


.. figure:: sections/figures/E1314dp80.png

    The first dark exposure after a 400k flat image under the parallel swing of 8.0V (Run E1314). The figure shows no distinct patterns from persistence in e2v sensors anymore.

Impact on full-well
^^^^^^^^^^^^^^^^^^^^^^^^
Reduction of the full well is expected by narrowing the parallel swing voltage. This subsection explores how much reduction in the PTC turnoff is observed in the dense PTC run. Two runs are acquired with identical setting except for the CCD operating voltage (E1113 for 9.3V and E1335 for 8.0V). As the PTC turnoff is defined in ADU, it needs to be multiplied by PTC_GAIN to make a comparison. The figure below compares the PTC turnoff in electrons and their difference in ratio. The median reduction was 22% .

.. figure:: sections/figures/PtcTurnoffRatio.png

    Histograms of the PTC turn offs (left) and the ratios of differences (right) between E1113 (9.3V) vs E1335 (8.0V). The median of the reduction is 22%.


Impact on Brighter-Fatter effect
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Reducing the parallel swing is expected to enhance the brighter-fatter effect (BFE), possibly in an anisotropic way. The BFE can be characterized via the evolution of the variance and covariances of flatfield exposures as a function of flux.  In order to evaluate the impact of reducing the parallel voltage swing on e2v sensors, we acquired two series of flatfield exposures with the respective voltage setups and extracted the "area" coefficients 
the "area" coefficients (Equation (1) in [A2023]_) from these two data sets. The area coefficients describe by how much a unit charge stored in a pixel wil alter the area of some other pixel (or itself). We find that reducing the parallele swing from 9.3V to 8V typically increases the area coefficients by 10% (between 5 and 19% depending on distance), and the increase is almost isotropic (along serial and parallel directions). From these measurements, we anticipate that the increase of star sizes with flux will not become more isotropic at 8V than it was at 9.3V, and hence does not introduce new threats on the measurement of the PSF ellipticity

.. figure:: sections/figures/aScatterPlots8vs9.3.png

     Scatter plots of area coefficients (one entry per amplifier) measured at 8V and 9.3V. The 9 subfigures correspond to separations between the source of the area distortion and its victim, with the self interaction at the bottom left. The first neighbors increase respectively by 19% in the parallel direction by 14% in the serial direction. So the BFE is slightly larger at 8V but not significantly more anistropic. 

.. [A2023] https://arxiv.org/pdf/2301.03274

Summary
^^^^^^^
E2V sensors had persistence. We confirmed changing the E2V CCD operating voltage greatly reduced persistence. As penalties, we observed 22% of full well reduction, and a ~10% increase of the brightter-fatter effect, essentially in an isotropic way.




