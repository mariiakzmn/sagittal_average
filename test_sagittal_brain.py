import numpy as np
import subprocess

data_input = np.zeros((20, 20))
data_input[-1, :] = 1
np.savetxt("brain_sample.csv", data_input, fmt='%d', delimiter=',')

subprocess.run(["python", "sagittal_brain.py"])

# data_output = np.mean(data_input, axis=1)[np.newaxis, :]
# np.savetxt("brain_average.csv", data_output, fmt='%d', delimiter=',')

data_output = np.loadtxt("brain_average.csv", dtype=float,  delimiter=',')
expected = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]])

np.testing.assert_array_equal(data_output, expected)