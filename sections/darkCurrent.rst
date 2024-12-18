Dark current and light leaks
############################################

This section describes dark current and light leaks in Run 7 testing.


Light leak mitigation with shrouding the camera body
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
One of the first tests we attempted with the camera was measuring dark current and sources of light leaks in the camera body.
This began by finding gaps between the L1 cover and the gaskets.
This was covered up by tape where we felt comfortable applying it.
Below shows the gaps that we could see between L1 and its cover.

.. figure:: sections/figures/Camera_Shroud.jpg

Once these were sealed, we took some intital measurements and then started to cover the camera body with shroud.
We also found light leaks where the light cone attached to L1 was housed, and from the utility trunk.
Below is the table of observations, their corressponding dark current, and comments on what changed.

.. _light_leak:

.. table:: Table showing the different 15 second dark exposures, the different conditions, and the resulting dark current.

    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | Exposure             | Dark Current  | Room Lights | Shutter          | Comments                                                  |
    +======================+===============+=============+==================+===========================================================+
    | MC_C20240909_000012  | 0.158         | Off         | Closed           |                                                           |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240909_000018  | 0.158         | On          | Closed           |                                                           |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240909_000038  | 2.94          | On          | Open             | Initial Covering (just the CCOB cone and around the L1    |
    |                      |               |             |                  | cover)                                                    |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240909_000054  | 1.34          | On          | Open             | Initial Covering + Blanket over the FCS                   |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240909_000072  | 0.41          | On          | Open             | Initial Covering + Blanket over AND under the FCS         |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240909_000078  | 0.18          | Off         | Open             | Initial Covering + Blanket over AND under the FCS         |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+
    | MC_C20240910_000031  | 0.033         | On          | Open             | Initial Covering + Blanket over AND under the FCS + UT    |
    +----------------------+---------------+-------------+------------------+-----------------------------------------------------------+


Below is a the image of the final shroud configuration covering the camera.

.. figure:: sections/figures/Camera_Shroud.jpg

        Final shroud configuration of LSSTCam in Level 3 to reduce light leaks.

Successful Autochanger Light Leaks masking
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A dedicated dark/light leak study was performed during the Run 6 at SLAC in summer 2023 and a localized faint light source
going up to ~ 0.04 e-/s/pixel was associated to the 24 V Clean of the FES auto-changer.

In the Auto-Changer this voltage is used to power some probes and all controllers. In february 2024, as AC-1 was extracted from the camera for a global maintenance, a
direct investigation to localized the light source was performed without success. A light source in the AC wasn't expected as in the AC all controllers LED have been removed, and most electronics are in "black boxes". Still two
small probes , which had LEDs that could not be removed, were initially masked by a black epoxy. As we had doubt on the quality of this masking in the IR, we applied
and extra-making (aluminium black tape) on them during the Feb 2024 maintenance (on AC 1 and 2).

At the start of the Run 7 a new study of the light leak based on 900s dark exposures with the shutter open and the empty frame filter en place, showed that the AC light leaks was still present
( :ref:`see left plots of AC light leak <fig-ac-light-leak>` ). 
Following this finding, a full review of all the AC hardware powered by the 24 V dirty was performed, and a candidate was found : the coders of the 5 main motors of the AC had a partial documentation from the vendor not mentioning
the presence of LED. After interaction with the vendor the presence of ~700nm LEDs incide the coders were reported. The hypothesis of ~700nm LED source has been found compatible with the observation as no AC light leaks were detected
using the different filters in camera at the start of Run 7 (g,r and y filters) .  
A dedicated test in Paris using an AC spare coder and a precision photometric set-up allowed to identify leak in the masking of those LED in the vendor packaging. A complementary masking method based on a 3D printed part + tape + cable tie  was qualified in Paris: it is masking the light leak and it is safe (all parts correctly secured ).

In November 2024, we masked all the lights in the back of level 3 clean room ( not the part with the camera) to setup a high quality dark room allowing a direct observation with a CMOS camera of the light leak on the AC2 motors coders. Also the level of darkness reached, allowed us to validate the quality of the AC coders light masking.
Notice that the FES-prototype in Paris doesn't have coder on the Online Clamps, so we had to tune/qualify directly on the AC2 at summit the masking of those coders.

For each AutoChanger (1 & 2), the 5 motors coders with vendor issue on their LED masking, have been successfully enveloped in a light tight mask.

Notice that the AC was off starting the Sep 27th at 21:15 UTC in the first part of the Run 7.
For the end of Run 7 (run taken after mid-November) the AC was back On: as the AC 1 was back in camera with the new coders light mask in place, we were able to take a new series of 900s dark with AC On & off, confirming
that we had no light leak left associated to the Filter Exchange System. (:ref:`see right plots of AC light leak <fig-ac-light-leak>`)



 
.. image::   sections/figures/AC_LightLeak_study.png
   :name: fig-ac-light-leak
   :alt:  *The left plot shows the original impact of the AC light leak on 900s dark ( AC On - AC off). On the right plot, after masking the AC LED coders, no light associated to the FES is present.*  

*The left plot shows the original impact of the AC light leak on 900s dark ( AC On - AC off). On the right plot, after masking the AC LED coders, no light associated to the FES is present in 900s dark difference( FES On - FES off).*  

Shutter condition impact on darks
"""""""""""""""""""""""""""""""""


Filter condition impact on darks
"""""""""""""""""""""""""""""""""


Final measurements of dark current
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


