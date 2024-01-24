
# Jacobi Set Simplification

The implementation has been done for time varying 2D scalar fields given as a 3D vti file(as in the ETH datasets).  
Execute the RUN.sh file.(All the scripts are executed in the order described in this file). For doing so, run the following commands on the terminal in this directory:  
- chmod a+x RUN.sh  
- ./RUN.sh

By the end of the execution, the Simplified Jacobi Set will be obtained as graph_(critical type).vtk  
Finally, add the number of edges(which will be printed) in the graph_(critical  type).vtk file and 3x(# of edges)  
Now to understand the contribution of each script:  
- **extract_scalar.py** - Returns the scalar fields of each timestep as seperate files. This requires changes if the input data is presented in a different format. This returns the scalar fields in csv format.  
- **convert_grid** - Takes in the csv files and makes them into a .vtk file on a uniform unit grid from the origin(0,0,0).  
- **simplify_fields.py** - simplifies the scalar fields via persistence.  
- **simplify_fields_move.py** - the same fields are moved for better visualization  
- **get_cp** - critical points are computed and stored as csv files.  
- **compute_grad.py** - computes the gradient magnitude fields are .raw files  
- **make_cp_zeros.py** - artifically makes the gradient magnitude values at the critical points zero.  
- **convert_vti1&2.py**- converts the raw files to vti.  
- **extract_subpoints.py** - computes the points on the gradient magnitude grid which have values lesser than delta.  
- **sublevel_script.py** - builds the sublevel sets from the subpoints  
- **extract_connectivity.py** - computes the connectivity of the sublevel sets  
- **sublevel_script_deg.py** - removes the degree zero components and also retains ony components specified by the critical type filter.  
- **write_csv.py** - required for the internal functioning of the nested tracking graph implementation on TTK/Paraview  
- **test.py** - computes the tracking graph from the components obtained from sublevel_script_deg.py  
- **obtain.py** - gives the simplified jacobi set from the tracking graph. This file considers the length threshold.  

Number of edges and the 3X(Number of edges) must be added to the "Lines" line of the final graph_(critical type).vtk file. This is the simplified Jacobi Set.  
A final post processing step for temporal consistency is required.  
One need not run all the files always from the beginning. Depending on the changes made one can run them accordingly.     

Note: The paramters can be changed in the parameters.py file. The critical type filter has also been implemented.
