Run 7 Optical modifications
############################################

For Run 7 there were a few changes with our setup on Level 3 as compared to Run 6 taken in IR2 at SLAC. 
One of the changes was that we did not have access to the CCOB Narrow/Thin beam. 
.. While the set up was on Level 3, we did not have the resources or expertise to get it setup. 
As such, the majority of the testing was done with the CCOB Wide Beam projector. 
We did obtain an additional projector, the 4k projector, part way through Run 7 that will be discussed later. 
With the CCOB Wide Beam, we used a cone attached to the L1 cover as well as shroud to create a dark environment as seen below. 

This allowed us to operate on Level 3 with a dark current of <0.1 ADU/sec with the shutter open. 
The initial set up of the CCOB Wide Beam was the same as Run 6, we had a minimal ND filter (10 %) attached to a C-mount lens. 
One change was that the f/stop of the lens was changed from 2.6 to 1.6 (fully open). 
This was done to try and reduce the effect of the 'weather' and the 'CMB patten' two effects that we found in Run 6 and were found to be due to our projection setup (see [Banovetz2024]_), 
While changing it did reduce the weather pattern, it also caused a much steeper roll off across the focal plane. 
The below figures show the weather pattern as compared to Run 6 and the rolloff of the light as compared to Run 6.

.. list-table:: 

    * - .. figure:: sections/figures/Camera_Shroud.jpg

         Final shroud configuration of LSSTCam in Level 3 to reduce light leaks.
    
      - .. figure:: sections/figures/CCOB_Wide_Shroud.jpg

         CCOB Wide Beam attached to the cone and shrouded.

.. figure:: sections/figures/Run7_DiffuserIllumination.png

    Illumination across the focal plane from Run 7 with the diffuser () as compared to Run 6 ().

To both reduce the effect of the 'weather' and 'CMB' but retain uniform illumination across the focal plane, we installed a diffuser in the cone attached to L1.
Below shows the placement of the diffuser along the cone. 

.. figure:: sections/figures/Diffuser.jpg

        Diffuser installed into the light cone.

The diffuser combined with a fully open F/stop effectively reduced the incoming light by roughly 35%. 
Adjusting for that, we found that it severly reduced the 'weather' and eliminated the CMB pattern, as well as fully illuminateing the focal plane. 
Below shows the effect of the diffuser in regards to the weather, CMB, and the overall illumination of the focal plane. 

.. list-table:: 

    * - .. figure:: sections/figures/Run6_Weather.png

         Full focal plane image showing the fractional difference in Run 6.
    
      - .. figure:: sections/figures/Run7_WeatherDiffuser.png

         Full focal plane image showing the fractional difference in Run 7.

.. figure:: sections/figures/Run7_DiffuserIllumination.png

    Illumination across the focal plane from Run 7 with the diffuser () as compared to Run 6 ().

The diffuser was installed for all B protocol and PTC runs moving forward, only being taken out for pinhole projection and when using the 4K projector.

The newest addition to the projectors used for EO testing was a 4K projector, simliar to those used in conference rooms. 
This projector was first tested at SLAC before coming to Chile around half through Run 7. 
This was used primarily as a spot projector, as the pinhole filter wasn't operational but more importantly, this could illuminate all 3206 amplifiers instead of the 21 illuminated by the pinhole projector. 
Most runs included the spots and the spot fluxes were controlled by the shutter instead of any flashing (e.g. CCOB Wide). 
One downside that was found was that the illumination of 'dark' regions (regions not supposed to be illuminated) were still giving off light. 
This background region had structure that changed with time and could not be easily subtracted. 
It also caused the contrast between the spot and the background to be around 6. 
Changing the shape to large rectangles for crosstalk measurements increased this contrast to 30.

.. [Banovetz2024] https://ui.adsabs.harvard.edu/abs/2024arXiv241113386B/abstract
