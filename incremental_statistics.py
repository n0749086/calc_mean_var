'''
https://zenn.dev/utcarnivaldayo/articles/ffeed5ac2e62bb
'''

class IncrementalStatistics(object):
    def __init__(self) -> None:
        self.__mean = 0.0
        self.__count = 0
        self.__m_2 = 0.0
        self.__c_mean = 0.0
        self.__c_m_2 = 0.0

    def clear(self) -> None:
        self.__init__()

    @staticmethod
    def kahan(sum: float, c: float, data: float):
        '''
        https://ja.wikipedia.org/wiki/%E3%82%AB%E3%83%8F%E3%83%B3%E3%81%AE%E5%8A%A0%E7%AE%97%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
        '''
        y = data - c
        t = sum + y
        c = (t - sum) - y
        sum = t

        return (sum, c)

    def add_data(self, data: float) -> tuple:
        self.__count += 1
        # meanの計算
        delta = data - self.__mean
        self.__mean, self.__c_mean = self.kahan(self.__mean, self.__c_mean, delta / self.__count)

        # varの計算
        delta_var = data - self.__mean
        self.__m_2, self.__c_m_2 = self.kahan(self.__m_2, self.__c_m_2, delta * delta_var)

    def get_mean(self):
        return self.__mean
    
    def get_variance(self):
        if self.__count == 0:
            return 0.0
        else:
            return self.__m_2 / self.__count
    
    def get_unvariance(self) -> float:
        if self.__count == 0:
            return 0.0
        else:
            return self.__m_2 / (self.__count - 1)
