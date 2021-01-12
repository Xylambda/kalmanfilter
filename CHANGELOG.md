# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/).

## [1.0.1] - 2021-01-10

### Added

- Added `state_size` attribute.

### Changed

- Updated `predict` method. Now it does not return anything.
- Updated `test_kalman.py` to a more friendly syntax.
- Updated problematic dependencies.

### Fixed

- Fixed minor typos in README.


## [1.0.0] - 2021-01-09

### Added

- Added multidimensional computations.
- Added log and badges from [shield.io](https://shields.io/)
- Added `control-input` matrix and vector to computations.

### Changed

- Updated README.
- Updated module design that allows for future features.
- Updated tests for kalman filter.
- Updated kalman_filter. Now it is a class and supports multivariate computations.

### Fixed

- Fixed minor typos in README.
- Fixed `update` formula in README.