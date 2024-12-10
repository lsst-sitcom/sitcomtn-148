Improved  Clear 
############################################


Overview
^^^^^^^^^^^^^

In this section we will describe the work done during run 7 to improve the image
clear prior to collect a new exposure.

The problem we wanted to address is the presence of residual charges in the
first lines read for image taken just after the clear of a saturated image.
These "hard to clear" charges , are associated to highly saturated
flat  or column(s) ( or stars as observed in AuxTel or ComCam), that leave signal in the
first lines of the following exposure. We have the following signature
of the effect : 

- in all ITL CCD (except in R01_S10 for which the effect is much more significant and that will be addressed later in this section):
  
    the first CCD line of an exposure read after an image with saturated overscan, is close to saturation and in most of the case there is also a small left over signal in the 2nd line read.
    
- in e2v CCD :
  
    the effect is slightly amplifier dependent, still, like in ITL, 
    the first line read in an exposure following an exposure with saturated overscan, is close to saturation, and a
    significant signal is visible in the first 20-50 lines. ( :ref:`see left plots of clear e2v image<image-e2vclear>` )


These left over electrons are not associated to what we usually
call residual image or persistence. They are suspected to be associated to pockets, induced by the
electric field configuration in the sensor and the field associated to
saturated pixels : pocket(s) that survive to a clear, will prevent charges to be cleared. 
A change of the electric field (ex: a change in clocks configuration) can remove the pockets, and free
the charges, allowing them to be cleared. If charges stuck in pocket(s) are not removed by a clear, we observed that an image read (ex: a bias) 
will fully remove them: only the first exposure taken after an image with saturated overscan is impacted: if the clocks configuration
used in our standard clear is not able to flush away those charges, a standard readout of >~ 2000 lines does remove them.   

The localisation of these uncleared electrons in the first lines of the
CCDs, spot the interface between the image area and the serial register , as the location of those pockets.
For this reason we investigated changes in the field configuration of
the serial register during the clear, to avoid the construction of
pockets at this image-serial register interface.

.. _image-e2vclear:

.. image::   /figures/plots_R12_S20_C15_E1880_bias_2024103000303.png
   :target:    ../figures/plots_R12_S20_C15_E1880_bias_2024103000303.png
   :alt: Figure showing the impact of the various type of clear on a bias taken after a saturated flat for an E2V sensor.


In the above image , we present for 3 types of sequencer ( from left to right : V29 , NoP and NopSF), a zoom on the first lines of an e2v amplifier ( here R12_S20 C10) shown as a 2D lines-columns image ( top
plots) or as the mean signal per line for the first lines read of an amplifier (bottom plots).
In an e2v CCD, a bias taken just after a saturated flat will show a residual signal in the first lines read when using the default clear (left images,clear=v29 ) : the first line has an almost saturated signal ( ~ 100 kADU here), and a
significant signal is seen up to the line ~50. In practice, in  function of the amplifier, signal can be seen up to line 20-50. When using the NoP clear (central plots), we can already see a strong reduction of the uncleared charges in the first acquired bias after a saturated flat, still a small residual signal is visible in the first ~ 20 lines. The NoPSF clear fully clear the saturated flat, and no uncleared charges are observed in the following bias.    


Conclusion
^^^^^^^^^^

 .. _table-SummaryClear:

.. table:: This table summaries the different clear methods used so
	   far . .
   
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     |                                          | Default Clear        | Multi Clear      | Multi Clear          | Deep Clear            | No Pocket(NoP)      |  No Pocket Serial Flush(NoPSF)  |
     |                                          | 1 Clear              | 3 Clears         | 5 Clears             | 1 Clear               | 1 Clear             |  1 Clear                        |
     |                                          | (seq. V29)           | (seq. V29)       | (seq. V29 )          | (Seq. V23 DC)         | (seq. V29_NoP)      |  ( seq.  V29, V30 )             |
     +==========================================+======================+==================+======================+=======================+=====================+=================================+
     | Clear duration                           | 65.5 ms              | 196.5 ms         | 327.4 ms             |   64.69 ms            |     65.8 ms         |   67 ms                         |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     | "E2V" after saturated Flat               |1st line saturated    |No residual       |No residual           |                       |signal up to line 20 | No residual                     |
     |                                          |signal up to line 50  | electrons        | electrons            |                       |                     |  electrons                      |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     | R30_S10_C10 E2V                          |                      |No residual       |No residual           |                       |                     |                                 |
     | Bright Column(~ sat. Star)               |                      | electrons        | electrons            |                       |                     |                                 |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     | "ITL" after saturated Flat               |                      |No residual       |No residual           |                       |                     |                                 |
     |                                          |                      | electrons        | electrons            |                       |                     |                                 |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     | R02_S20_C14 ITL                          |                      |No residual       |No residual           |                       |                     |                                 |
     | Bright Column (~ sat. Star)              |                      | electrons        | electrons            |                       |                     |                                 |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+
     | R01_S10  ITL "unique"                    |                      |                  |                      |                       |                     |                                 |
     |                                          |                      |                  |                      |                       |                     |                                 |
     +------------------------------------------+----------------------+------------------+----------------------+-----------------------+---------------------+---------------------------------+

     


 
