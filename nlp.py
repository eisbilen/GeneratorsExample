
import tensorflow as tf

import tensorflow_datasets as tfds
import os



import glob

print("erdem")

parent_dir = /Users/erdemisbilen/Angular/TRTWorld/articlesTXT/"

FILE_NAMES = [f for f in listdir(parent_dir) if isfile(join(parent_dir, f))]
FILE_NAMES = glob.glob(parent_dir + "*.txt")
print(glob.glob(parent_dir + "*.txt"))

print(FILE_NAMES)

def labeler(example, index):
  return example, tf.cast(index, tf.int64)  

labeled_data_sets = []

for i, file_name in enumerate(FILE_NAMES):
  lines_dataset = tf.data.TextLineDataset(os.path.join(parent_dir, file_name))
  labeled_dataset = lines_dataset.map(lambda ex: labeler(ex, i))
  labeled_data_sets.append(labeled_dataset)

print(labeled_data_sets)
print("erdem")