if __name__ == '__main__':
    import sys
    import os
    from mri_funs import mreye_funs as mreye

    print(sys.argv[1])
    start_dir = sys.argv[1]
    subjects = sys.argv[2]
    sufix = sys.argv[3]
    seq = sys.argv[4]
    plane = sys.argv[5]
    coords = sys.argv[6]
    out = sys.argv[7]

    slices = list(map(float, coords.strip('[]').split(',')))

    with open(subjects, 'r') as subjects:
        for subject in subjects:
            subject = str(subject).replace('\n', '')
            visit = subject + sufix
            file = seq + '.nii.gz'
            mri = os.path.join(start_dir, subject, visit, seq, file)
            out = out + '/' + subject + '_' + seq
            a, b = mreye.load_nifti(mri)
            b = mreye.adjust_contrast(b)
            c = mreye.array2nifti(b, img_header=a.header, img_affine=a.affine)
            mreye.plot_imim(img=c, plane=plane, slices=slices, title=subject, output_file=out)
            out = sys.argv[7]