# Data-plotter-folder-scanner
Cathode processing data plotter folder scanner
This script iteratively processes all CSV files within a specified di-
rectory, each containing timestamped voltage and current readings
from a high-voltage system, and generates dual-axis plots showing
the power supply voltage (IGLGL01HVPSkVolts_ave) and ion pump
current (VIPGT04cur) as a function of time. Each file is parsed into
a DataFrame with fixed column names and date-time formatting,
then passed to a plotting function that produces a figure with volt-
age on the primary y-axis and current on the secondary y-axis, both
sharing a common time-based x-axis. The resulting figures are la
beled with the original file name and saved as PNG files in the same
directory
