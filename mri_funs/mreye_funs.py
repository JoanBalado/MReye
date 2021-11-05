import numpy
import numpy as np
import nibabel as nib
import nilearn.plotting as niplot


def load_nifti(path):
    """
    Load a nifti image and returns both nifti and data objects
    Args:
        path(str): Path to nifti.
    Return:
         Nifti and data objects
    """
    if type(path) is not str:
        raise TypeError('Path must be a string')

    img_nifti = nib.load(path)
    img_data = img_nifti.get_fdata()
    return img_nifti, img_data

def adjust_contrast(img: np.ndarray, prob_sup=0.999, prob_inf=0):
    """
    Adjust contrast image based on quantiles.
    Args:
        img(numpy.ndarray): Numpy array conaining MRI info.
        prob_sup(numeric): Superior quantile to be used. Intensities above this threshold will be replaced for the superior quantile value.
        prob_inf(numeric): Inferior quantile to be used. Intensities below this threshold will be replaced for the inferior quantile value.
    Return:
         Returns np.ndarray data object.

    """
    if type(img) is not np.ndarray:
        raise TypeError('Image must be a numpy array')
    img_new = img.copy()
    if prob_sup != 1:
        tmp = np.quantile(img_new.ravel(), q=prob_sup)
        img_new[img_new > tmp] = tmp
    if prob_inf != 0:
        tmp = np.quantile(img_new.ravel(), q=prob_inf)
        img_new[img_new < tmp] = tmp
    return img_new

def array2nifti(img, img_header, img_affine):
    """
    Converts numpy array to nifti Image object
    Args:
        img (np.ndarray): Numpy array containing neuroimaging data.
        img_header (Nifti1Header): Header to be used (in nib format)
        img_affine (np.ndarray): Affine transform from scanner coords to real world coords.
    Return:
        Nibabel NiftiImage.
    """
    if type(img) is not np.ndarray:
        raise TypeError('Image must be a numpy array')
    if type(img_affine) is not np.ndarray:
        raise TypeError('Affine transform must be a numpy array')
    if type(img_header) is not nib.nifti1.Nifti1Header:
        raise TypeError('Header must be a nib header object')
    new_img = nib.Nifti1Image(img, header=img_header, affine=img_affine)
    return new_img


def plot_imim(img, plane, slices, title, output_file):
    """
    Takes a nifti image and returns a plot showing a set of slices in the desired plane.
    Args:
        img (nib.nifti1.Nifti1Image): Nifti object.
        plane (str): One of the following planes: 'x', 'y', 'z'
        slices (list): List indicating the slices to be plotted. For instance: [10, 20, 30, 50].
        title (str).
        output_file (str): output fle to be passed to nilearn
    Returns:
        Nilearn plot.
    """
    if type(img) is not nib.nifti1.Nifti1Image:
        raise TypeError('Image must be a nibabel NIFTI object')
    if type(plane) is not str:
        raise TypeError("Plane arg must be a str indicating the plane to be plotted: 'x', 'y' or 'z'")
    if type(slices) is not list:
        raise TypeError('Slices must be a list indicating the slices to be plotted: e.g., [10, 20, 30]')
    if type(title) is not str:
        raise TypeError('Title must be a string')
    niplot.plot_anat(img, display_mode=plane, cut_coords=slices, title=title, output_file=output_file)
