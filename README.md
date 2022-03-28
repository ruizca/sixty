# sixty
A simple python wrapper for [SIXTE](https://www.sternwarte.uni-erlangen.de/research/sixte/index.php), a software package for X-ray telescope observation simulations.

This module assumes that a working installation of SIXTE and SIMPUT is available in your system. See the installation instructions in the [SIXTE website](https://www.sternwarte.uni-erlangen.de/research/sixte/simulation.php). I have only trested this on linux, I don't know if it would work on macOS.


Example
-------
```
import sixty

sixty.run("sixteversion")
```

Any command available for SIXTE/SIMPUT can be called by the `run` method. For example, to run the first example presented in the SIXTE website, you can do (assuming you already have the required files):
```
sixty.run(
  "simputfile",
  RA=40.2,
  Dec=12.8,
  XSPECFile="example_spectrum.xcm",
  LCFile=example_lightcurve.dat,
  MJDREF=50800.0,
  Emin=0.5,
  Emax=10.0,
  srcFlux=2.3e-12,
  Simput="example_source.simput",
)
```
