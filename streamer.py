"""
This script processes a video with object detection.

Usage:
    python your_script.py [--video_path VIDEO_PATH] [--detector_name DETECTOR_NAME] [--save_in_db]

Options:
    --video_path VIDEO_PATH       Path to the input video file. Default is "highway.mp4".
    --detector_name DETECTOR_NAME Name of the object detector to use. Default is "yolov5s".
    --save_in_db                  Whether to save detections in a database.
                                  If provided, detections will be saved.
"""

import argparse
from apputils import show_video

def main():
    """
    Main function to process a video with object detection.

    This function parses command-line arguments to specify the input video file,
    the object detector to use,
    and whether to save detections in a database. It then calls the `show_video()`
    function from apputils
    module to process the video with the specified parameters.

    Command-line Arguments:
        --video_path (str): Path to the input video file. Default is "highway.mp4".
        --detector_name (str): Name of the object detector to use. Default is "yolov5s".
        --save_in_db (bool): Whether to save detections in a database. If provided,
          detections will be saved.

    Returns:
        None
    """
    parser = argparse.ArgumentParser(description="Process video with object detection.")
    parser.add_argument("--video_path", type=str, default="highway.mp4", help="Path to the input video file.")
    parser.add_argument("--detector_name", type=str, default="yolov5s", help="Name of the object detector to use.")
    parser.add_argument("--save_in_db", action="store_true", help="Whether to save detections in a database.")
    parser.add_argument("--db_name", type=str, default=None, help="Name of the database to save detections.")
    parser.add_argument("--param", action="store_true", help="Some additional parameter.")
    parser.add_argument("--replace_detections", action="store_true", help="Replace detections if they already exist in the database.")
    parser.add_argument("--show_fps", action="store_true", help="Whether to show FPS information on the video.")
    parser.add_argument("--len_img_bucket", type=int, default=10, help="Length of image bucket.")

    args = parser.parse_args()

    show_video(video_path=args.video_path, detector_name=args.detector_name,\
                save_in_db=args.save_in_db, replace_detections = True,\
                show_fps = True, len_img_bucket=10)

if __name__ == "__main__":
    main()
