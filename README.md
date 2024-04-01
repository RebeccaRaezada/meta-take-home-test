
### This repository has the solutions to the problems provided as part of Meta take home test:

## Bash

#### In Bash, how do I list all text files in the current directory (excluding subdirectories) that have been modified in the last month
SOLUTION: in Bash folder, in bash solution file

## Python

#### 1) Compute the length of the longest strictly increasing subsequence in a list.
    ○ Input: nums = [11, 5, 2, 5, 3, 7, 101, 18]
    ○ Output: 4
    ○ Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
SOLUTION: Function is in longestSequence.py, which can be run using main.py

#### 2) Write a script to produce a list of every file under
    https://gentoo.osuosl.org/distfiles/
SOLUTION: For this required functions are in listAllFiles.py, which can be run using main.py too.
The output file is also attached as all_files_listed

## SQL
      We have: <br>
      ● a machine learning binary classifier which takes as input an image and outputs the image quality score (from 0 to 1, where scores closer to 0 represent low-quality images, and scores closer to 1 represent high-quality images). <br>
      ● a SQL table containing 1M unlabeled images. We run each of these images through our machine learning model to get float scores from 0 to 1 for each image.
      We want to prepare a new training set with some of these unlabeled images. An example of unlabeled_image_predictions (1M rows) is shown below: <br>
      image_id score<br>
      242 0.23<br>
      123 0.92<br>
      248 0.88<br>
      … …<br>
      Our sampling strategy is to order the images in decreasing order of scores and sample every 3rd image starting with the first from the beginning until we get 10k positive samples. And we would like to do the same in the other direction, starting from the end to get 10k negative samples. <br>
      Task: Write a SQL query that performs this sampling and creates the expected output ordered by image_id with integer columns image_id, weak_label.
SOLUTION: in SQL folder, in sql solution file
