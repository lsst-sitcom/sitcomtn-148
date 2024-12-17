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
    significant signal is visible in the following 20-50 lines. ( :ref:`see left plots of clear e2v image<fig-image-e2vclear>` )


These left over electrons are not associated to what we usually
call residual image or persistence. They are suspected to be associated to pockets, induced by the
electric field configuration in the sensor and the field associated to
saturated pixels : pocket(s) that survive to a clear, will prevent charges to be cleared. 
A change of the electric field (ex: a change in clocks configuration) can remove the pockets, and free
the charges, allowing them to be cleared. If charges stuck in pocket(s) are not removed by a clear, we observed that an image read (ex: a bias) 
will fully remove them: only the first exposure taken after an image with saturated overscan is impacted. If the clocks configuration
used in our standard clear is not able to flush away those charges, a standard readout of >~ 2000 lines does remove them.   


The localisation of these uncleared electrons in the first lines of the
CCDs, spots the interface between the image area and the serial register as the location for those pockets.
For this reason we investigated changes in the field configuration of
the serial register during the clear, to avoid 
pockets at this image-serial register interface.


New sequencers
^^^^^^^^^^^^^^

To addresse this clear issue, we focussed on updating the serial register field as the lines are moved to it. The constrain being that the changes introduced should not significantly increase the clear execution time.
It should be notice that we tried in 2021 a sequencer called "Deep Clear" ( [sequencerV23_DC]_ ) as a first try to address the clear issue: it added one full line flush on top of the existing one at the end of the clear. This sequencer did improve the clear , still not fully fixing the clear issue ( see :ref:`Summary table<table-SummaryClear>`). 

In the run7, We considered on top of the default clear, 2 new configurations. The changes are in the ParallelFlush function , which move the charges from the image area to the serial register :

- the default clear (V29) : In the default clear, all serial clocks are kept up as the // clocks move charges from the image area to the serial register ( [sequencerV29]_ ). The charges once on the serial register will hopefully flow to the ground : the serial register clocks being all up , without pixels boundary , and with its amplifier in clear state. At the end of the clear, a full flush of the serial register is done ( ~ the serial clocks changes to read a single line ).       

- the No-pocket Clear (NoP) : a clear where the serial register has the same configuration   ( S1 & S2 up , S3 low ) when the // clock P1 moves the charges to the serial register than in a standard image read . Still we keept all phases up the rest of the time for a fast clear of the charges along the serial register ( [sequencerV29_NoP]_ ) . The idea is that the S3 phase is not designed to be up when charges are transfered to the serail register, and is probably playing a major role in the pockets creation.

- The No-pocket with serial flush Clear (NoPSF) : this sequencer is close to the NoP solution , except that during the transfered of 1 line to the serial register, the serial phases are also moved to transfer two pixels along teh serial register. The changes in electric field at the image-serial register interface are then even more representative to what a standard read will produce, and should further prevent the creation of pockets.  ( [sequencerV29_NoPSF]_ ).



.. [sequencerV23_DC]  https://github.com/lsst-camera-dh/sequencer-files/blob/master/run5/FP_E2V_2s_ir2_v23_DC.seq
.. [sequencerV29]     https://github.com/lsst-camera-dh/sequencer-files/blob/master/run7/FP_E2V_2s_l3cp_v29.seq 
.. [sequencerV29_NoP] https://github.com/lsst-camera-dh/sequencer-files/blob/master/run7/FP_E2V_2s_l3cp_v29_Nop.seq
.. [sequencerV29_NoPSF]  https://github.com/lsst-camera-dh/sequencer-files/blob/master/run7/FP_E2V_2s_l3cp_v29_NopSf.seq 

Results on standard e2v and itl CCD
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


.. image::   sections/figures/plots_R12_S20_C15_E1880_bias_2024103000303.png
   :name: fig-image-e2vclear
   :alt:  Figure showing the impact of the various types of clear on a bias taken after a saturated flat for an E2V sensor.
      

*Figure showing the impact of the various types of clear on a bias taken after a saturated flat for an E2V sensor.*
	  

.. image::   sections/figures/plots_R03_S11_C14_E1812_bias_2024102800352.png
   :name: fig-image-itlclear
   :alt: Figure showing the impact of the various types of clear on a bias taken after a saturated flat for an ITL sensor.
      

*Figure showing the impact of the various types of clear on a bias taken after a saturated flat for an ITL sensor.*



In the above images , we present for 3 types of sequencer ( from left to right : V29 , NoP and NopSF), a zoom on the first lines of an itl or e2v amplifier ( for itl R03_S11 C14 and  for e2v  R12_S20 C10 ) shown as a 2D lines-columns image ( top
plots) or as the mean signal per line for the first lines read of an amplifier (bottom plots).

As seen in :ref:`see left plots of clear e2v image<fig-image-e2vclear>` for an e2v CCD, a bias taken just after a saturated flat will show a residual signal in the first lines read when using the default clear (left images,clear=v29 ) : the first line has an almost saturated signal ( ~ 100 kADU here), and a
significant signal is seen up to the line ~50. In practice, in  function of the amplifier, signal can be seen up to line 20-50. When using the NoP clear (central plots), we can already see a strong reduction of the uncleared charges in the first acquired bias after a saturated flat, still a small residual signal is visible in the first ~ 20 lines. The NoPSF clear (right plots) fully clear the saturated flat, and no uncleared charges are observed in the following bias.    



