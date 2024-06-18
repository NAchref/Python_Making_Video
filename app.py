import os
import imageio
from PIL import Image, ImageDraw, ImageFont

# Function to aggregate specific paragraphs related to Azure
def aggregate_specific_info():
    azure_info = [
        "Microsoft Azure is a cloud computing platform and service created by Microsoft for building, testing, deploying, and managing applications and services through Microsoft-managed data centers.",
        "Azure offers a wide range of services and solutions including computing, analytics, storage, and networking.",
        "With Azure, organizations can achieve cost savings, scalability, and flexibility by leveraging its pay-as-you-go pricing model and global infrastructure.",
        "Azure provides comprehensive security, compliance, and privacy features to protect data and applications.",
        "Developers can use Azure to build, deploy, and manage applications using their preferred tools and frameworks."
    ]
    
    return azure_info

# Function to create video using images and Azure information
def create_video(images_folder='images', output_file='azure_video.mp4'):
    azure_info = aggregate_specific_info()
    
    # Gather images from folder
    image_files = sorted([os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith('.jpg') or f.endswith('.png')])
    num_images = len(image_files)
    
    # Ensure there are enough images for the paragraphs
    if num_images < len(azure_info):
        raise ValueError("Not enough images in the folder to match Azure information paragraphs.")
    
    # Create frames with image and Azure information
    frames = []
    font = ImageFont.truetype("arial.ttf", 16)
    for i in range(len(azure_info)):
        image_path = image_files[i]
        azure_text = azure_info[i]
        
        # Open image and resize if necessary
        image = Image.open(image_path)
        if image.size[0] > 800 or image.size[1] > 600:
            image = image.resize((800, 600))
        
        # Add Azure information text overlay
        draw = ImageDraw.Draw(image)
        text_width, text_height = draw.textsize(azure_text, font=font)
        text_x = (image.width - text_width) // 2
        text_y = image.height - text_height - 20
        draw.text((text_x, text_y), azure_text, font=font, fill=(255, 255, 255))
        
        # Convert image to RGB mode (required for imageio)
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        # Append frame to frames list
        frames.append(np.array(image))
    
    # Save frames as a video using imageio
    imageio.mimsave(output_file, frames, fps=1)

if __name__ == "__main__":
    create_video()
    print(f"Video created successfully as 'azure_video.mp4'")
