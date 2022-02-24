# Apriltags testbench

Provides information on the accuracy of estimations made by apriltag_ros library

## How to use

- ### Static tests

1. Create rosbags

    1. Record a video: Make sure to wait long enough on target translation/rotations, so that the graphs have plateaus. The rest of the data points will be discarded

    2. Edit [this file](test_pipeline/launch/video_file.launch) for entering recorded video file parameters;

        Param | Detail | Default/Example
        --- | --- | --- 
        `camera_info_url` | Camera calibration file | file:///home/uware/general_webcam_calibration_files/ost.yaml
        `video_stream_provider` | Video file location | /home/user/test_vids/some_file.mkv
        `width/height` | Resolution | 800 480
        `fps` | Fps | 30

        > Make sure Camera calibration file has matching `camera_name` and `resolution`
    
    3. Run `roslaunch test_pipeline video_detection.launch`. Transformation messages published by the topic `/tf` will be recorded in rosbag under `/home/uware/rosbags/` by default. This can be changed by editing [this file](test_pipeline/launch/video_detection.launch)

    4. `Ctrl-C` to stop the process.
