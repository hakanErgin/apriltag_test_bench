# Apriltags testbench

## About

Provides information on the accuracy of estimations made by [Apriltag_ros](https://github.com/AprilRobotics/apriltag_ros) library.
> This repository is the content of `src` folder of a _catkin workspace_ with multiple packages. The virtual environment and the custom files are created in custom package `test_pipeline`.

### Tests performed
1. Static

    - Z - Distance - 2,4,6,8,10m
    - Yaw angle - 0,15,30,45,60,75° (at 2m and 5m)

2. Dynamic
    - Linear velocity - 0.5m/s 
    (@ 2.5m and 4.5m distance)
    - Rotational velocity - 90°/s roll & yaw 
    (@ 1m and 3m distance)

### Tags
- Tag families:
    - 16h5 / 21h7 / 25h9 / 36h11

- Tags sizes: 
    - Large tags ~15-20cm 
    - Small tags ~5-7cm

- Resolutions:
    - 1080/720/360p (High/Med/Low)

---
## Results

- Slides

Extensive results can be found [here](https://docs.google.com/presentation/d/1EUutPdiExMkT9pG82kUPofYTUeRxX2j08Qsl4d8sF74/edit?usp=sharing)

-  Notebooks

All tests results can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/analysis.ipynb)

Rotational tests can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/cumulative_rotations.ipynb)

Distance test results can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/cumulative_translations.ipynb)

---
### How to create own tests

See [here](how_to_create_tests.md)