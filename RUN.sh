#!/bin/bash
python3 extract_scalar.py
python3 convert_grid.py
python3 simplify_fields.py
python3 simplify_fields_move.py
python3 get_cp.py
python3 compute_grad.py
python3 make_cp_zeros.py
python3 convert_vti1.py
python3 convert_vti2.py
python3 extract_subpoints.py
python3 sublevel_script.py
python3 extract_connectivity.py
python3 sublevel_script_deg.py
python3 write_csv.py
python3 test.py
python3 obtain.py

