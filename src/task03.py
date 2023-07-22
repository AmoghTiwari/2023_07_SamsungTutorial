import cv2
import os

def create_video_from_frames(frames_folder, output_video_path, fps=30):
    # Get a list of all image files in the frames folder
    image_files = [f for f in os.listdir(frames_folder) if f.endswith(".png") or f.endswith(".jpg")]

    if not image_files:
        print("No image files found in the frames folder.")
        return

    image_files.sort()
    image_files2 = image_files[:15]
    for image_file in image_files[-15:]:
        image_files2.append(image_file)
    image_files = image_files2

    # Sort the image files to ensure they are in the correct order
    # Note that this is an important step (as os.listdir doesn't load in order)

    # Get the first image to determine the size of the video frames
    first_image_path = os.path.join(frames_folder, image_files[0])
    frame = cv2.imread(first_image_path)
    height, width, _ = frame.shape

    # Define the codec and create a VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use 'XVID' for AVI format
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

    # Loop through the image files and write each frame to the video
    for image_file in image_files:
        image_path = os.path.join(frames_folder, image_file)
        frame = cv2.imread(image_path)

        if frame is not None:
            out.write(frame)

    # Release the VideoWriter and close the file
    out.release()
    print(f"Video created: {output_video_path}")

# Example usage:
frames_folder = "../data/vid_frames"
output_video_path = "../data/magic.mp4"
fps = 15  # Frames per second
create_video_from_frames(frames_folder, output_video_path, fps)