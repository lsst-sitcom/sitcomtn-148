.. image:: https://img.shields.io/badge/sitcomtn--148-lsst.io-brightgreen.svg
   :target: https://sitcomtn-148.lsst.io
.. image:: https://github.com/lsst-sitcom/sitcomtn-148/workflows/CI/badge.svg
   :target: https://github.com/lsst-sitcom/sitcomtn-148/actions/

########################################
LSST Camera Electro-Optical Test Results
########################################

SITCOMTN-148
============

'This note collects results from the LSST Camera electro-optical testing prior to installation on the TMA. We describe the CCD and Focal Plane optimization and the resulting default settings. Results from eo_pipe are shown for standard runs such as B-protocols, Dense and SuperDense PTCs, gain stability, OpSim runs of Darks, and Darks with variable delays. We also describe features such as e2v Persistence, ITL phosphorescence in coffee stains, remnant charge near Serial register following saturated images, vampire pixels, ITL dips, and others.

**Links:**

- Publication URL: https://sitcomtn-148.lsst.io
- Alternative editions: https://sitcomtn-148.lsst.io/v
- GitHub repository: https://github.com/lsst-sitcom/sitcomtn-148
- Build system: https://github.com/lsst-sitcom/sitcomtn-148/actions/


Build this technical note
=========================

Refer this: https://developer.lsst.io/project-docs/technotes.html

Build this technical note locally
=================================
```
docker run --rm -v `pwd`:/build -w /build lsstsqre/lsst-texmf:latest sh -c 'make'
```

Publishing changes to the web
=============================

This technote is published to https://sitcomtn-148.lsst.io whenever you push changes to the ``main`` branch on GitHub.
When you push changes to a another branch, a preview of the technote is published to https://sitcomtn-148.lsst.io/v.


Editing this technical note
===========================

The main content of this technote is in ``index.rst`` (a reStructuredText file).
Metadata and configuration is in the ``technote.toml`` file.
For guidance on creating content and information about specifying metadata and configuration, see the Documenteer documentation: https://documenteer.lsst.io/technotes.
