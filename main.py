from statistics import mean, variance
import matplotlib.pyplot as plt

from incremental_statistics import IncrementalStatistics

def calc_error(num: int, use_kahan = True, calc_ape=True) -> tuple:
    """calculate error

    Args:
        num (int): num of iterate
        use_kahan (bool, optional): use kahan algorithm. Defaults to True.
        calc_ape (bool, optional): calculate error on absolute percentage error. Defaults to True.

    Returns:
        tuple: error of sum, variance
    """
    inc = IncrementalStatistics(use_kahan)
    val_list = []
    err_mean = []
    err_var = []

    for i in range(num):
        val = 1e8 / pow(10, i)
        inc.add_data(val)
        val_list.append(val)
        if len(val_list) > 1:
            val_mean = abs(inc.get_mean() - mean(val_list))
            val_var = abs(inc.get_unvariance() - variance(val_list))
            if calc_ape:
                val_mean = val_mean / mean(val_list) * 100.0
                val_var =  val_var / variance(val_list) * 100.0
            err_mean.append(val_mean)
            err_var.append(val_var)

    return (err_mean, err_var)

def main():
    """ main function
    """
    
    iter_num = 250
    calc_ape = True

    err_mean_kahan, err_var_kahan = calc_error(iter_num, calc_ape=calc_ape)
    err_mean_normal, err_var_normal = calc_error(iter_num, False, calc_ape)

    # plot error
    unit_str = '(Percent)' if calc_ape else '(Absolute Error)'
    plt.subplot(2, 1, 1)
    plt.plot(range(iter_num-1), err_mean_kahan, label='kahan')
    plt.plot(range(iter_num-1), err_mean_normal, label='normal')
    plt.legend()
    plt.title('mean error' + unit_str)

    plt.subplot(2, 1, 2)
    plt.plot(range(iter_num-1), err_var_kahan, label='kahan')
    plt.plot(range(iter_num-1), err_var_normal, label='normal')
    plt.legend()
    plt.title('variance error' + unit_str)

    plt.tight_layout()
    plt.show()


if __name__ == '__main__':
    main()

