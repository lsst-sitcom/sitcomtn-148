Run 7 final operating parameters 
############################################

This section describes the conclusions of run 7 optimization and the operating conditions of the camera. Decisions regarding these parameters were decided based upon the results of the `voltage optimization <https://sitcomtn-148.lsst.io/#persistence-optimization>`__, `sequencer optimization <https://sitcomtn-148.lsst.io/#sequencer-optimization>`__, and `thermal optimization <https://sitcomtn-148.lsst.io/#thermal-optimization>`__.

Voltage conditions
^^^^^^^^^^^^^^^^^^^^

.. table:: Voltage conditions

   +-----------+--------------------+--------------------+
   | Parameter | dp80 (new voltage) | dp93 (Run 5)       |
   +===========+====================+====================+
   | pclkHigh  |    2.0             |    3.3             |
   +-----------+--------------------+--------------------+
   | pclkLow   |   -6.0             |   -6.0             |
   +-----------+--------------------+--------------------+
   | dpclk     |    8.0             |    9.3             |
   +-----------+--------------------+--------------------+
   | sclkHigh  |   3.55             |   3.9              |
   +-----------+--------------------+--------------------+
   | sclkLow   |   -5.75            |   -5.4             |
   +-----------+--------------------+--------------------+
   | rgHigh    |   5.01             |   6.1              |
   +-----------+--------------------+--------------------+
   | rgLow     |   -4.99            |   -4.0             |
   +-----------+--------------------+--------------------+
   | rd        |   10.5             |   11.6             |
   +-----------+--------------------+--------------------+
   | od        |   22.3             |   23.4             |
   +-----------+--------------------+--------------------+
   | og        |   -3.75            |   -3.4             |
   +-----------+--------------------+--------------------+
   | gd        |   26.0             |   26.0             |
   +-----------+--------------------+--------------------+

Sequencer conditions
^^^^^^^^^^^^^^^^^^^^

.. table:: Sequencer conditions

   +---------------+------------------------+
   | Detector type |       File name        |
   +===============+========================+
   |      E2V      | FP_E2V_2s_l3cp_v30.seq |
   +---------------+------------------------+
   |      ITL      | FP_ITL_2s_l3cp_v30.seq |
   +---------------+------------------------+

- v30 sequencers are identical to the FP_ITL_2s_l3cp_v29_Noppp.seq and FP_E2V_2s_l3cp_v29_NopSf.seq. All sequencer files can be found in the `github repository <https://github.com/lsst-camera-dh/sequencer-files/tree/master/run7>`__.

Other camera conditions
^^^^^^^^^^^^^^^^^^^^^^^
- Idle flush disabled
