# Apriltags testbench

## Results

All tests results can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/analysis.ipynb)
Rotational tests can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/cumulative_rotations.ipynb)
Distance test results can be found [here](https://github.com/hakanErgin/apriltag_test_bench/blob/main/analysis/cumulative_translations.ipynb)


Provides information on the accuracy of estimations made by [Apriltag_ros](https://github.com/AprilRobotics/apriltag_ros) library.
> This repository is the content of `src` folder of a _catkin workspace_ with multiple packages. The virtual environment and the custom files are created in custom package `test_pipeline`.

## How to use

> Don't forget to set up apriltag_ros [config](apriltag_ros/apriltag_ros/config) files according to the your tags.

1. Create rosbags
    1. Recording a video: 
        - ### Static tests
            Static tests check if the tag is detected at target positions/rotations. They provide estimated measurements to compare with real measurements. And plot info on errors.
            - Videos for static tests can have multiple translations OR rotations. For example: the same video can have the tag displayed to the camera at 1m,2m,3m or 30°,45°,90°
            - Make sure to wait long enough on target translation/rotations, so that the graphs have plateaus on targets when plotted against time. The rest of the data points will be discarded
        - ### Dynamic tests
            Dynamic tests check if the tag is detected at known speeds in single axis. They provide percentages of detected and not detected data points in relation to time. And plot other informative graphs.
            - Videos for dynamic tests should be edited to the portion in a way that the tag is expected to be detected at measured speed.

    2. Edit [this file](test_pipeline/launch/video_file.launch) with the recorded video file parameters and camera calibration file;

        Param | Explanation | Default/Example
        --- | --- | --- 
        `camera_info_url` | Camera calibration file | file:///home/uware/calibration_files/ost.yaml
        `video_stream_provider` | Video file location | /home/user/test_vids/some_file.mkv
        `width/height` | Resolution | 800/480
        `fps` | Fps | 30

        > Make sure the Camera calibration file has matching `camera_name` (or just change to 'camera') and `resolution`
    
    3. Run `roslaunch test_pipeline video_detection.launch`. Transformation messages published by the topic `/tf` and `/tag_detections` will be recorded in rosbag under `/home/uware/rosbags/` by default with optional `bag_name` param for giving a name to rosbag recorded. Path can be changed in [launch file](test_pipeline/launch/video_detection.launch)

        > If you see an error/warniung about the camera topics `/camera_info` and `/camera_rect` not being published, the nodes didn't start in proper order, just rerun the command above.

    4. `Ctrl-C` to stop the process when receiving message `Reached the end of frames`.

2. Visualise results
    
    1. From `rotations` or `translations` folder in [test_pipeline/scripts](test_pipeline/scripts) use the notebook that suites your needs.

    2. Edit the second cell of the notebook for following inputs:
        
        Input | Type | Notes
        --- | --- | --- 
        bag | string | relative/absolute path or rosbag
        target | string | target variable - will be used when plotting
        input_vals (_only static tests_) |  list (int) | this is where you specify 1m,2m,3m or 30°,45°,90° (described in `Recording a video` above.)

    3. Run the notebook
---

