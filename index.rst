########################################
LSST Camera Electro-Optical Test Results
########################################

.. abstract::

   'This note collects results from the LSST Camera electro-optical testing prior to installation on the TMA. We describe the CCD and Focal Plane optimization and the resulting default settings. Results from eo_pipe are shown for standard runs such as B-protocols, Dense and SuperDense PTCs, gain stability, OpSim runs of Darks, and Darks with variable delays. We also describe features such as e2v Persistence, ITL phosphorescence in coffee stains, remnant charge near Serial register following saturated images, vampire pixels, ITL dips, and others.

--------------------------------
Electro-optical setup
--------------------------------
.. include::   sections/run7Changes.rst
.. include::   sections/projectorSpots.rst
.. include::   sections/darkCurrent.rst
--------------------------------
Camera Optimization
--------------------------------
.. include::   sections/persistenceOptimization.rst
.. include::   sections/sequencerOptimization.rst
.. include::   sections/thermalOptimization.rst
--------------------------------
Characterization
--------------------------------
.. include::   sections/baselineCharacterization.rst
.. include::   sections/guiderOperation.rst
--------------------------------
Camera stability
--------------------------------
.. include::   sections/defectStability.rst
.. include::   sections/biasStability.rst
.. include::   sections/gainStability.rst
--------------------------------
Sensor features
--------------------------------
.. include::   sections/treeRings.rst
.. include::   sections/ITLDips.rst
.. include::   sections/vampirePixels.rst
.. include::   sections/serialRemnants.rst
.. include::   sections/phosphorescence.rst
--------------------------------
Conclusions
--------------------------------
.. include::   sections/run7OperatingParameters.rst
.. include::   sections/recordRuns.rst

