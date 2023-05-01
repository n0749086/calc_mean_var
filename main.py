from statistics import mean, variance

from incremental_statistics import IncrementalStatistics

inc = IncrementalStatistics()
s = []

for i in range(100):
    val = 10000000.0 / pow(10, i)
    inc.add_data(val)
    s.append(val)
    if len(s) > 1:
        print(inc.get_mean() - mean(s), inc.get_unvariance() - variance(s))
