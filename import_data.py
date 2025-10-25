import numpy as np
T = 12
Delta_t = 5 / 60
params = {
    'num_cont_tcl': 2,
    'num_disc_tcl': 2,
    'num_ess': 2,
    'C_L': 0.0,
    'C_U': 30.0,
    'C_cont': [316.11, 140.56],
    'eta_cont': [4.0, 4.0],
    'H_cont': [3.892, 0.92092],
    'p_cont_max_tcl': [17.4, 7.69],
    'theta_min_cont': [21.0, 21.0],
    'theta_max_cont': [25.0, 25.0],
    'theta_set_cont': [23.0, 23.0],
    'C_disc': [95.5, 170.42],
    'eta_disc': [3.6, 3.6],
    'H_disc': [1.96, 2.10],
    'p_disc_max_tcl': [15.73, 10.46],
    'theta_min_disc': [21.0, 21.0],
    'theta_max_disc': [25.0, 25.0],
    'theta_set_disc': [23.0, 23.0],
    'eta_chg': [0.97, 0.98],
    'eta_dis': [0.98, 0.97],
    'pmax_chg_ess': [25.0, 10.0],
    'pmax_dis_ess': [25.0, 10.0],
    'e_min': [0.0, 0.0],
    'e_max': [50.0, 40.0],
}
data = np.load('profiles_data.npz')
full_p_bl, full_p_pv, full_theta_amb = 20 * data['load_data'], 40 * data['pv_data'], data['temp_data']
