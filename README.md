# 0. About

This is just a repository with some auxiliar functions. Main script iterates over a list of subjects plotting MRIs in the desired plane and coordinates. I created this in order to do some quality controls in my work, but I'm planning to keep improving it...

# 1. Installation and Dependencies

Python 3.8. 

## 1.1. Dependencies

- matplotlib==3.4.3
- nibabel==3.2.1
- nilearn==0.8.1
- numpy==1.21.3
- pandas==1.3.4
- scikit-learn==1.0.1
- scipy==1.7.1

## 1.2. Installation

Just pull the git repository and uncompress in your python-lybrary fold. If you don't know where it is, check with: 

```Python
import sys
for path in sys.path: print(path)
```

# 2. How to use

```Python
import MReye as mreye
```
All functions include documentation, check with help(). 

# 3. Running the main script

The main script takes the following positional arguments: 

- 1: Starting directory.
- 2: Text file with subjects to be plotted. 
- 3: The program expects that each subject has a sub-directory. It also expects that the subdirectory is the same name of the subject directory plus a sufix. If there is no sufix leave it blank (''). 
- 4: Sequence to be plotted. 
- 5: Plane--> x, y, z. 
- 6: Coords --> List with coordinates to be passed to nilearn. 
- 7: Output directory. 

So, the program expects the following directory structur: 
start_dir
|__subj1
   |__subj1_sufix
      |__flair_ax
         |__flair_ax.nii.gz

Example:

```bash
python -m MReye /media/start_directory ~/subjects_list.txt sufix t1_ax z [-30,-20,-10,0,10,20,30] ~/out_directory
```
Where subjects list is just a text file with the name of each subject...

# 4. License

This project is distributed under MIT license. Please, refer to license.txt for further information.

        
     

