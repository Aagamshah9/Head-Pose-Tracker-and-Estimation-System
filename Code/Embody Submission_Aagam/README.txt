%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                        README
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                     Requirements
                                    ______________
1. Python - 3.6.12  
2. Tensorflow - 2.2.0
3. Opencv(cv2) - 4.4.0
4. Numpy - 1.19.4
5. dlib - 19.21.0

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                    Installations
                                   _______________

To install Python and Dlib library in virtual enviornment

1. Download anaconda for python 3.6 from https://www.anaconda.com/download/
2. Open Anaconda Prompt in Administrative mode.
3. Make sure that all conda libraries are up-to-date. Type in anaconda command prompt:
   conda update conda
   conda update anaconda 
4. Create a new environment
   conda create -n dlib_env python=3.6
5. Activate the conda environment
   conda activate dlib_env
6. Install dlib
   conda install -c conda-forge dlib
7. Check dlib version in interpreter	
   python
   >>> import dlib
   >>> dlib.__version__
8. Exit and deactivate the env
   >>> exit()
   deactivate
########################################################################################

To create and launch the kernel in the jupyter notebook

1. In the Anaconda command prompt type 
   source activate myenv
   python -m ipykernel install --user --name myenv --display-name "dlib_env"

This will create and launch your kernel in the dlib_env (virtual environment)

2. Now open Anaconda command prompt and type
   conda activate dlib_env
   conda install numpy==1.19.4
   conda install -c conda-forge opencv
   conda install tensorflow==2.2.0
   jupyter notebook

3. Now we are set to run the code in the jupyter notebook in our virtual enviornment 
   once it is launched.

########################################################################################

Place all the data files (images and videos), pretrained models, function files, 
images and models folder in the same path and directory as that of the code.

Now you should be good to go and run all the codes and view the outputs of each program
being executed.

Please use only ESC key to close the output window after it is viewed or observed, just
to keep it simple and error free.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                                       THANK YOU
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
