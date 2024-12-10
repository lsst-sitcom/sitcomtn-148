Improved  Clear 
############################################

In this section we will describe the work done during run 7 to improve the image
clear prior to collect a new exposure.

The problem we wanted to solve is the presence of  charges in the
first lines read of an image taken after a saturated image.
These "hard to clear" charges , are associated to highly saturated
flat  or column ( or stars as observed in AuxTel or ComCam), that  will  leave signal in the
first lines of the following exposure. We have the following signature
of the effect : 
- in all ITL CCD except in R01_S10 for which the effect is much more significant and that will be addressed later in this section:
  
    the first CCD line of the following exposure is ~ saturated and signal is also present in the 2nd line read of the CCD.
- in e2v CCD :
    the effect is slightly amplifier dependent , still  in most of
    the device a saturation is observed in the first xx CCD line read of
    the following exposure, and a
    significant signal is visible up to 40th line.


These left over electrons are not associated to what we usually
call residual image or persistence. They are suspected to be associated to pockets, induced by the
electric field configuration in the sensor and the field associated to
saturated pixels : in CCD location that allow the existence of such
pocket(s) during a clear, charges will stay in the pocket and will not be fully cleared. 
A change of the clocks configuration, can remove the pockets, and free
the charges allowing them to be cleared. In particular such charge
residuals if present in the first bias taken after a saturated image ,
are not present in the following bias : if the clocks configuration
used in our standard clear is not able to flush away those charges
/ destroy the pockets, a standard readout of >~ 2000 lines does remove them.   

The localisation of these uncleared electron in the first lines of the
CCDs, spot the interface between the image area and the serial register , as the location of those pockets.
For this reason we investigated changes in the field configuration of
the serial register during the clear, to avoid the construction of
pockets at this image-serial register interface. 

.. image::   /figures/plots_R12_S20_C15_E1880_bias_2024103000303.png
   :target:  .. /figures/plots_R12_S20_C15_E1880_bias_2024103000303.png
   :alt: Figure showing the impact of the various type of clear on a bias taken after a saturated flat for an E2V sensor 

   In this images , we can see for 3 type of sequencer ( from left to right : V29 , NoP and NopSF), a zoom on the first lines of an e2v amplifier ( here R12_S20 C10) shown as a 2D image ( top plots) or with the mean signal per line (bottom plots).  A bias taken just after a saturated flat in a e2v
   CCD will show a residual signal in the first lines when using the default clear (left images,clear=v29 ) : the first line has an almost saturated signal ( ~ 100 kADU here), and a significant signal is seen up to the line ~50 here. In practice, in  function of the amplifier, signal can be seen up
   to line 20-50. When using the NoP clear (central plots), we can already see a strong reduction of the unclear charges still present in the first acquired bias after a saturated flat. The NoPSF clear fully clear the saturated flat , and no uncleared charges are observed  in the following bias.    




 .. _table-SummaryClear:

.. table:: This table summaries the different clear methods used so
	   far . .

    +------------------------+------------+----------+-------------+----------------+-----------------+-------------------------+--------+-------+ 
    |                                                  | Default Clear    | Multi Clear    |     Multi Clear    | Deep Clear                | No Pocket  (NoP)        |  No Pocket Serial Flush (NoPSF) | Header 3  | Header 4 |
    |                                                  |      1 Clear         |      3 Clears    |      5 Clears      |     Clear +1 Line        |    1 Clear                    |             1 Clear                           |                |                 |
    |                                                  |   (seq. V29 )       |   (seq. V29 )   |      (seq. V29 )  |      (Seq. V23 DC)       | (seq. V29_NoP)           |   ( seq.  V29, V30 )                     |                |                 |
    +===================+==========+==========+========+=============+==============+====================+======+======+
    | Clear duration                            | 65.5 ms            | 196.5 ms       | 327.4 ms      |   64.69 ms                 |     65.8 ms                   |   67 ms                                       |               |                   | 
    +===================+==========+==========+==========+==========+================+===================+======+=======+
    | "E2V" after saturated Flat           |                          |                         |                           |                                 |                            |                                       |              |                     |
    +------------------------+------------ +                        |                           +----------------+-------------+-------------------+-------+---------+
    | R30_S10_C10 E2V                       |                         |                         |                            |                                 |                            |                                       |              |                     |
    |         Bright Column (~ sat. Star) |                         |  No residual e-  | No residual e-   |                                 |                            |                                       |              |                     |
    +===================+==========                        |                     +==========+===========+==========+==========+==========+
    | "ITL" after saturated Flat           |                        |    in following  |     in following   |                                 |                            |                                       |              |                     |
    +------------------------+------------+                       |                    +----------------+-------------+-------------------+-------+---------+
    | R02_S20_C14 ITL                        |                         |       image  |     image             |                                 |                            |                                       |              |                     |
    |Bright Column (~ sat. Star)         |                            |                     |                        |                                 |                            |                                       |              |                     |
    +===================+==========+==========+==========+==========+===========+==========+==========+==========+
    | R01_S10  ITL "unique"              |                        |                         |                     |                                 |                            |                                       |              |                     |
    +------------------------+------------+------------+----------+----------------+-------------+-------------------+-------+---------+
 



This section describes incomplete serial flush.

- Background
- Mitigation with sequencers
- discussion of different clears
