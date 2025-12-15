#
//  timepass.py
//  
//
//  Created by kushal on 09/12/25.
//

import matplotlib.pyplot as plt
import numpy as np

ages = np.random.normal(loc=30, scale=5, size=1000  )
plt.hist(ages, bins=10)
plt.show()
