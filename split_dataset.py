import os
import shutil
import random

source_images = "White_Cane_Dataset/images"
source_labels = "White_Cane_Dataset/labels"
output_dataset = "White_Cane_YOLO_Ready" # The new, clean folder we will create

train_ratio = 0.8

print("Setting up YOLO folder structure...")

folders_to_create = [
    f"{output_dataset}/images/train",
    f"{output_dataset}/images/val",
    f"{output_dataset}/labels/train",
    f"{output_dataset}/labels/val"
]
for folder in folders_to_create:
    os.makedirs(folder, exist_ok=True)

all_images = [f for f in os.listdir(source_images) if f.endswith(('.jpg', '.png', '.jpeg'))]
random.seed(42) # Keeps the randomness consistent if you run it twice
random.shuffle(all_images)

split_index = int(len(all_images) * train_ratio)
train_images = all_images[:split_index]
val_images = all_images[split_index:]

def copy_data(image_list, split_name):
    print(f"Copying {len(image_list)} files into {split_name}...")
    for img_name in image_list:
        # Copy the image
        src_img_path = os.path.join(source_images, img_name)
        dst_img_path = os.path.join(output_dataset, "images", split_name, img_name)
        shutil.copy(src_img_path, dst_img_path)
        
        # Find and copy the matching label (.txt)
        label_name = os.path.splitext(img_name)[0] + ".txt"
        src_label_path = os.path.join(source_labels, label_name)
        dst_label_path = os.path.join(output_dataset, "labels", split_name, label_name)
        
        # Check if the label exists (sometimes images don't have objects in them)
        if os.path.exists(src_label_path):
            shutil.copy(src_label_path, dst_label_path)

copy_data(train_images, 'train')
copy_data(val_images, 'val')

yaml_content = f"""path: {os.path.abspath(output_dataset).replace('\\', '/')}
train: images/train
val: images/val
nc: 1
names:
  0: White_Cane
"""

yaml_path = os.path.join(output_dataset, "dataset.yaml")
with open(yaml_path, "w") as yaml_file:
    yaml_file.write(yaml_content)

print(f"\nYOLO dataset is ready at: {output_dataset}")
print(f"Train images: {len(train_images)}")
print(f"Val images: {len(val_images)}")