As seen in :ref:`see left plots of clear itl image<fig-image-itlclear>` for an itl CCD, a bias taken just after a saturated flat will show a residual signal in the first lines read when using the default clear (left images,clear=v29 ) : the first line has an almost saturated signal ( ~ 100 kADU here), and a
significant signal is seen in the following line. Both NoP clear (central plots) and NoPSF clear (right plots)  fully clear the saturated flat, and no uncleared charges are observed in the following bias.    


Results on itl R01_S10 
^^^^^^^^^^^^^^^^^^^^^^^

.. image::   sections/figures/Clear_R01_S10.png
   :name: fig-image-itlR01_S10clear
   :alt: Figure showing the impact of the various types of clear on ITL R01_S10.




*Figure showing the impact of the various types of clear on ITL R01_S10 after a saturated flat ( bias after a saturated flat), from left to right : 1 standard Clear , 3 standard Clear , 5 standard Clear , 1 NoP Clear, 1 NoPSF Clear*


There is one ITL sensor, R01_S10, that presents a specific and non-understood behavior :

- It has a quite low full well (2/3 of nominal )

- The 3 CCD of this REB have a gain 20% lower than all other ITL CCD ?

- The images taken after a large staturation, as seen in figure :ref:`clear in itl R01_S10 <fig-image-itlR01_S10clear>`, show a large amount of uncleared charged ( with the standard clear : 4 amplifiers with ~500 lines of saturated signal !)

It apears that putting S3 low during the clear as done in NoP or NoPSF , is even worse than a standard clear. This is strange as a full frame read , which does this too, manages to clear such image.
We can notice that NoPSF is ~ 50% better than NoP , but still worse than the standard clear , in particular for the 12 amplifiers almost correct with the standard clear.

At this stage we don't have a correct way to clear this sensor once it collects a saturated flat, but It's not known if a saturated star in this sensor, leaving signal in the parallele overscan, will presents the same clear issue.





Conclusion
^^^^^^^^^^

 .. _table-SummaryClear:

.. table:: *This table summaries the different clear methods used so far.*
	   
     +------------------------------------------+----------------------+---------------------+----------------------+-----------------------+-----------------------+---------------------------------+
     |                                          | Default Clear        | Multi Clear         | Multi Clear          | Deep Clear            | No Pocket(NoP)        |  No Pocket Serial Flush(NoPSF)  |
     |                                          | 1 Clear              | 3 Clears            | 5 Clears             | 1 Clear               | 1 Clear               |  1 Clear                        |
     |                                          | (seq. V29)           | (seq. V29)          | (seq. V29 )          | (Seq. V23 DC)         | (seq. V29_NoP)        |  ( seq.  V29_NoPSF, V30 )       |
     +==========================================+======================+=====================+======================+=======================+=======================+=================================+
     | Clear duration                           | 65.5 ms              | 196.5 ms            | 327.4 ms             |   64.69 ms            |     65.8 ms           |   67 ms                         |
     +------------------------------------------+----------------------+---------------------+----------------------+-----------------------+-----------------------+---------------------------------+
     | "E2V" after saturated Flat               |1st line saturated    |No residual          |No residual           |1st line saturated     |signal up to line 20   | No residual                     |
     |                                          |signal up to line 50  | electrons           | electrons            |signal up to line <20  |                       |  electrons                      |
     +------------------------------------------+----------------------+---------------------+----------------------+-----------------------+-----------------------+---------------------------------+
     | "ITL" after saturated Flat               |1st line saturated    |No residual          |No residual           |tiny signal left in    |  No residual          | No residual                     |
     |                                          |signal up to 2nd line | electrons           | electrons            |the first line         |   electrons           |  electrons                      |
     +------------------------------------------+----------------------+---------------------+----------------------+-----------------------+-----------------------+---------------------------------+
     | R01_S10  ITL "unique"                    |first 500 lines       |first 150 lines      |first 100 lines       | not measured          |first 1000  lines      | first 750  lines                |
     |                                          |saturated for 4 amp.  |saturated for        |saturated for         |                       |saturated for 16 amp.  | saturated for 16 amp.           |
     |                                          |13 amp. with signals. |2 amp.               |2 amp.                |                       |16 amp. with signals.  | 16 amp. with signals.           |
     |                                          |                      |5 amp. with signals. |2 amp. impacted       |                       |                       |                                 |
     +------------------------------------------+----------------------+---------------------+----------------------+-----------------------+-----------------------+---------------------------------+



Even if NoP or NoPSF are overcoming the clear issue we had with ITL sensors, the exception of R01_S10 prevented the usage of those sequencers for ITL device for the run7. Notice that beyond R01_S10  the numbers of line potencilly  "not cleared" are small (2 first lines)in ITL device, and they correspond to a CCD area hard to use anyway ( sensor edges with low efficciency). So at this stage the default clear is still our default for ITL, and further studies to overcome the problem with R01_S10 are forseen ( ex : do a continuous serial flush during exposure  at low rate , 10^6 pixels flush in 15s).  

 On the other side , after those studies in run7, we now have a good way to fully clear the e2v devices through the NopSF clear. The NoPSF clear grants that the first 50 lines of e2v device that had un-cleared electrons from the previous exposure, are now free of such contamination.



From now   :

- for e2v, NoPSF will be the default clear method

- for ITL, the origial clear (serial phase 3 always ), slightly extended in time to match the NoPSF e2v clear execution time , will stay the default method.  



