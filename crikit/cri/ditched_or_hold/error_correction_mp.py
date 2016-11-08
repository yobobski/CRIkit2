# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 21:35:10 2016

@author: chc
"""


import numpy as _np
import copy as _copy

from scipy.signal import savgol_filter as _sg

from crikit.cri.algorithms.kk import hilbertfft as _hilbert

#from crikit.preprocess.algorithms.als import (als_baseline as _als_baseline,
#                                              als_baseline_redux as
#                                              _als_baseline_redux)

from crikit.preprocess.algorithms.als_mp import (ALS as _ALS)

from crikit.utils.datacheck import _rng_is_pix_vec


class PhaseErrCorrectALS_MP:
    """
    Phase error correction using alternating least squares (ALS)

    Reference
    ---------
    * C H Camp Jr, Y J Lee, and M T Cicerone, JRS (2016).
    """
    def __init__(self, smoothness_param=1, asym_param=1e-2, redux=10, 
                 redux_interp=True, print_iteration=False, rng=None):
        
        self.smoothness_param = smoothness_param
        self.asym_param = asym_param
        self.redux = redux
        self.redux_interp = redux_interp
        self.print_iteration = print_iteration
        
        self.rng = _rng_is_pix_vec(rng)
        
        self._als_method = _ALS(smoothness_param=self.smoothness_param,
                                asym_param=self.asym_param,
                                redux=self.redux, 
                                redux_interp=self.redux_interp,
                                print_iteration=self.print_iteration)

    def _calc(self, data, ret_obj, **kwargs):

#        try:
#            shp = data.shape[0:-2]
#            total_num = _np.array(shp).prod()
    
#            for num, blk in enumerate(data):
#                print('Detrended iteration {} / {}'.format(num, total_num))

        ph = _np.unwrap(_np.angle(data))

        if self.rng is None:
            err_phase = self._als_method.calculate(ph)
        else:
            err_phase = self._als_method.calculate(ph[..., self.rng])

        h = _np.zeros(err_phase.shape)
        
        if h.ndim <= 2:
            h += _hilbert(err_phase)
        else:
            for num, blk in enumerate(err_phase):
#                print('Detrended iteration {} / {}'.format(num+1, _np.array(err_phase.shape[0:-2]).prod()))
                h[num,:] = h[num,:] + _hilbert(blk)

        correction_factor = 1/_np.exp(h.imag) * _np.exp(-1j*err_phase)

        if self.rng is None:
            ret_obj *= correction_factor
        else:
            ret_obj[..., self.rng] *= correction_factor
                
#        except:
#            return False
#        else:
        return True

    def calculate(self, data):

        data_copy = _copy.deepcopy(data)
        
        success = self._calc(data, ret_obj=data_copy)
        if success:
            return data_copy
        else:
            return None

    def transform(self, data):
        

        success = self._calc(data, ret_obj=data)
        return success

class ScaleErrCorrectSG:
    """
    Scale error correction using Savitky-Golay

    Reference
    ---------
    * C H Camp Jr, Y J Lee, and M T Cicerone, JRS (2016).
    """
    def __init__(self, win_size=601, order=2, rng=None):
        self.win_size = win_size
        self.order = order
        self.rng = _rng_is_pix_vec(rng)

    def _calc(self, data, ret_obj):
        try:
            if self.rng is None:
                correction_factor = _sg(data.real, window_length=self.win_size,
                                        polyorder=self.order, axis=-1)
            else:
                correction_factor = _sg(data[..., self.rng].real,
                                        window_length=self.win_size,
                                        polyorder=self.order, axis=-1)

            correction_factor[correction_factor == 0] = 1
            correction_factor **= -1

            if self.rng is None:
                ret_obj *= correction_factor
            else:
                ret_obj[..., self.rng] *= correction_factor
        except:
            return False
        else:
            return True

    def calculate(self, data):

        data_copy = _copy.deepcopy(data)
        success = self._calc(data, ret_obj=data_copy)
        if success:
            return data_copy
        else:
            return None

    def transform(self, data):
        success = self._calc(data, ret_obj=data)
        return success


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    from crikit.cri.kk import KramersKronig
    import timeit

    SPECT_LEN = 878
    WN = _np.linspace(4000, 500, SPECT_LEN)
    chi = (1 / ((WN - 1000 - 1j * 10)) +
           1 / ((WN - 1020 - 1j * 10)) +
           1 / ((WN - 2800 - 1j * 10)))
    chiNR = 0*chi + 0.055
    exc = WN
    sig = _np.abs(chi + chiNR)**2

    sigNR = _np.abs(chiNR)**2
    sigRef = chiNR*(WN/1e3)**.5

    NUM_REPS = 50

    kk = KramersKronig()
    kkd = kk.calculate(sig, sigRef)
    #kkd = _np.dot(_np.random.rand(NUM_REPS,NUM_REPS,1)*_np.ones((NUM_REPS, NUM_REPS, 1)), kkd[None, :])
    kkd = _np.dot(_np.ones((NUM_REPS, NUM_REPS, 1)), kkd[None, :])
#    plt.plot(chi.imag/chiNR.real, label='Ideal')
    plt.plot(kkd[5, 5, :].imag, label='Before Correction')

    start = timeit.default_timer()
    phase_err_correct_als = PhaseErrCorrectALS_MP()
    out = phase_err_correct_als.calculate(kkd)
#    success = phase_err_correct_als.transform(kkd)
#    print('Success? : {}'.format(success))
    stop = timeit.default_timer()
    print('Sec/spectrum: {:.3g}'.format((stop-start)/NUM_REPS**2))

    
#    
    plt.plot(out[5,5,:].imag.T, label='After PhErr Corr.')
    plt.legend()
    plt.show()
#    scale_err_correct_sg = ScaleErrCorrectSG()
#    success = scale_err_correct_sg.transform(kkd)
#    print('Success? : {}'.format(success))
#    plt.plot(kkd[5, 5, :].imag, label='After Correction')
#    plt.legend(loc='best')
#    plt.show()

#    scale_err_correct_sg = ScaleErrCorrectSG()
#    out = scale_err_correct_sg.calculate(kkd[0,0,:])
#    plt.plot(out.imag)
#    
#    scale_err_correct_sg = ScaleErrCorrectSG(win_size=11, order=2)
#    out = scale_err_correct_sg.calculate(kkd[0,0,:])
#    plt.plot(out.imag)
#    
#    plt.show()
    
#
#    phase_err_correct_als = PhaseErrCorrectALS(print_iteration=False)
#    out = phase_err_correct_als.calculate(kkd)
#    
#    plt.plot(out[0,0,:].imag)
#    
#    phase_err_correct_als = PhaseErrCorrectALS(smoothness_param=1e1, 
#                                                asym_param=1e-2,
#                                                redux_factor=1)
    
    
#    print(phase_err_correct_als._k)