import os
import imageio

def create_video_from_images(input_folder, output_video_path, fps=30):
    # Get the list of PNG files in the input folder
    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.jpg')]

    # Sort the files to maintain order
    image_files.sort()

    if not image_files:
        print("No PNG images found in the specified folder.")
        return

    # Create a list to store image paths
    image_paths = [os.path.join(input_folder, img) for img in image_files]

    # Read images and create video
    with imageio.get_writer(output_video_path, fps=fps) as writer:
        for image_path in image_paths:
            image = imageio.imread(image_path)
            writer.append_data(image)

    print(f"Video created successfully at: {output_video_path}")

# Example usage:
input_folder_path = "C:\\Project\\sampleCode\\hdSigns"
output_video_path = "C:\\Project\\sampleCode\\hdSigns\\video.mp4"
create_video_from_images(input_folder_path, output_video_path)
