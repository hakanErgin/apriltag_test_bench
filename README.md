# Apriltags testbench

Provides information on the accuracy of estimations made by [Apriltag_ros](https://github.com/AprilRobotics/apriltag_ros) library.
> This repository is the content of `src` folder of a _catkin workspace_ with multiple packages. The virtual environment and the custom files are created in custom package `test_pipeline`.

## How to use

> Don't forget to set up apriltag_ros [config](apriltag_ros/apriltag_ros/config) files according to the your tags.

- ### Static tests

1. Create rosbags

    1. Recording a video: 
        - Videos for static tests can have multiple translations or rotations. For example: the same video can have the tag displayed to the camera at 1m,2m,3m or 30°,45°,90°
        - Make sure to wait long enough on target translation/rotations, so that the graphs have plateaus on targets when plotted against time. The rest of the data points will be discarded

    2. Edit [this file](test_pipeline/launch/video_file.launch) with the recorded video file parameters and camera calibration file;

        Param | Explanation | Default/Example
        --- | --- | --- 
        `camera_info_url` | Camera calibration file | file:///home/uware/calibration_files/ost.yaml
        `video_stream_provider` | Video file location | /home/user/test_vids/some_file.mkv
        `width/height` | Resolution | 800/480
        `fps` | Fps | 30

        > Make sure the Camera calibration file has matching `camera_name` (or just change to 'camera') and `resolution`
    
    3. Run `roslaunch test_pipeline video_detection.launch`. Transformation messages published by the topic `/tf` will be recorded in rosbag under `/home/uware/rosbags/` by default. This can be changed by editing [the launch file](test_pipeline/launch/video_detection.launch)

        > If you see an error/warniung about the camera topics `/camera_info` and `/camera_rect` not being published, it means the nodes didn't start in proper order, just rerun the command above.

    4. `Ctrl-C` to stop the process when receiving message `Reached the end of frames`.

2. Visualise results
    
    1. From `rotations` or `translations` folder in [test_pipeline/scripts](test_pipeline/scripts) use the notebook that suites your needs.

    2. Edit the second cell of the notebook for following inputs:
        
        Input | Type | Notes
        --- | --- | --- 
        bag | string | relative/absolute path or rosbag
        target | string | target variable - will be used when plotting
        input_vals |  list (int) | this is where you specify 1m,2m,3m or 30°,45°,90° (described in `Recording a video` above.)

    3. Run the notebook
---

- ### Dynamic tests - wip
