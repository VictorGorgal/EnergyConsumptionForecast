from send_data import get_data_from_date, reduce_data
import matplotlib.pyplot as plt
import numpy as np

# date = get_data_from_date('7/5/2022')
date = get_data_from_date('8/5/2022')
# date = get_data_from_date('9/5/2022')
# date = get_data_from_date('10/5/2022')
date = reduce_data(date)

x = np.linspace(0, 24, 48)
plt.plot(x, date)
plt.xlabel('hour')
plt.ylabel('W')
plt.show()
