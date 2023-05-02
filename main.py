from statistics import mean, variance
import matplotlib.pyplot as plt

from incremental_statistics import IncrementalStatistics

inc = IncrementalStatistics()
s = []

err_mean = []
err_var = []

NUM = 100
CALC_APE = True # calc on absolute percentage error

for i in range(NUM):
    val = 10000000.0 / pow(10, i)
    inc.add_data(val)
    s.append(val)
    if len(s) > 1:
        val_mean = abs(inc.get_mean() - mean(s))
        val_var = abs(inc.get_unvariance() - variance(s))
        if CALC_APE:
            val_mean = val_mean / mean(s) * 100.0
            val_var =  val_var / variance(s) * 100.0
        err_mean.append(val_mean)
        err_var.append(val_var)

# plot error
UNIT_STR = '(Percent)' if CALC_APE else '(Absolute Error)'
plt.subplot(2, 1, 1)
plt.plot(range(NUM-1), err_mean)
plt.title('mean error' + UNIT_STR)

plt.subplot(2, 1, 2)
plt.plot(range(NUM-1), err_var)
plt.title('variance error' + UNIT_STR)

plt.tight_layout()
plt.show()
