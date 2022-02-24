# Apriltags testbench

Provides information on the accuracy of estimations made by apriltag_ros library.
> This repository is the content of `src` folder of a _catkin workspace_ with multiple packages. The virtual environment and the custom files are created in custom package `test_pipeline`.

## How to use

- ### Static tests

1. Create rosbags

    1. Record a video: Make sure to wait long enough on target translation/rotations, so that the graphs have plateaus. The rest of the data points will be discarded

    2. Edit [this file](test_pipeline/launch/video_file.launch) with the recorded video file parameters and camera calibration file;

        Param | Explanation | Default/Example
        --- | --- | --- 
        `camera_info_url` | Camera calibration file | file:///home/uware/calibration_files/ost.yaml
        `video_stream_provider` | Video file location | /home/user/test_vids/some_file.mkv
        `width/height` | Resolution | 800/480
        `fps` | Fps | 30

        > make sure the Camera calibration file has matching `camera_name` (change to 'camera') and `resolution`
    
    3. Run `roslaunch test_pipeline video_detection.launch`. Transformation messages published by the topic `/tf` will be recorded in rosbag under `/home/uware/rosbags/` by default. This can be changed by editing [the launch file](test_pipeline/launch/video_detection.launch)

    4. `Ctrl-C` to stop the process when receiving message `Reached the end of frames`.

2. Visualise results
    
    1. From `rotations` or `translations` folder from [test_pipeline/scripts](test_pipeline/scripts) use the notebook that suites your needs.

    2. Edit the second cell of the notebook for following inputs:
        
        - Location of rosbag file

        - Target variable

        - Inputs that are recorded in the video file (in meters or degrees)

    3. Run the notebook
---

- ### Dynamic tests - wip
